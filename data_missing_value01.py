#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 14:45:26 2018

@author: NAN
"""

import pandas as pd

df = pd.read_csv('/Users/NAN/Desktop/All_data.csv',low_memory=True)

# searching for NaN value
nan_all = df.isnull() # acquire all Nan value in dataframe，and return boolean type matrix

# searching for missing values in columns
nan_col_any = df.isnull().any() # for any column that includes Nan
nan_col_all = df.isnull().all() # for any column that all value is Nan
#print(nan_col_any)

# extract the list of Nan included columns
nan_features_any = pd.Series(list(nan_col_any[nan_col_any==True].index))
#print(nan_features_any)

# eatract the list of all Nan columns
nan_features_all = pd.Series(list(nan_col_all[nan_col_all==True].index))

# for entire Nan columns
if nan_features_all.empty != True:
    for each in nan_features_all:
        df.drop(each, axis=1, inplace=True) # delete entire column without reassign to df 

# for Nan value included columns, implement data cleansing(fillna method)
if nan_features_any.empty != True:
    for features in nan_features_any:
        if features == 'Parent Contract ID':
            df.loc[:,features] = df.loc[:,features].fillna('None')
        elif features == 'Amendment Date':
            df.loc[:,features] = df.loc[:,features].fillna('Not Amended')
        elif features == 'Description':
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Agency Ref ID':
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'UNSPSC Title': 
            list_of_nan = []
            for index in range(df.shape[0]):
                if type(df.loc[index,features]) != str:
                    list_of_nan.append(index) # acquire a list contain all index of Nan value in the Title column                  
            nan_UNSPSC_Code = []
            for each in list_of_nan:
                nan_UNSPSC_Code.append(df.loc[each,'UNSPSC Code'])
            nan_UNSPSC_Code = list(map(str,nan_UNSPSC_Code))    # get the corresponding value in UNSPSC Code            
            for index in range(len(list_of_nan)):
                # use UNSPSC ID to replace the Nan Value
                df.loc[list_of_nan[index],features] = nan_UNSPSC_Code[index]
                print(df.loc[list_of_nan[index],[features,'UNSPSC Code']])
        elif features == 'ATM ID':
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'SON ID':
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Panel Arrangement': # value str [Yes/No]
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Confidentiality Contract Flag':  # value str [No]
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Confidentiality Contract Reason': # value str
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Confidentiality Outputs Flag': # value str [No]
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Confidentiality Outputs Reason': # value str
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Consultancy Flag':  # value str [Yes/No]
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Consultancy Reason': # value str [ex:Skills currently unavailable within agency]
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Amendment Reason': # value str [ex:Contract value increased from $932,144.50]
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Supplier Address': # value str
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Supplier Suburb': # value str
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Supplier Postcode': # value str like numbers
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Supplier ABN': # value float [79097795125.0]
            df.loc[:,features] = df.loc[:,features].fillna(float(0)) # use 0.0 replace Nan in this field
        elif features == 'Contact Phone': # value str like num
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Branch': # value str
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Division':  # value str
            df.loc[:,features] = df.loc[:,features].fillna('N/A')
        elif features == 'Office Postcode': # vlaue str like numbers
            df.loc[:,features] = df.loc[:,features].fillna('N/A')            
            
#print(df.loc[:,'UNSPSC Title'].isnull().any())


        