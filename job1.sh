#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=03:00:00
#SBATCH --ntasks-per-node=5
#SBATCH --account=ACF-UTK0011
#SBATCH --partition=campus
#SBATCH --qos=campus
#SBATCH --output=temp

######### run the script ##############
python train_model.py
