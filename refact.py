from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "smallcloudai/Refact-1_6B-fim"
# "cuda" for gpu
device = "cpu" 

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True).to(device)

prompt_template = "<empty_output>SYSTEM {system}\n" \
                  "<empty_output>USER {query}\n" \
                  "<empty_output>ASSISTANT"
prompt = prompt_template.format(system="You are a programming assistant",
                                query="Can you write Fortran code to add two numbers?")

inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
outputs = model.generate(inputs, max_length=100, temperature=0.2)
print("-"*80)
print(tokenizer.decode(outputs[0]))
