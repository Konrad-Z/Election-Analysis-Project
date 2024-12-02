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
        
    def __str__(self):
        return f"Constituency name: {self.__cName:<40}Region name: {self.__cRegion:<40}Country name: {self.__cCountry:<40}Constituency type: {self.__cType:<40}"

        
        
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
        self.__mpDetails = {'First name': self.__mpFirstname,'Surname': self.__mpSurname,'Gender': self.__mpGender,'Party': self.__mpParty}

    def __str__(self):
        return 

    def GetMPDetails(self):
        return self.mpDetails

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

        

    def getTotalmps():
        return Party.__TotalMPs
    
    def setTotalmps(totalmps):
        Party.__TotalMPs = totalmps

    
    def __str__(self):
        return
    


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
    Parties = []
    totalmps = 0
    for row in csvfile:
        constituency = Constituency(name = row['Constituency name'],region=row['Region name'],country=row['Country name'],type=row['Constituency type'])
        mp = MP(firstname=row['Member first name'],surname=row['Member surname'],gender=row['Member gender'],party=row['First party'],electorate=int(row['Electorate'].replace(",", "")),validvotes=int(row['Valid votes'].replace(",", "")),invalidvotes=int(row['Invalid votes'].replace(",", "")))
        Constituencies.append(constituency)
        MPs.append(mp)
        
        totalmps += 1
    
    
        
    Party.setTotalmps(totalmps)

    TotalMPs = Party.getTotalmps()
    print(TotalMPs)
    

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

