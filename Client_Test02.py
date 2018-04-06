# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:20:26 2018

@author: Nan
"""

import pandas as pd 

class Client:
       
    upload_Dataframe = pd.DataFrame()
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
                self.upload_Dataframe = pd.read_csv(upload_file,low_memory=False)
                self.listOfFields = list(self.upload_Dataframe)
                self.output = 'Pass'     
            except FileNotFoundError:
                self.output = "File Not Found!"
            except SyntaxError:
                self.output = "SntaxError, file path should be C:/Users/data.csv"
            break
                  
    
    # Fields selection fuction  *************Not Finished Yet***************
    def fields_selection(self,questions=0): # value of quest indicates the list of fields that required by corresponding question
        # based on the question, distribute corresponding index to each question
        if questions == 0:
            listOfSelection = ['Agency Name']
        elif questions == 1:  # How much funding is available in the target categories? (Total, by category, over time)
            listOfSelection = []
        else:
            listOfSelection = []
        return listOfSelection
    
    # **********************************************************************

if __name__ == '__main__':
    c = Client()
    c.upload_file('C:\\Users\\Nan\\Desktop\\Qt Project\\project V2.3\\full_db.csv')
    print(c.listOfFields)