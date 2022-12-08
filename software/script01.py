import os
import numpy as np
import scipy
import scipy.stats as st
import scipy.optimize
from scipy import special
import pandas as pd
import iqplot
import numba
import tqdm
import itertools
import warnings
import bebi103
import bokeh.io
import bokeh.plotting
bokeh.io.output_notebook()

#import data
data_path = "https://s3.amazonaws.com/bebi103.caltech.edu/data/"
fname = os.path.join(data_path,'gardner_mt_catastrophe_only_tubulin.csv')
df=pd.read_csv(fname, comment="#")

#separate data into numpy arrays for later use
c12=df["12 uM"].values
c12 = c12[~np.isnan(c12)]
c07=df["7 uM"].values
c07 = c07[~np.isnan(c07)]
c09=df["9 uM"].values
c09 = c09[~np.isnan(c09)]
c10=df["10 uM"].values
c10 = c10[~np.isnan(c10)]
c14=df["14 uM"].values
c14 = c14[~np.isnan(c14)]