import numpy as np
import os

time_width = int(9)

fs = 8000
win_size = int(0.025 * fs)  # The number of samples in window
win_step = int(0.010 * fs)
# nfft = np.int(2 ** (np.floor(np.log2(win_size) + 1)))
nfft = np.int(256)

freq_size = int(nfft/2+1)

lr = 0.0001
lrDecayRate = .99  # 0.99
lrDecayFreq = 2000

keep_prob = 0.9

device = '/gpu:1'

# logs_dir = os.path.abspath('../logs')

dist_num = int(8)

max_epoch = int(2e6)

batch_size = int(256)

test_batch_size = batch_size

val_step = int(20)
summary_step = int(3000)  # 3000
summary_fnum = int(1)

mode = "fnn"