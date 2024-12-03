# Election analysis app
# Allows the user to analyse the 2024 UK general election

# imports
import csv

# Lists to store my Constituency, MP and Party objects
Constituencies = []
MPs = []
Parties = []


# Classes

class Party:
    '''Party class'''
    def __init__(self,name):
        self.__Description = {'Name':name, 'Members':0,'Votes':0}
        
    def Set_TotalMembers(self):
        self.__Description['Members'] += 1
    def SetTotalVotes(self,votes):
        self.__Description['Votes'] += int(votes)
        
    @property   # Property Decorator allows me to Get, Set and delete atrribute values easily
    def Get_pName(self):
        return self.__Description['Name']
    
    @property
    def Get_pVotes(self):
        return self.__Description['Votes']
        
    def __str__(self):
        return f"{self.__Description['Name']}, 'has', {self.__Description['Members']}, 'Members and', {self.__Description['Votes']}, 'Total Votes'"

class Constituency:
    '''Constituency class'''
    def __init__(self,name,region,country,type):
        self.__cName = name
        self.__cRegion = region
        self.__cCountry = country
        self.__cType = type

    # Getters and Setters
    @property 
    def Get_cName(self):
        return self.__cName

    @property
    def Get_cRegion(self):
        return self.__cRegion

    @property
    def Get_cCountry(self):
        return self.__cCountry

    @property
    def Get_cType(self):
        return self.__cType

        
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

    # Getters and Setters
    
    @property
    def Get_mpFirstname(self):
        return self.__mpFirstname

    @property
    def Get_mpSurname(self):
        return self.__mpSurname

    @property
    def Get_mpGender(self):
        return self.__mpGender

    @property
    def Get_mpParty(self):
        return self.__mpParty

    @property
    def Get_mpElectorate(self):
        return self.__mpElectorate

    @property
    def Get_mpValidvotes(self):
        return self.__mpValidvotes
    
    @property
    def Get_mpInvalidvotes(self):
        return self.__mpInvalidvotes


def read_file():
    '''Reading CSV'''
    csvfile = open('FullDataFor2024.csv', 'r+')
    reader = csv.DictReader(csvfile)
    return reader
    csvfile.close()



def manage_data():
    csvfile = read_file()
    for row in csvfile:
        constituency = Constituency(name = row['Constituency name'],region=row['Region name'],country=row['Country name'],type=row['Constituency type'])
        mp = MP(firstname=row['Member first name'],surname=row['Member surname'],gender=row['Member gender'],party=row['First party'],electorate=int(row['Electorate'].replace(",", "")),validvotes=int(row['Valid votes'].replace(",", "")),invalidvotes=int(row['Invalid votes'].replace(",", "")))
        
        Constituencies.append(constituency)
        MPs.append(mp)
        
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

