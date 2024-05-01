#!/bin/bash
#SBATCH -J Model_Training
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --ntasks-per-node=4
#SBATCH --partition=ai-tenn
#SBATCH --qos=ai-tenn
#SBATCH --gpus=4
#SBATCH --output=Model_Training.o%j
#SBATCH --error=Model_Training.e%j
#SBATCH --account=ISAAC-UTK0281

######### run the script ##############
CUDA_LAUNCH_BLOCKING=1 python train_model.py