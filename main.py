#grading system main code
mport pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from matplotlib.ticker import MaxNLocator
import os
file_path=r"C:\Users\pravinkuyate\Downloads\Copy of Technical Training feedback of trainer.xlsx"
df=pd.read_excel(file_path)
df.dropna(inplace=True)
