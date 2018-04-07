# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:20:26 2018

@author: Nan
"""

import pandas as pd 
import matplotlib.pyplot as plt

class Client:
       
    upload_Dataframe = pd.DataFrame()
    cleaned_Dataframe = pd.DataFrame()
    listOfFields = []
    listOfSelection = []
    filename = ''
    pointer='wait'
    output = ''
    
    # communication module which acquires input orders
    def comm_module(self):
        self.output = 'Welcome to the Tender database visulisation system!' 
           
            # actually use the local file to make DA
         
    # comm_pointer
    def comm_pointer(self,index=0):   
        if index == 1:
            self.pointer = 'Quit'
        elif index == 2:
            self.pointer = 'upload file'
        elif index == 3:
            self.pointer = 'fields selection'
        elif index == 0:
            self.pointer = 'wait'
        
    
    # Upload function
    def upload_file(self,upload_file):
        while True:
            try:              
                # save the dataframe into upload_Dataframe
                self.upload_Dataframe = pd.read_csv(upload_file,low_memory=False)
                self.listOfFields = list(self.upload_Dataframe) # extract the list of header of dataframe
                self.data_cleansing()
                self.output = 'Pass'     # if successfully read the csv, give the Pass output to ui
            except FileNotFoundError:
                self.output = "File Not Found!"
            except SyntaxError:
                self.output = "SntaxError, file path should be C:/Users/data.csv"
            break
    
    # data cleansing
    def data_cleansing(self):
        df = self.upload_Dataframe
        # searching for missing values in columns
        nan_col_any = df.isnull().any() # for any column that includes Nan
        nan_col_all = df.isnull().all() # for any column that all value is Nan
        # extract the list of Nan included columns
        nan_features_any = pd.Series(list(nan_col_any[nan_col_any==True].index))
        # eatract the list of all Nan columns
        nan_features_all = pd.Series(list(nan_col_all[nan_col_all==True].index))
        # if exist entire Nan values columns
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
            self.cleaned_Dataframe = df
    
    # Fields selection fuction  *************Not Finished Yet***************
    def fields_selection(self,questions=0): # value of quest indicates the list of fields that required by corresponding question
        # based on the question, distribute corresponding index to each question
        if questions == 0:
            self.listOfSelection = ['Agency Name']
        elif questions == 1:  # How much funding is available in the target categories? (Total, by category, over time)
            self.listOfSelection = ['Value','UNSPSC Title']
        else:
            self.listOfSelection = []
            
    # visualisation quesiton, use bar chart to represent the Tender funding by category of interest
    # bsed ont the UNSPSC code & Title
    def visual_quest1(self,listOfSelection):
        # get a new dataframe based on the selected features
        df1 = self.upload_Dataframe.loc[:,listOfSelection]
        # extrac unique value of 'UNSPSC Titile'
        listOfCategory = df1.loc[:,'UNSPSC Title'].unique()  # len(listOfCategory) is longer than sumByCat, nan(float type) is included
        # create a new empty dataframe
        new_pd = pd.DataFrame(columns=listOfSelection)
        
        for cat in listOfCategory:
            # calculate the sum value by unique 'UNSPSC Title'
            sumByCat = df1.groupby('UNSPSC Title')['Value'].sum()[cat]
            # create a Serise with column = ['UNSPSC Title','Value']
            df_sumByCat = pd.DataFrame([[sumByCat,cat]],columns=listOfSelection)
            #update new_pd which saves the sum of value by title
            new_pd = new_pd.append(df_sumByCat)
            
        print(new_pd)
        
    
    # **********************************************************************

if __name__ == '__main__':
    c = Client()
    c.upload_file('C:\\Users\\Nan\\Desktop\\Qt Project\\project V2.3\\full_db.csv')
    print(c.listOfFields)
    c.fields_selection(1)
    c.visual_quest1(c.listOfSelection)
    