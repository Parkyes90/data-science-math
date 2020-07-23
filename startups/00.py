import warnings
warnings.simplefilter("ignore")
import matplotlib as mpl
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import numpy as np
import scipy as sp
import pandas as pd
import statsmodels.api as sm
import sklearn as sk

mpl.use("Agg")

sns.set()
sns.set_style("whitegrid")
sns.set_color_codes()