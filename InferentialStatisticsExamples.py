# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:08:23 2021

@author: Administrator
"""

#Samples from  https://www.datavedas.com/inferential-statistics-in-python/

folder = "Data Sets"

## ---(Mon Nov  8 13:12:18 2021)---
import numpy as np
from numpy import random
import pandas as pd
from statsmodels.stats.weightstats import ztest
import scipy.stats as stats

#Read in student scores
Z_ScoresData = pd.read_excel(r"Data Sets/Marks_Scored.xlsx")
print(Z_ScoresData)
input()

#Create z-scores
Z_ScoresData['Score_ZScore'] = (Z_ScoresData['Score'] - Z_ScoresData['Score'].mean())/Z_ScoresData['Score'].std(ddof=0)
print(Z_ScoresData)
input()

#Generate some fake height values as a population, saving to Excel format
x = np.random.normal(loc=70, scale=3, size=200)
df = pd.DataFrame(x)
df.columns = ['Height']
df.to_excel(r"Data Sets/heights_pop.xlsx")

#Take a random sample of population heights data, saving to Excel format
df2 = df.sample(n=50)
df2.to_excel(r"Data Sets/heights_sample.xlsx")

#Get height population and sample into separate dataframes
HeightDataPop = pd.read_excel(r"Data Sets/heights_pop.xlsx")
HeightDataSample = pd.read_excel(r"Data Sets/heights_sample.xlsx")

#Perform Ztest
MeanPop = HeightDataPop['Height'].mean()
MeanSample = HeightDataSample['Height'].mean()
MeanPopFmt = "{:0.4f}".format(MeanPop)
MeanSampleFmt = "{:0.4f}".format(MeanSample)
print("MeanPop = " + MeanPopFmt + ", MeanSample = " + MeanSampleFmt)
X2 = np.array(HeightDataPop['Height'])
Y2 = np.array(HeightDataSample['Height'])
zVal_pVal = ztest(Y2,x2=None,value=MeanPop)
print(zVal_pVal)

#Perform One-Sample Ttest
DiamondData = pd.read_excel(r"Data Sets/DiamondData.xlsx")
DiamondData['WEIGHT'].mean()
output = stats.ttest_1samp(DiamondData['WEIGHT'],0.5)
print(output)

#Perform Independence TTest
AgeData = pd.read_csv(r"Data Sets/data1.csv")
Female_Age = AgeData[AgeData['gender'] == 'Female']['age']
Male_Age = AgeData[AgeData['gender'] == 'Male']['age']
Female_Age.mean()
#Out[21]: 55.57142857142857
Male_Age.mean()
#Out[22]: 54.0
output = stats.ttest_ind(a=Female_Age,b=Male_Age,equal_var=False)
#Out[23]: Ttest_indResult(statistic=0.43715320177431105, pvalue=0.6692391116588792)
print(output)

#Perform Paired T-test
ScoresData = pd.read_csv(r"Data Sets/Student Test Scores.csv")
before = ScoresData['Test A']
after = ScoresData['Test B']
output = stats.ttest_rel(a = before, b= after)
print(output)
##Out[7]: Ttest_relResult(statistic=-6.970438606669267, pvalue=1.2167687282184405e-06)


