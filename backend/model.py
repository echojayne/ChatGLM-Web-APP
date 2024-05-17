from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "path/to/checkpoints"
device = 'cuda:2'

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True).to(device)
model.eval()

def chat(input_text, history=[]):
    response_text, _  = model.chat(tokenizer, input_text, history)
    return response_text
