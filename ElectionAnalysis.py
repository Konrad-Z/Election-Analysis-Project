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
    def Get_cName(self):
        return self.__cName

    @Get_cName.setter
    def Set_cName(self, value):
        self.__cName = value

    @property
    def Get_cRegion(self):
        return self.__cRegion

    @Get_cRegion.setter
    def Set_cRegion(self, value):
        self.__cRegion = value

    @property
    def Get_cCountry(self):
        return self.__cCountry

    @Get_cCountry.setter
    def Set_cCountry(self, value):
        self.__cCountry = value

    @property
    def Get_cType(self):
        return self.__cType

    @Get_cType.setter
    def Set_cType(self, value):
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
    def Get_mpFirstname(self):
        return self.__mpFirstname

    @Get_mpFirstname.setter
    def Set_mpFirstname(self, value):
        self.__mpFirstname = value

    @property
    def Get_mpSurname(self):
        return self.__mpSurname

    @Get_mpSurname.setter
    def Set_mpSurname(self, value):
        self.__mpSurname = value

    @property
    def Get_mpGender(self):
        return self.__mpGender

    @Get_mpGender.setter
    def Set_mpGender(self, value):
        self.__mpGender = value

    @property
    def Get_mpParty(self):
        return self.__mpParty

    @Get_mpParty.setter
    def Set_mpParty(self, value):
        self.__mpParty = value

    @property
    def Get_mpElectorate(self):
        return self.__mpElectorate

    @Get_mpElectorate.setter
    def Set_mpElectorate(self, value):
        self.__mpElectorate = value

    @property
    def Get_mpValidvotes(self):
        return self.__mpValidvotes

    @Get_mpValidvotes.setter
    def Set_mpValidvotes(self, value):
        self.__mpValidvotes = value

    @property
    def Get_mpInvalidvotes(self):
        return self.__mpInvalidvotes

    @Get_mpInvalidvotes.setter
    def Set_mpInvalidvotes(self, value):
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
    
    

    for c in Constituencies:
        if c.Get_cName == "Ashfield":
            print("Yes")

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

