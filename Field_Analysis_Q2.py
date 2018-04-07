from Client_Test03 import Client

client = Client()
client.upload_file('/Users/purple/Desktop/All CN.csv')

lof = client.listOfFields
data = client.upload_Dataframe

# input from client's keyboard
catSelected = input('Enter the category of interest: ')

# return agency list under the category
agency = client.category_agency(catSelected.lower())

print(data)


