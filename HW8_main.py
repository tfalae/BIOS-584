# HW8_main.py

import os
import numpy as np
import scipy.io as sio

from HW7 import E_val
from self_py_fun.HW8Fun import produce_trunc_mean_cov, plot_trunc_mean, plot_trunc_cov


data = sio.loadmat(r'C:\Users\temif\OneDrive\Documents\GitHub\BIOS-584\data\K114_001_BCI_TRN_Truncated_Data_0.5_6.mat')


eeg_trunc_signal = data['Signal']
eeg_trunc_type = data['Type'].flatten()
E_val = 16
signal_tar_mean = np.zeros((E_val, length_per_electrode))
time_index = np.arange(signal_tar_mean.shape[1])
electrode_name_ls = [str(x[0]) for x in data['LetterTable'].flatten()]



num_trials = eeg_trunc_signal.shape[0]
length_per_electrode = eeg_trunc_signal.shape[1] // E_val
eeg_trunc_signal_3d = eeg_trunc_signal.reshape(num_trials, E_val, length_per_electrode)

signal_tar_mean, signal_ntar_mean, signal_tar_cov, signal_ntar_cov, signal_all_cov = \
    produce_trunc_mean_cov(eeg_trunc_signal_3d, eeg_trunc_type, E_val)

save_dir = 'K114'
plot_trunc_mean(signal_tar_mean, signal_ntar_mean, 'K114', time_index, E_val, electrode_name_ls, save_dir)
plot_trunc_cov(signal_tar_cov, 'Target', time_index, 'K114', E_val, electrode_name_ls, save_dir)
plot_trunc_cov(signal_ntar_cov, 'Non-Target', time_index, 'K114', E_val, electrode_name_ls, save_dir)
plot_trunc_cov(signal_all_cov, 'All', time_index, 'K114', E_val, electrode_name_ls, save_dir)

print("All 4 figures saved under folder K114")
