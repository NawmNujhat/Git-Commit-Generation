import csv
import os
import random

from dotenv import load_dotenv
from langchain_community.chat_models import ChatDeepInfra, ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
import pandas as pd
from extract_diff import import_dataset
from src.CodeT5Wrapper import CodeT5Wrapper
from src.extract_diff import import_subset_for_local_machine

load_dotenv()

LLMS = {
    'deepinfra': ChatDeepInfra(model="databricks/dbrx-instruct", temperature=0),
    'ollama/starcoder2': ChatOllama(model="ollama/starcoder2", temperature=0),
    'codet5':CodeT5Wrapper(model_name="Salesforce/codet5-base")
}


def call_model_sync(model, messages):
    llm = LLMS[model]
    if model in ["codet5"]:
        return llm.invoke(messages)
    else:
       resp = llm.invoke(messages)
    return resp.content


if __name__ == "__main__":
    # TODO: check whether we agree with this dataset
    output_dir="output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    train_dataset, validation_dataset, test_dataset = import_dataset("Maxscha/commitbench")
    model_name=input("Enter the model name: ")
    subset=None
    if model_name in ["codet5"]:
       indices=random.sample(range(len(train_dataset)), 10)
       subset=train_dataset.select(indices)
    # Open the CSV file for writing
    with open(os.path.join(output_dir,"output.csv"), mode="w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header row
        csv_writer.writerow(["Original Message", "Model Output"])
        if model_name == "codet5":
            for row in subset:
                diff=row['diff']
                original_message=row['message']
                message = [
                SystemMessage(
                    content="Be a helpful assistant with knowledge of git message conventions."
                ),
                HumanMessage(
                    content=f"Summarize this git diff into a useful, 10 words commit message: {diff}"
                ),
              ]

            # Call the model and get the output
                model_output = call_model_sync('codet5', message)

            # Write the row to the CSV file
                csv_writer.writerow([original_message, model_output])

        else:
        # Iterate through the dataset
         for item in train_dataset:
            diff = item['diff']
            original_message = item['message']

            # Create the input message for the model
            message = [
                SystemMessage(
                    content="Be a helpful assistant with knowledge of git message conventions."
                ),
                HumanMessage(
                    content=f"Summarize this git diff into a useful, 10 words commit message: {diff}"
                ),
            ]

            # Call the model and get the output
            model_output = call_model_sync('deepinfra', message)

            # Write the row to the CSV file
            csv_writer.writerow([original_message, model_output])

    df=pd.read_csv(os.path.join(output_dir,"output.csv"))
    print(df)