# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:04:28 2020

@author: Radhouen
"""


import Glassdoor_Scraper as gs 
import pandas as pd 
path="C:/Users/Radhouen/Documents/GitHub/DataScientist_Salary_Prediction_Project/chromedriver.exe"

df=gs.get_jobs('data scientist', 1000, False, path, 20)


df2=pd.read_csv("C:/Users/Radhouen/Documents/GitHub/DataScientist_Salary_Prediction_Project/Glassdoor_Jobs_Srapped.csv")

pd.DataFrame(df2)