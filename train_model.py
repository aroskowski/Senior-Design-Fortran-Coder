#this has to be done in a virtual environment and is at ~/venv
#more info here: https://oit.utk.edu/hpsc/isaac-open-enclave-new-kpb/anaconda-user-guide_ng/
#using the venv can be found here: https://oit.utk.edu/hpsc/isaac-open-enclave-new-kpb/pip-and-venv-user-guide_ng/
#you have to run it in batches 
#more info found here: https://oit.utk.edu/hpsc/isaac-open-enclave-new-kpb/running-jobs-new-cluster-kpb/
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from datasets import load_dataset
from transformers import TrainerCallback
import torch
import os
#trying this on one
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"


class GradientCheckpointingCallback(TrainerCallback):
    def on_train_begin(self, args, state, control, model=None, **kwargs):
        model.gradient_checkpointing_enable()


# Set up the tokenizer
tokenizer = AutoTokenizer.from_pretrained("/lustre/isaac/proj/UTK0281/CodeLlama-7b-Instruct-hf")
tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# Set up the model
model = AutoModelForCausalLM.from_pretrained("/lustre/isaac/proj/UTK0281/CodeLlama-7b-Instruct-hf")
model.resize_token_embeddings(len(tokenizer))

dataset = load_dataset("text", data_files={"train": ["/lustre/isaac/proj/UTK0281/Senior-Design-Fortran-Coder/datasets/comments.txt", "/lustre/isaac/proj/UTK0281/Senior-Design-Fortran-Coder/datasets/code.txt"]}, name="fortran_dataset")

# Load your dataset from a local file
with open("/lustre/isaac/proj/UTK0281/Senior-Design-Fortran-Coder/datasets/comments.txt", "r", encoding="utf-8") as file:
    comments_data = file.readlines()

# Define the preprocessing function
def preprocess_function(examples):
    inputs = examples["text"]
    model_inputs = tokenizer(inputs, max_length=1024, truncation=True, padding="max_length", return_tensors="pt")
    labels = model_inputs["input_ids"].clone()
    return {"input_ids": model_inputs["input_ids"], "labels": labels}


# Apply the preprocessing function to the dataset
tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Set up training arguments and trainer
training_args = TrainingArguments(
    output_dir="/lustre/isaac/proj/UTK0281/output",
    per_device_train_batch_size=4,
    num_train_epochs=3
)

gradient_checkpointing_callback = GradientCheckpointingCallback()

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    tokenizer=tokenizer,
    data_collator=None,
    callbacks=[gradient_checkpointing_callback],

)

trainer.train()