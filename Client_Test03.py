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
    # 15 categories of interest by Agency
    catByAgency = {
        'comprehensive health services':["Attorney-General's Department", 'Australian Customs and Border Protection Service', 'Australian Electoral Commission', 'Australian Federal Police', 'Australian Prudential Regulation Authority (APRA)', 'Australian Sports Anti-Doping Authority (ASADA)', 'Australian Taxation Office', 'Cancer Australia', 'Comsuper', 'CRS Australia', 'CSIRO', 'Defence Materiel Organisation', 'Department of Agriculture and Water Resources', 'Department of Defence', 'Department of Finance', 'Department of Foreign Affairs and Trade - Australian Aid Program', 'Department of Health', 'Department of Human Services', 'Department of Immigration and Border Protection', 'Department of Infrastructure and Regional Development', 'Department of Infrastructure and Transport', 'Department of Parliamentary Services', 'Department of Regional Australia, Local Government, Arts and Sport', 'Department of the Treasury', "Department of Veterans' Affairs", 'National Blood Authority', 'National Water Commission', 'Office of the Fair Work Building Industry Inspectorate', 'Professional Services Review', 'Royal Australian Mint'],
        'community and social services':['Department of Social Services', 'Department of Immigration and Border Protection', 'Department of Foreign Affairs and Trade - Australian Aid Program', 'Department of Education Employment and Workplace Relations', 'Department of the Prime Minister and Cabinet', 'Department of Human Services', 'Department of Defence', "Department of Veterans' Affairs", 'Department of Regional Australia, Local Government, Arts and Sport', 'Department of Communications and the Arts', "Attorney-General's Department", 'Department of Infrastructure and Regional Development', 'Department of Education and Training', 'Department of Employment', 'Australian Human Rights Commission', 'Department of Health', 'Australian Communications and Media Authority (ACMA)', 'Department of Families, Housing, Community Services and Indigenous Affairs', 'Murray-Darling Basin Authority', 'Australian Electoral Commission', 'Australian Federal Police', 'Office of the Fair Work Ombudsman', 'Department of Agriculture and Water Resources'],
        'healthcare provider support persons':['Department of Immigration and Border Protection', "Department of Veterans' Affairs", 'Department of Defence', 'Australian Taxation Office', 'Department of the Prime Minister and Cabinet', 'Australian Federal Police', 'Department of Parliamentary Services', 'Department of Infrastructure and Regional Development', 'Australian Organ and Tissue Donation and Transplantation Authority', 'Australian Communications and Media Authority (ACMA)', 'Cancer Australia', 'Australian Radiation Protection and Nuclear Safety Agency (ARPANSA)'],
        'health programs':['Department of Health', 'Department of the Prime Minister and Cabinet', "Department of Veterans' Affairs", 'Cancer Australia', 'National Health Performance Authority', 'Department of Foreign Affairs and Trade - Australian Aid Program', 'Department of Industry, Innovation and Science', 'Independent Hospital Pricing Authority', 'Department of Families, Housing, Community Services and Indigenous Affairs', 'Department of Agriculture and Water Resources', 'Department of Human Services', 'Department of Defence', 'Australian Bureau of Statistics', 'Australian Communications and Media Authority (ACMA)', 'Australian Radiation Protection and Nuclear Safety Agency (ARPANSA)', 'Department of Foreign Affairs and Trade', 'Department of Infrastructure and Regional Development', 'Department of the Environment', 'Australian National Preventive Health Agency', 'Defence Materiel Organisation', 'Old Parliament House', 'Department of Regional Australia, Local Government, Arts and Sport', 'Department of Parliamentary Services'],
        'research programs':['Australian Centre for International Agricultural Research', 'Department of Social Services', 'Department of Education and Training', 'Department of Education Employment and Workplace Relations', 'Department of Defence', 'Australian Research Council', "Department of Veterans' Affairs", 'Australian Fisheries Management Authority', 'Department of Immigration and Border Protection', "Attorney-General's Department", 'Department of Employment', 'Australian Institute of Family Studies', 'Safe Work Australia', 'Great Barrier Reef Marine Park Authority', 'Defence Materiel Organisation', 'National Health and Medical Research Council', 'National Mental Health Commission', 'Department of Industry, Innovation and Science', 'Fair Work Commission', 'Department of the Environment', 'Department of Families, Housing, Community Services and Indigenous Affairs', 'Australian Institute of Criminology', 'Department of Foreign Affairs and Trade', 'Department of Climate Change and Energy Efficiency', 'Australian Securities and Investments Commission', 'Asbestos Safety and Eradication Agency', 'Bureau of Meteorology', 'Department of Human Services', 'Geoscience Australia', 'Department of Agriculture and Water Resources', 'Department of the Prime Minister and Cabinet', 'Australian Federal Police', 'Australian Taxation Office', 'Australian Organ and Tissue Donation and Transplantation Authority', 'Australian National Preventive Health Agency', 'Australian War Memorial', 'Australian Human Rights Commission', 'Australian Institute of Health and Welfare', 'Department of Resources Energy and Tourism', 'Office of the Fair Work Ombudsman', 'Old Parliament House', 'Australian Communications and Media Authority (ACMA)', 'Austrade', 'Workplace Gender Equality Agency', 'Department of Finance', 'Australian Bureau of Statistics', 'Australian Aged Care Quality Agency', 'Clean Energy Regulator', 'Digital Transformation Office', 'Office of Parliamentary Counsel', 'Productivity Commission', 'Department of Regional Australia, Local Government, Arts and Sport', 'Office of the Australian Information Commissioner', 'Australian Prudential Regulation Authority (APRA)', 'Office of the Australian Accounting Standards Board', 'National Capital Authority', 'Office of the Fair Work Building Industry Inspectorate', 'Inspector-General of Taxation', 'Australian Transaction Reports and Analysis Centre (AUSTRAC)', 'Department of Foreign Affairs and Trade - Australian Aid Program', 'Australian Electoral Commission', 'Murray-Darling Basin Authority', 'Cancer Australia'],
        'disease prevention and control':['Department of Health', 'Department of Foreign Affairs and Trade - Australian Aid Program', 'Department of Agriculture and Water Resources', 'Australian Centre for International Agricultural Research', 'Defence Materiel Organisation', 'Department of Defence', 'Department of Communications and the Arts', 'Department of the Prime Minister and Cabinet', 'Department of Parliamentary Services', "Attorney-General's Department", 'Department of Education and Training', 'Department of Regional Australia, Local Government, Arts and Sport'],
        'health administration services':['Department of Defence', 'Australian Federal Police', 'Department of Human Services', "Department of Veterans' Affairs", 'Department of Foreign Affairs and Trade', 'Cancer Australia', "Attorney-General's Department", 'Department of Finance', 'Department of Immigration and Border Protection', 'Department of Health', 'Department of Industry, Innovation and Science', 'Australian National Preventive Health Agency', 'Defence Materiel Organisation', 'Professional Services Review', 'Department of Foreign Affairs and Trade - Australian Aid Program', 'Safe Work Australia', 'Department of Parliamentary Services', 'Department of Resources Energy and Tourism', 'National Health and Medical Research Council', 'Austrade', 'Department of Social Services', 'Australian Transaction Reports and Analysis Centre (AUSTRAC)', 'Department of Agriculture and Water Resources'],
        'market research':['Austrade', 'Department of Health', 'Department of Human Services', 'Australian Taxation Office', 'Department of Communications and the Arts', 'Department of Defence', 'Department of Industry, Innovation and Science', 'Department of Social Services', 'Department of Finance', 'Australian National Preventive Health Agency', 'Australian Securities and Investments Commission', 'Department of the Environment', 'Department of Families, Housing, Community Services and Indigenous Affairs', 'Australian Communications and Media Authority (ACMA)', 'Department of Immigration and Border Protection', 'Tourism Australia', "Attorney-General's Department", 'Australian Institute of Health and Welfare', 'Australian Electoral Commission', 'Department of the Treasury', 'Independent Hospital Pricing Authority', 'Department of Foreign Affairs and Trade', 'Australian Centre for International Agricultural Research', 'Department of Resources Energy and Tourism', "Department of Veterans' Affairs", 'Department of Infrastructure and Regional Development', 'Digital Transformation Office', 'Australian Bureau of Statistics', 'Department of Agriculture and Water Resources', 'Department of Employment', 'Australian Organ and Tissue Donation and Transplantation Authority', 'Clean Energy Regulator', 'Australian Competition and Consumer Commission', 'Department of Climate Change and Energy Efficiency', 'Defence Materiel Organisation', 'Department of Education and Training', 'Australian Federal Police', 'Australian Public Service Commission', 'Department of Regional Australia, Local Government, Arts and Sport', 'Department of Infrastructure and Transport', 'Bureau of Meteorology', 'Department of Education Employment and Workplace Relations', 'Australian Human Rights Commission', 'Office of the Fair Work Ombudsman', 'Australian Financial Security Authority', 'Department of Health - Therapeutic Goods Administration', 'IP Australia', 'Cancer Australia', 'Great Barrier Reef Marine Park Authority', 'Australian Sports Anti-Doping Authority (ASADA)', 'Comsuper', 'Australian National Audit Office (ANAO)', 'Old Parliament House', 'Australian Pesticides and Veterinary Medicines Authority', 'Workplace Gender Equality Agency', 'Department of the Prime Minister and Cabinet', 'Australian Criminal Intelligence Commission', 'Director of National Parks', 'Geoscience Australia', 'Australian Skills Quality Authority', 'Department of Foreign Affairs and Trade - Australian Aid Program', 'Murray-Darling Basin Authority', 'National Mental Health Commission', 'Australian Radiation Protection and Nuclear Safety Agency (ARPANSA)', 'Department of Parliamentary Services', 'National Capital Authority', 'Telecommunications Universal Service Management Agency', 'Office of National Assessments', 'Australian Research Council', 'Safe Work Australia', 'Private Health Insurance Ombudsman', 'National Archives of Australia', 'Federal Court of Australia', 'Australian Transport Safety Bureau', 'Fair Work Commission', 'Office of the Fair Work Building Industry Inspectorate'],
        'military science and research':['Department of Defence', 'Defence Materiel Organisation', "Department of Veterans' Affairs"],
        'safety or risk analysis':['Department of Defence', 'Department of Agriculture and Water Resources', 'Defence Materiel Organisation', 'Department of Health', 'Department of the Environment', 'Department of Immigration and Border Protection', 'Clean Energy Regulator', "Attorney-General's Department", 'Department of Finance', 'Australian Competition and Consumer Commission', 'Office of the Director of Public Prosecutions', 'Department of Foreign Affairs and Trade', 'Department of Industry, Innovation and Science', 'Department of Families, Housing, Community Services and Indigenous Affairs', 'Department of the Prime Minister and Cabinet', 'Department of Infrastructure and Transport', 'Australian Federal Police', "Department of Veterans' Affairs", 'Australian Customs and Border Protection Service', 'Department of Infrastructure and Regional Development', 'Safe Work Australia', 'Australian Securities and Investments Commission', 'Australian Fisheries Management Authority', 'Department of Parliamentary Services', 'Geoscience Australia', 'Department of Health - Therapeutic Goods Administration', 'Department of Communications and the Arts', 'Department of Education Employment and Workplace Relations', 'Australian Radiation Protection and Nuclear Safety Agency (ARPANSA)', 'Administrative Appeals Tribunal', 'Royal Australian Mint', 'Office of the Fair Work Building Industry Inspectorate', 'National Offshore Petroleum Safety and Environmental Management Authority', 'Office of the Fair Work Ombudsman', 'Australian Bureau of Statistics', 'Austrade', 'Office of the Official Secretary to the Governor-General', 'Australian Institute of Family Studies'],
        'economics':['Department of Infrastructure and Regional Development', 'Department of Infrastructure and Transport', 'Department of Foreign Affairs and Trade - Australian Aid Program', 'Department of the Treasury', 'Department of Defence', 'Department of Foreign Affairs and Trade', 'Department of Communications and the Arts', 'Department of Infrastructure Transport Regional Development and Local Government', 'Productivity Commission', 'Department of the Environment', 'Department of the Prime Minister and Cabinet', 'Department of Industry, Innovation and Science', 'Department of Immigration and Border Protection', 'Department of Agriculture and Water Resources'],
        'medical science research and experimentation':["Department of Veterans' Affairs", 'Australian Federal Police', 'Department of Defence', 'Department of Health', 'Defence Materiel Organisation', 'Department of Social Services', 'Department of Health - Therapeutic Goods Administration', 'Australian Pesticides and Veterinary Medicines Authority', 'Department of Foreign Affairs and Trade - Australian Aid Program', 'Australian Sports Anti-Doping Authority (ASADA)', 'Australian Radiation Protection and Nuclear Safety Agency (ARPANSA)', 'Australian Securities and Investments Commission'],
        'economic analysis':['Australian Office of Financial Management', 'Department of Climate Change and Energy Efficiency', 'Department of Industry, Innovation and Science', 'Department of Health', 'Department of Social Services', 'Climate Change Authority', 'Department of the Environment', 'Department of Foreign Affairs and Trade', 'Department of Communications and the Arts', "Attorney-General's Department", 'Department of Education Employment and Workplace Relations', 'Department of the Treasury', 'Department of Defence', 'Department of Resources Energy and Tourism', 'Department of the Prime Minister and Cabinet', 'Defence Materiel Organisation', 'Department of Infrastructure and Transport', 'Department of Infrastructure and Regional Development', 'National Capital Authority', 'Australian Organ and Tissue Donation and Transplantation Authority', 'Australian Communications and Media Authority (ACMA)', 'Cancer Australia', 'Australian Centre for International Agricultural Research', 'Safe Work Australia', 'Great Barrier Reef Marine Park Authority', 'Department of Health - Therapeutic Goods Administration', 'Commonwealth Grants Commission', 'Department of Immigration and Border Protection', 'Department of Parliamentary Services', 'Australian Fisheries Management Authority', 'Geoscience Australia', 'Department of Foreign Affairs and Trade - Australian Aid Program', 'Productivity Commission', 'Australian Human Rights Commission', 'Department of Education and Training', 'Department of Families, Housing, Community Services and Indigenous Affairs', 'Department of Employment', 'Office of National Assessments', 'Parliamentary Budget Office'],
        'statistics':['Department of Education Employment and Workplace Relations', "Attorney-General's Department", 'Department of Immigration and Border Protection', 'Department of Defence', 'Department of Education and Training', "Department of Veterans' Affairs", 'Department of Foreign Affairs and Trade - Australian Aid Program', 'National Health Performance Authority', 'Australian Bureau of Statistics', 'Department of Infrastructure and Regional Development', 'Department of Regional Australia, Local Government, Arts and Sport', 'Department of Infrastructure and Transport', 'Department of the Environment - Australian Antarctic Division', 'Department of Communications and the Arts', 'Department of Industry, Innovation and Science', 'Department of the Environment', 'Bureau of Meteorology', 'Tertiary Education Quality and Standards Agency', 'Department of Agriculture and Water Resources', 'Clean Energy Regulator', 'Australian Competition and Consumer Commission', 'Department of the Treasury', 'Department of Infrastructure Transport Regional Development and Local Government', 'Australian Electoral Commission', 'Department of Resources Energy and Tourism', 'Department of Social Services', 'Australian National Preventive Health Agency', 'Department of the Prime Minister and Cabinet', 'Department of Foreign Affairs and Trade', 'Australian Communications and Media Authority (ACMA)', 'Department of Families, Housing, Community Services and Indigenous Affairs', 'Commonwealth Grants Commission', 'Defence Materiel Organisation', 'National Health and Medical Research Council', 'Department of Employment'],
        'drug abuse prevention or control programs':['Department of Defence', 'Australian Federal Police', 'Department of Families, Housing, Community Services and Indigenous Affairs', 'Australian Criminal Intelligence Commission', 'Department of Immigration and Border Protection']
    }
    
    # communication module which acquires input orders
    def comm_module(self):
        self.output = 'Welcome to the Tender database visualisation system!'
           
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
                self.output = "SyntaxError, file path should be C:/Users/data.csv"
            break
    
    # data cleansing -- handling missing value
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
#                        print(df.loc[list_of_nan[index],[features,'UNSPSC Code']])
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
    
    # # Fields selection function  *************Not Finished Yet***************
    # value of quest indicates the list of fields that required by corresponding question
    def fields_selection(self,questions=0):
        # based on the question, distribute corresponding index to each question
        if questions == 0:
            self.listOfSelection = ['Agency Name']
        elif questions == 1:  # How much funding is available in the target categories? (Total, by category, over time)
            self.listOfSelection = ['Value','UNSPSC Title']
        elif questions == 2: # question 2
            self.listOfSelection = []
        else:
            self.listOfSelection = []
            
    # visualisation quesiton, use bar chart to represent the Tender funding by category of interest
    # based on the UNSPSC code & Title
    def visual_quest1(self,listOfSelection):
        # get a new dataframe based on the selected features
        df1 = self.upload_Dataframe.loc[:,listOfSelection]
        # extrac unique value of 'UNSPSC Titile'
        listOfCategory = df1.loc[:,'UNSPSC Title'].unique()
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

    # Return the list of agency name with target category
    def category_agency(self, category_name):
        listAgency = self.catByAgency.get(category_name)
        return listAgency
    # **********************************************************************

if __name__ == '__main__':
    c = Client()
    c.upload_file('/Users/NAN/Desktop/All_data.csv')
#    print(c.listOfFields)
#    c.fields_selection(1)
#    print(c.cleaned_Dataframe.isnull().any())
    