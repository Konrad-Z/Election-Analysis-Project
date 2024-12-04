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
        self.__Description = {'Name':name, 'Members':0,'Votes':0}
        
    def IncrementMembers(self):
        self.__Description['Members'] += 1
    def SetTotalVotes(self,votes):
        self.__Description['Votes'] += int(votes)
        
    # Property Decorator allows me to Get, Set and delete atrribute values easily
    def Get_pName(self):
        return self.__Description['Name']
    
    @property
    def Get_pVotes(self):
        return self.__Description['Votes']
        
    def __str__(self):
        return f"{self.__Description['Name']} has {self.__Description['Members']} Members and {self.__Description['Votes']} Total Votes'"


class MP:
    '''Member of Parliament class'''
    def __init__(self,firstname,surname,constituency,gender,party):   
        self.__mpFirstname = firstname
        self.__mpSurname = surname
        self.__mpConstituency = constituency
        self.__mpGender = gender
        self.__mpParty = party
        
        self.__description = {'Name': self.__mpFirstname + '' + self.__mpSurname, 'Constituency': self.__mpConstituency, 'Gender': self.__mpGender, 'Party': self.__mpParty, 'Votes': 0,'Electorate': 0,}
        
    # Getters and Setters
    
    def __str__(self):
        return self.__description

    # Setting Votes and electorate data
    def SetVotingData(self,electorate, votes):
        self.__description['Electorate'] = int(electorate)
        self.__description['Votes'] = int(votes)
        
    @property
    def Get_mpFirstname(self):
        return self.__mpFirstname

    @property
    def Get_mpSurname(self):
        return self.__mpSurname

    @property
    def Get_mpConstituency(self):
        return self.__mpConstituency
    
    @property
    def Get_mpGender(self):
        return self.__mpGender

    @property
    def Get_mpParty(self):
        return self.__mpParty

    @property
    def Get_Votes(self):
        return self.__description['Votes']
    
    @property
    def Get_InvalidVotes(self):
        return self.__description['Invalid Votes']
    
    @property
    def Get_Electorate(self):
        return self.__description['Electorate']
    

def read_file():
    '''Reading CSV'''
    csvfile = open('FullDataFor2024.csv', 'r+')
    reader = csv.DictReader(csvfile)
    return reader
    csvfile.close()


def manage_data():
    csvfile = read_file()
    for row in csvfile:
        
        party = row['First party']
        
        # Setting MP information
        mpObject = MP(firstname=row['Member first name'],surname=row['Member surname'],gender=row['Member gender'],constituency=row['Constituency name'],party=row['First party'])
        
        if party == 'Ind' or party == 'TUV' or party == 'Spk':
            mpObject.SetVotingData(row['Electorate'],row['Of which other winner'])
        else:
            mpObject.SetVotingData(row['Electorate'],row[party])
        MPs.append(mpObject)
        
        if party not in PartyNames:
            thisParty = Party(party)
            thisParty.IncrementMembers()
            thisParty.SetTotalVotes(mpObject.Get_Votes)
            PartyNames.append(party)
            Parties.append(thisParty)
        else:
            for p in Parties:
                if p.Get_pName() == party:
                    p.IncrementMembers()
                    p.SetTotalVotes(mpObject.Get_Votes)
    
manage_data()



MainOptions = ['List the MPs', 'List the constituencies', 'List the Parties']

# Main Menu

print('Welcome to the 2024 General Election Analysis App')
print('Choose your option - Use the number')
print('#\t Option')

optionNumber = 0
for option in MainOptions:
    print(optionNumber, '\t', option)
    optionNumber += 1

