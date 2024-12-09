from transformers import AutoModelForSeq2SeqLM, T5Tokenizer, T5ForConditionalGeneration
from transformers import AutoTokenizer


class T5Wrapper:
    def __init__(self, model_name):# Load model directly
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def invoke(self,prompt):
        inputs=self.tokenizer(prompt,return_tensors="pt",truncation=True,max_length=512)
        outputs=self.model.generate(inputs.input_ids, max_length=50,num_beams=5,early_stopping=True)
        return self.tokenizer.decode(outputs[0],skip_special_tokens=True)