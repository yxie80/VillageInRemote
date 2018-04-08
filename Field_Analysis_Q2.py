from Client_Test03 import Client
import pandas as pd
import numpy as np
from Server import Server


def match_interest(input_df, match_with):
    input_df = pd.merge(input_df, match_with, how='left', left_on='UNSPSC Title', right_on='Filter UNSPSC of Interest')
    return input_df


client = Client()
server = Server()

client.upload_file('/Users/purple/Desktop/All CN.csv')

lof = client.listOfFields
df = client.upload_Dataframe
match_df = server.match_df
catByAgency = client.catByAgency

if 'Filter UNSPSC of Interest' not in lof:
    # updated file after add Category of Interest
    updated_data = match_interest(df, match_df)
# filter the dataframe to exclude the items not interested
updated_data.filter(like='Categories of Interest')


# input from client's keyboard, link to UI
catSelected = input('Enter the category of interest: ')

# show all the category
# for category in catByAgency.keys():
#     agency = client.category_agency(category)
#     funding = updated_data.loc[df['Agency Name'].isin(agency)]
#     # group by agency name and sort in descend order
#     top_funding = pd.pivot_table(funding, index='Agency Name', values='Value', aggfunc=np.sum) \
#         .sort_values(by='Value', ascending=False)
#     print(top_funding)


# return agency list under the category
agency = client.category_agency(catSelected.lower())
funding = updated_data.loc[df['Agency Name'].isin(agency)]
# group by agency name and sort in descend order
top_funding = pd.pivot_table(funding, index='Agency Name', values='Value', aggfunc=np.sum)\
    .sort_values(by='Value', ascending=False)
# return top_funding
print(top_funding)


