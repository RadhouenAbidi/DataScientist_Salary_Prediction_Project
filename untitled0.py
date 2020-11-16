# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:04:28 2020

@author: Radhouen
"""


import Glassdoor_Scraper as gs 
import pandas as pd 
path="C:/Users/Radhouen/Documents/DataScientist_Salary_Prediction_Project/chromedriver"

df=gs.get_jobs('data scientist', 15, False, path, 60)
