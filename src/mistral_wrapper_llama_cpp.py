import os

from dotenv import load_dotenv
from llama_cpp import Llama

load_dotenv()
class LlamaMistralWrapper:

    def __init__(self):
         self.llm=Llama(model_path=os.environ['MODEL_PATH_MISTRAL'],
                        chat_format="llama-2",
                        n_ctx=int(os.environ['CONTEXT_WINDOW_FOR_MISTRAL']),
                        n_gpu_layers=int(os.environ['GPU_LAYERS']),
                        verbose=True)

    def __del__(self):
        if hasattr(self, 'llm'):
            del self.llm
    print("Loaded Mistral")
    def invoke(self, prompt):
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates meaningful git commit messages."},
            {"role": "user", "content": prompt}
        ]
        print("Generating Outputs")
        output=self.llm.create_chat_completion(messages,max_tokens=1024)
        return output['choices'][0]['message']['content'].strip()
