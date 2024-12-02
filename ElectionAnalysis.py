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

    @property
    def _cName(self):
        return self.__cName

    @_cName.setter
    def _cName(self, value):
        self.__cName = value

    @property
    def _cRegion(self):
        return self.__cRegion

    @_cRegion.setter
    def _cRegion(self, value):
        self.__cRegion = value

    @property
    def _cCountry(self):
        return self.__cCountry

    @_cCountry.setter
    def _cCountry(self, value):
        self.__cCountry = value

    @property
    def _cType(self):
        return self.__cType

    @_cType.setter
    def _cType(self, value):
        self.__cType = value

        
    
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

    @property
    def _mpFirstname(self):
        return self.__mpFirstname

    @_mpFirstname.setter
    def _mpFirstname(self, value):
        self.__mpFirstname = value

    @property
    def _mpSurname(self):
        return self.__mpSurname

    @_mpSurname.setter
    def _mpSurname(self, value):
        self.__mpSurname = value

    @property
    def _mpGender(self):
        return self.__mpGender

    @_mpGender.setter
    def _mpGender(self, value):
        self.__mpGender = value

    @property
    def _mpParty(self):
        return self.__mpParty

    @_mpParty.setter
    def _mpParty(self, value):
        self.__mpParty = value

    @property
    def _mpElectorate(self):
        return self.__mpElectorate

    @_mpElectorate.setter
    def _mpElectorate(self, value):
        self.__mpElectorate = value

    @property
    def _mpValidvotes(self):
        return self.__mpValidvotes

    @_mpValidvotes.setter
    def _mpValidvotes(self, value):
        self.__mpValidvotes = value

    @property
    def _mpInvalidvotes(self):
        return self.__mpInvalidvotes

    @_mpInvalidvotes.setter
    def _mpInvalidvotes(self, value):
        self.__mpInvalidvotes = value


    

class Party:
    '''Party class'''
    __pTotalMPs = 0
    __pParties = []
    
    @property
    def _totalMPs():
        return Party.__pTotalMPs
    
    @_totalMPs.setter
    def _totalMPs(totalmps):
        Party.__pTotalMPs = totalmps 
    

    


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
    
    Party._totalMPs = totalmps

    print(Party._totalMPs)
    
    

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

