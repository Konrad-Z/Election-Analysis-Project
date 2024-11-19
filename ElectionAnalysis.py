# Election analysis app
# Allows the user to analyse the 2024 UK general election

# imports
import csv

# Classes

class Constituency:
    '''Constituency class'''
    def __init__(self,name,region,country,type):
        self.cName = name
        self.cRegion = region
        self.cCountry = country
        self.cType = type
        self.description = {'Country name':self.cCountry,'Region name':self.cRegion,'Constituency Type':self.cType}
        
    def __str__(self):
        return self.cName
    def GetDescription(self):
        return self.description 
        
class MP:
    '''Member of Parliament class'''
    def __init__(self,firstname,surname,gender,party,electorate,validvotes,invalidvotes):   
        self.mpFirstname = firstname
        self.mpSurname = surname
        self.mpGender = gender
        self.mpParty = party
        self.mpElectorate = electorate
        self.mpValidvotes = validvotes
        self.mpInvalidvotes = invalidvotes
        self.mpDetails = {'First name': self.mpFirstname,'Surname': self.mpSurname,'Gender': self.mpGender,'Party': self.mpParty}

    def __str__(self):
        return 

    def GetMPDetails(self):
        return self.mpDetails

class Party:
    '''Party class'''
    def __init__(self,totalMPs,NewMPs,totalelectorate,totalvalid,totalinvalid,propotion):
        self.pTotalMPs = totalMPs
        self.pNewMPs = NewMPs
        self.pTotalelectorate = totalelectorate
        self.pTotalvalid = totalvalid
        self.pTotalinvalid = totalinvalid
        self.pProportion = propotion

        self.pDetails = {'Total MPs': self.pTotalMPs,'New MPs': self.pNewMPs,'Total Electorate':self.pTotalelectorate,'Total Valid':self.pTotalvalid,'Total Invalid':self.pTotalinvalid,'Proportion':self.pProportion}

    def __str__(self):
        return
    def GetPartyDetails(self):
        return self.pDetails


def read_file():
    '''Reading CSV'''
    csvfile = open('FullDataFor2024.csv', 'r+')
    reader = csv.DictReader(csvfile)
    return reader
    csvfile.close()

MainOptions = ['List the MPs', 'List the constituencies', 'List the Parties']

# Main Menu

print('\nWelcome to the 2024 General Election Analysis App')
print('Choose your option - Use the number')
print('#\t Option')

optionNumber = 0
for option in MainOptions:
    print(optionNumber, '\t', option)
    optionNumber += 1

