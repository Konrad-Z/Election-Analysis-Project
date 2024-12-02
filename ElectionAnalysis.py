# Election analysis app
# Allows the user to analyse the 2024 UK general election

# imports
import csv

# Classes

class Constituency:
    '''Constituency class'''
    def __init__(self,name,region,country,type):
        self.__cName = name
        self.__cRegion = region
        self.__cCountry = country
        self.__cType = type
            
class MP:
    '''Member of Parliament class'''
    def __init__(self,firstname,surname,gender,party,electorate,validvotes,invalidvotes):   
        self.__mpFirstname = firstname
        self.__mpSurname = surname
        self.__mpGender = gender
        self.__mpParty = party
        self.__mpElectorate = electorate
        self.__mpValidvotes = validvotes
        self.__mpInvalidvotes = invalidvotes

class Party:
    '''Party class'''
    __TotalMPs = 0

    def __init__(self,party,NewMPs,totalelectorate,totalvalid,totalinvalid,propotion):
        self.__pParty = party
        self.__pNewMPs = NewMPs
        self.__pTotalelectorate = totalelectorate
        self.__pTotalvalid = totalvalid
        self.__pTotalinvalid = totalinvalid
        self.__pProportion = propotion

    


def read_file():
    '''Reading CSV'''
    csvfile = open('FullDataFor2024.csv', 'r+')
    reader = csv.DictReader(csvfile)
    return reader
    csvfile.close()


def manage_data():
    csvfile = read_file()
    Constituencies = []
    MPs = []
    totalmps = 0
    for row in csvfile:
        constituency = Constituency(name = row['Constituency name'],region=row['Region name'],country=row['Country name'],type=row['Constituency type'])
        mp = MP(firstname=row['Member first name'],surname=row['Member surname'],gender=row['Member gender'],party=row['First party'],electorate=int(row['Electorate'].replace(",", "")),validvotes=int(row['Valid votes'].replace(",", "")),invalidvotes=int(row['Invalid votes'].replace(",", "")))
        Constituencies.append(constituency)
        MPs.append(mp)
        
        totalmps += 1
    
    
        
    
    

manage_data()



MainOptions = ['List the MPs', 'List the constituencies', 'List the Parties']

# Main Menu

print('\nWelcome to the 2024 General Election Analysis App')
print('Choose your option - Use the number')
print('#\t Option')

optionNumber = 0
for option in MainOptions:
    print(optionNumber, '\t', option)
    optionNumber += 1

