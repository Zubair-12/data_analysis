#import numpy of numerical python
import numpy as np
#import pandas for dealing with dataframe
import pandas as pd
#import seaborn and matplotlib for ploting the graphs
import seaborn as sns
import matplotlib.pyplot as plt
#setting the figure size to 12X9
sns.set(rc={'figure.figsize':(12,9)})

#create instance called dataset of type pandas dataframe from csv file
dataset=pd.read_csv("heart.csv")

#used head() method to create snapshot of first five rows of the dataset
dataset.head()

dataset.tail()

#how many rows and columns are there in dataframe
print("The data frame has {} rows and {} columns".format(dataset.shape[0],dataset.shape[1]))

dataset.dtypes

dataset.info()

dataset.apply(lambda x:sum(x.isnull()))

dataset.size

dataset['sex'].value_counts()

dataset['children'].value_counts()

#import warning to supress in out
import warnings
#supress warning 
warnings.filterwarnings('ignore')
#set plot style
sns.set(style="ticks")
#set x equals to column of our interest which is age here
x=dataset['age']
#create figure f, boxplot and histogram in single chart        
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, 
                                    gridspec_kw={"height_ratios": (.15, .85)})
#set input in boxplot
sns.boxplot(x, ax=ax_box)
#set input in histogram
sns.distplot(x, ax=ax_hist)
ax_box.set(yticks=[])
#plot the histogram
sns.despine(ax=ax_hist)
#plot the  boxplot 
sns.despine(ax=ax_box, left=True)

#import warning to supress in out
import warnings
#supress warning 
warnings.filterwarnings('ignore')
#set plot style
sns.set(style="ticks")
#set x equals to column of our interest which is BMI here
x=dataset['age']
#create figure f, boxplot and histogram in single chart        
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, 
                                    gridspec_kw={"height_ratios": (.15, .85)})
#set input in boxplot
sns.boxplot(x, ax=ax_box)
#set input in histogram
sns.distplot(x, ax=ax_hist)
ax_box.set(yticks=[])
#plot the histogram
sns.despine(ax=ax_hist)
#plot the  boxplot 
sns.despine(ax=ax_box, left=True)

#import warning to supress in out
import warnings
#supress warning 
warnings.filterwarnings('ignore')
#set plot style
sns.set(style="ticks")
#set x equals to column of our interest which is children here
x=dataset['children']
#create figure f, boxplot and histogram in single chart        
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, 
                                    gridspec_kw={"height_ratios": (.15, .85)})
#set input in boxplot
sns.boxplot(x, ax=ax_box)
#set input in histogram
sns.distplot(x, ax=ax_hist)
ax_box.set(yticks=[])
#plot the histogram
sns.despine(ax=ax_hist)
#plot the  boxplot 
sns.despine(ax=ax_box, left=True)
