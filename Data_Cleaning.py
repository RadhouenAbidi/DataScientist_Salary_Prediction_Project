# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:12:00 2020

@author: Radhouen
"""

import pandas as pd 
df=pd.read_csv("C:/Users/Radhouen/Documents/GitHub/DataScientist_Salary_Prediction_Project/Glassdoor_Jobs_Srapped.csv")

#Parsing the salaries

df['hourly']=df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided']=df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary: ' in x.lower() else 0)

df=df[df['Salary Estimate'] != '-1']

salary=df['Salary Estimate'].apply(lambda x: x.split('(')[0])

minus_kd=salary.apply(lambda x: x.replace('K','').replace('$',''))
minus_hr=minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary']=minus_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary']=minus_hr.apply(lambda x: int(x.split('-')[1]))
df['min_salary'].dtype
df['avg_salary']=(df.min_salary+df.max_salary)/2
#Comapany''s name 
df['Company_name_cleaned']=df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)
 
#State Field 

df['Job_State']=df['Location'].apply(lambda x: x.split(',')[1])
df['Job_State'].value_counts()
df.Job_State.value_counts()

df['same_state']=df.apply(lambda x: 1 if x.Location==x.Headquarters else 0 ,axis=1)

#Company's age 

df['Company_Age']=df.Founded.apply(lambda x: x if x<1 else 2020-x)

#Parsing the job description by soft skills 

df['Python']=df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['Excel']=df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['Aws']=df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['R_studio']=df['Job Description'].apply(lambda x: 1 if 'r studio' or 'r-studio' in x.lower() else 0)
df['Spark']=df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

df.Python.value_counts()
df.Spark.value_counts()
df.Aws.value_counts()
df.Excel.value_counts()
df.R_studio.value_counts()

df_cleaned=df.drop(['Unnamed: 0'],axis=1)
df_cleaned.to_csv('Cleaned_DataFrame.csv',index=False)


