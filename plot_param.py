import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
# Create 2x2 sub plots
gs = gridspec.GridSpec(2, 2)

rand = np.load("Random_param.npz")
rand = rand['l1'].flatten()

prop = np.load('Param_1024_1_divergence.npz')
prop = prop['w'].flatten()

plt.figure()

ax = plt.subplot(gs[0,0])
sns.distplot(rand, kde=True, rug=False, color= 'g')
plt.title("a)Randomly initialized")
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))


ax = plt.subplot(gs[0,1])
sns.distplot(prop * 1.06, kde=True, rug=False, color='r')
plt.title("b)After binwise pretraining")
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))


ax = plt.subplot(gs[1,:])
sns.distplot(prop * 1.06, kde=True, rug=False, color='r')
sns.distplot(rand, kde=True, rug=False, color= 'g')
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
plt.show()
