# self_py_fun/HW8Fun.py
import os
import numpy as np
import matplotlib.pyplot as plt


def produce_trunc_mean_cov(eeg_trunc_signal_3d, eeg_trunc_type, E_val):

    tar_idx = np.where(eeg_trunc_type == 1)[0]
    ntar_idx = np.where(eeg_trunc_type == -1)[0]

    num_trials, E_val, length_per_electrode = eeg_trunc_signal_3d.shape

    signal_tar_mean = np.zeros((E_val, length_per_electrode))
    signal_ntar_mean = np.zeros((E_val, length_per_electrode))
    signal_tar_cov = np.zeros((E_val, length_per_electrode, length_per_electrode))
    signal_ntar_cov = np.zeros((E_val, length_per_electrode, length_per_electrode))
    signal_all_cov = np.zeros((E_val, length_per_electrode, length_per_electrode))

    for e in range(E_val):
        signal_tar_mean[e, :] = np.mean(eeg_trunc_signal_3d[tar_idx, e, :], axis=0)
        signal_ntar_mean[e, :] = np.mean(eeg_trunc_signal_3d[ntar_idx, e, :], axis=0)
        signal_tar_cov[e, :, :] = np.cov(eeg_trunc_signal_3d[tar_idx, e, :], rowvar=False)
        signal_ntar_cov[e, :, :] = np.cov(eeg_trunc_signal_3d[ntar_idx, e, :], rowvar=False)
        signal_all_cov[e, :, :] = np.cov(eeg_trunc_signal_3d[:, e, :], rowvar=False)

    return [signal_tar_mean, signal_ntar_mean, signal_tar_cov, signal_ntar_cov, signal_all_cov]


def plot_trunc_mean(eeg_tar_mean, eeg_ntar_mean, subject_name, time_index, E_val, electrode_name_ls, save_dir='K114'):

    os.makedirs(save_dir, exist_ok=True)
    fig, axes = plt.subplots(4, 4, figsize=(14, 10))
    axes = axes.ravel()

    for e in range(E_val):
        axes[e].plot(time_index, eeg_tar_mean[e, :], color='r', label='Target')
        axes[e].plot(time_index, eeg_ntar_mean[e, :], color='b', label='Non-Target')
        axes[e].set_title(electrode_name_ls[e])
        axes[e].set_xlabel("Time (ms)")
        axes[e].set_ylabel("Amplitude (μV)")

    plt.suptitle(f"Subject {subject_name} - Target vs Non-Target Means")
    axes[0].legend()
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(os.path.join(save_dir, "Mean.png"), dpi=300)
    plt.close()


def plot_trunc_cov(eeg_cov, cov_type, time_index, subject_name, E_val, electrode_name_ls, save_dir='K114'):

    os.makedirs(save_dir, exist_ok=True)
    fig, axes = plt.subplots(4, 4, figsize=(14, 12))
    axes = axes.ravel()

    for e in range(E_val):
        t, y = np.meshgrid(time_index, time_index)
        axes[e].contourf(t, y, eeg_cov[e, :, :], cmap='viridis')
        axes[e].set_title(electrode_name_ls[e])
        axes[e].set_xlabel("Time (ms)")
        axes[e].set_ylabel("Time (ms)")

    plt.suptitle(f"{subject_name} - {cov_type} Covariance")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    filename = os.path.join(save_dir, f"Covariance_{cov_type}.png")
    plt.savefig(filename, dpi=300)
    plt.close()
