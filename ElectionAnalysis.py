# Election analysis app
# Allows the user to analyse the 2024 UK general election

# imports
import csv

# Lists to store my Constituency, MP and Party objects
Constituencies = []
MPs = []
Parties = []
PartyNames = [] # Temp List to get unique parties

# Classes

class Party:
    '''Party class'''
    def __init__(self,name):
        self.__pDescription = {'Name':name, 'Members':0,'Votes':0}
    
    def __str__(self):
        return f'Name: {self.__pDescription['Name']:<30} Members: {self.__pDescription['Members']:<30} Votes: {self.__pDescription['Votes']:<30}'
    
    # Methods to increment party members and party votes for the party (Setters)
    def IncrementMembers(self):
        self.__pDescription['Members'] += 1
    def IncrementTotalVotes(self,votes):
        self.__pDescription['Votes'] += int(votes)

    # Getters
    def Get_pName(self):
        return self.__pDescription['Name']
    def Get_pVotes(self):
        return self.__pDescription['Votes']
        
    

class MP:
    '''Member of Parliament class'''
    def __init__(self,firstname,surname,constituency,gender,party):   
        self.__mpFirstname = firstname
        self.__mpSurname = surname
        self.__mpConstituency = constituency
        self.__mpGender = gender
        self.__mpParty = party
        self.__mpDescription = {'Name': self.__mpFirstname + ' ' + self.__mpSurname, 'Constituency': self.__mpConstituency, 'Gender': self.__mpGender, 'Party': self.__mpParty, 'Votes': 0,'Electorate': 0, 'Majority':0}

    def __str__(self):
        return f'Name: {self.__mpDescription['Name']:<30} Gender: {self.__mpDescription['Gender']:<20} Constituency: {self.__mpDescription['Constituency']:<40} Party: {self.__mpDescription['Party']:<10} Votes: {self.__mpDescription['Votes']:<10} Electorate: {self.__mpDescription['Electorate']:<10} Majority: {self.__mpDescription['Majority']}'

    # Methods to set the voting data for the mp (Setters)
    def SetVotingData(self,electorate, votes,majority):
        self.__mpDescription['Electorate'] = int(electorate)
        self.__mpDescription['Votes'] = int(votes)
        self.__mpDescription['Majority'] = int(majority)
        
    # Getters 
    def Get_mpFirstname(self):
        return self.__mpFirstname
    def Get_mpSurname(self):
        return self.__mpSurname
    def Get_mpConstituency(self):
        return self.__mpConstituency
    def Get_mpGender(self):
        return self.__mpGender
    def Get_mpParty(self):
        return self.__mpParty
    def Get_mpVotes(self):
        return self.__mpDescription['Votes']
    def Get_mpElectorate(self):
        return self.__mpDescription['Electorate']
    
        
    
class Constituency:
    '''Constituency class'''
    def __init__(self,name,region,country,type):
        self.__cName = name
        self.__cRegion = region
        self.__cCountry = country
        self.__cType = type
        self.__cDescription = {'Name': self.__cName, 'Region': self.__cRegion,'Country':self.__cCountry,'Type': self.__cType}
        
    def __str__(self):
        return f'Constituency name: {self.__cDescription['Name']:<50} Region: {self.__cDescription['Region']:<50} Country: {self.__cDescription['Country']:50} Type: {self.__cDescription['Type']:<50}'
    
    # Getters
    def Get_cName(self):
        return self.__cName
    def Get_cRegion(self):
        return self.__cRegion
    def Get_cCountry(self):
        return self.__cCountry
    def Get_cType(self):
        return self.__cType

# Function for Reading the csv file
def read_file(): 
    '''Reading CSV'''
    csvfile = open('FullDataFor2024.csv', 'r+')
    reader = csv.DictReader(csvfile)
    return reader
    csvfile.close()

# Function for importing all the data from the csv into my classes as objects
def manage_data():
    csvfile = read_file()
    for row in csvfile:
        
        party = row['First party']
        
        # Setting MP information
        mpObject = MP(firstname=row['Member first name'],surname=row['Member surname'],gender=row['Member gender'],constituency=row['Constituency name'],party=row['First party'])
        constituency = Constituency(name = row['Constituency name'],region=row['Region name'],country=row['Country name'],type=row['Constituency type'])
        if party == 'Ind' or party == 'TUV' or party == 'Spk':
            mpObject.SetVotingData(row['Electorate'],row['Of which other winner'],row['Majority'])
        else:
            mpObject.SetVotingData(row['Electorate'],row[party],row['Majority'])
        MPs.append(mpObject)
        Constituencies.append(constituency)

        if party not in PartyNames:
            thisParty = Party(party)
            thisParty.IncrementMembers()
            thisParty.IncrementTotalVotes(mpObject.Get_mpVotes())
            PartyNames.append(party)
            Parties.append(thisParty)
        else:
            for p in Parties:
                if p.Get_pName() == party:
                    p.IncrementMembers()
                    p.IncrementTotalVotes(mpObject.Get_mpVotes())
    
manage_data()



MainOptions = ['List MP information', 'List the constituencies', 'List the Parties']

# Main Menu

print('\nWelcome to the 2024 General Election Analysis App')
print('Choose your option - Use the number')
print('#\t Option')

optionNumber = 0
for option in MainOptions:
    print(optionNumber, '\t', option)
    optionNumber += 1

UserInput = int(input('\nEnter your choice: '))

if UserInput == 0:
    for mp in MPs:
        print(mp)
elif UserInput == 1:
    for constituency in Constituencies:
        print(constituency)
elif UserInput == 2:
    for party in Parties:
        print(party)