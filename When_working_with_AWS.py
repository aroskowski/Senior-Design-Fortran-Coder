#this has to be done in a virtual environment and is at ~/venv
#more info here: https://oit.utk.edu/hpsc/isaac-open-enclave-new-kpb/anaconda-user-guide_ng/
#using the venv can be found here: https://oit.utk.edu/hpsc/isaac-open-enclave-new-kpb/pip-and-venv-user-guide_ng/
#you have to run it in batches 
#more info found here: https://oit.utk.edu/hpsc/isaac-open-enclave-new-kpb/running-jobs-new-cluster-kpb/
from transformers import Trainer, TrainingArguments
from transformers import AutoModelForMaskedLM, AutoTokenizer
import numpy as np 

hyperparameters = {
    'model_name_or_path': 'TheBloke/CodeLlama-7B-GGUF',
    'output_dir': '/lustre/isaac/proj/UTK0281/training_environment/output_trainingfile',
    'train_file': 'Senior-Design-Fortran-Coder/datasets/output_file1.txt',
    'validation_file': '/path/to/validation/file.txt',
    'per_device_train_batch_size': 8,
    'per_device_eval_batch_size': 8,
    'num_train_epochs': 3,
    'save_steps': 1000,
    'save_total_limit': 2,
    'logging_dir': '/path/to/logging/dir',
}

tokenizer = AutoTokenizer.from_pretrained(hyperparameters['model_name_or_path'])
model = AutoModelForMaskedLM.from_pretrained(hyperparameters['model_name_or_path'])

training_args = TrainingArguments(
    output_dir=hyperparameters['output_dir'],
    overwrite_output_dir=True,
    per_device_train_batch_size=hyperparameters['per_device_train_batch_size'],
    per_device_eval_batch_size=hyperparameters['per_device_eval_batch_size'],
    num_train_epochs=hyperparameters['num_train_epochs'],
    save_steps=hyperparameters['save_steps'],
    save_total_limit=hyperparameters['save_total_limit'],
    logging_dir=hyperparameters['logging_dir'],
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenizer.masked_lm_train_dataset(hyperparameters['train_file']),
    eval_dataset=tokenizer.masked_lm_train_dataset(hyperparameters['validation_file']),
)

trainer.train()

