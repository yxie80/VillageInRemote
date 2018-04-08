#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 08:20:49 2018

@author: NAN
"""
from Client_Test03 import Client

if __name__ == '__main__':
    c = Client()
    c.upload_file('/Users/NAN/Desktop/All_data.csv')
    c.fields_selection(1) # set question 1 required features
    
    # create new dataframe for question
    df = c.cleaned_Dataframe.loc[:,c.listOfSelection]
    
    # extract unique value of 'UNSPSC Title'
    listOfCategory = df.loc[:,'UNSPSC Title'].unique()
    

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
            