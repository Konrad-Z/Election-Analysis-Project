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
    def __init__(self,firstname,surname,constituency,gender,party,result):   
        self.__mpFirstname = firstname
        self.__mpSurname = surname
        self.__mpConstituency = constituency
        self.__mpGender = gender
        self.__mpParty = party
        self.__mpResult = result
        self.__mpDescription = {'Name': self.__mpFirstname + ' ' + self.__mpSurname, 'Constituency': self.__mpConstituency, 'Gender': self.__mpGender, 'Party': self.__mpParty,'Result': self.__mpResult, 'Votes': 0,'Electorate': 0, 'Majority':0, 'Valid Votes': 0, 'Percentage of Votes':0}

    def __str__(self):
        return f'Name: {self.__mpDescription['Name']:<30} Gender: {self.__mpDescription['Gender']:<20} Constituency: {self.__mpDescription['Constituency']:<40} Party: {self.__mpDescription['Party']:<10} Votes: {self.__mpDescription['Votes']:<10} Valid Total Votes cast: {self.__mpDescription['Valid Votes']:<10} Majority: {self.__mpDescription['Majority']:<10} % of Votes: {self.__mpDescription['Percentage of Votes']:.2f}'

    # Methods to set the voting data for the mp (Setters)
    def SetVotingData(self,electorate, votes,majority,validvotes):
        self.__mpDescription['Electorate'] = int(electorate)
        self.__mpDescription['Votes'] = int(votes)
        self.__mpDescription['Majority'] = int(majority)
        self.__mpDescription['Valid Votes'] = int(validvotes)
        self.__mpDescription['Percentage of Votes'] = (self.__mpDescription['Votes'] / self.__mpDescription['Valid Votes']) * 100
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
    def Get_mpDescription(self):
        return self.__mpDescription
        
    
class Constituency:
    '''Constituency class'''
    def __init__(self,name,region,country,type,electorate,mp,party):
        self.__cName = name
        self.__cRegion = region
        self.__cCountry = country
        self.__cType = type
        self.__cElectorate = electorate
        self.__cMP = mp
        self.__cParty = party
        self.__cDescription = {'Name': self.__cName, 'Region': self.__cRegion,'Country':self.__cCountry,'Type': self.__cType, 'Electorate': self.__cElectorate, 'Elected MP': self.__cMP, 'Elected Party': self.__cParty}
        
    def __str__(self):
        return f'Constituency name: {self.__cDescription['Name']:<40} Region: {self.__cDescription['Region']:<30} Country: {self.__cDescription['Country']:25} Type: {self.__cDescription['Type']:<20} Electorate: {self.__cDescription['Electorate']:<20} Elected MP: {self.__cDescription['Elected MP']:<25} Elected Party: {self.__cDescription['Elected Party']:<25}'
    
    # Getters
    def Get_cName(self):
        return self.__cName
    def Get_cRegion(self):
        return self.__cRegion
    def Get_cCountry(self):
        return self.__cCountry
    def Get_cType(self):
        return self.__cType
    def Get_cDescription(self):
        return self.__cDescription

# Function for Reading the csv file
def read_file(): 
    '''Reading CSV'''
    csvfile = open('FullDataFor2024.csv', 'r+')
    reader = csv.DictReader(csvfile)
    return reader


# Function for importing all the data from the csv into my classes as objects
def manage_data():
    csvfile = read_file()
    for row in csvfile:
        
        party = row['First party']
        
        # Setting MP information
        mpObject = MP(firstname=row['Member first name'],surname=row['Member surname'],gender=row['Member gender'],constituency=row['Constituency name'],party=row['First party'],result=row['Result'])
        constituency = Constituency(name = row['Constituency name'],region=row['Region name'],country=row['Country name'],type=row['Constituency type'],electorate=row['Electorate'],mp=row['Member first name'] + ' ' + row['Member surname'], party=row['First party'])
        if party == 'Ind' or party == 'TUV' or party == 'Spk':
            mpObject.SetVotingData(row['Electorate'],row['Of which other winner'],row['Majority'],row['Valid votes'])
        else:
            mpObject.SetVotingData(row['Electorate'],row[party],row['Majority'],row['Valid votes'])
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


def main():
    MainOptions = ['List MP information', 'List Constituency information', 'List Party information', 'List Results by constituency','Search','Display Unformatted CSV Data']
    SearchOptions = ['Search for a MP', 'Search for a Constituency', 'Search for a Party']
    # Main Menu

    print('\nWelcome to the 2024 General Election Analysis App')
    print('Choose your option - Use the number')
    print('#\t Option')

    optionNumber = 0
    searchNumber = 0
    for option in MainOptions:
        print(optionNumber, '\t', option)
        optionNumber += 1

    while True:
        try:
            UserInput = int(input('\nEnter your choice: '))
            break
        except:
            print('Value Must be Numeric')
            
      

    if UserInput == 0:
        for mp in MPs:
            print(mp)
    elif UserInput == 1:
        for constituency in Constituencies:
            print(constituency)
    elif UserInput == 2:
        for party in Parties:
            print(party)
    elif UserInput == 3:
        for mp in MPs:
            print(f'Constituency: {mp.Get_mpDescription()['Constituency']:<30} Result: {mp.Get_mpDescription()['Result']:<30} Elected: {mp.Get_mpDescription()['Name']:<30} Votes: {mp.Get_mpDescription()['Votes']:<30}')
    elif UserInput == 4:    
        for searchOption in SearchOptions:
            print(searchNumber ,'\t', searchOption)
            searchNumber += 1
        
        UserInput = int(input('\nEnter your choice: '))
        
        if UserInput == 0:
            UserSearch = input('Enter MP Name: ')
            for mp in MPs:
                if UserSearch in mp.Get_mpDescription()['Name']:
                    print(mp)
        elif UserInput == 1:
            UserSearch = input('Enter Constituency Name: ')
            for constituency in Constituencies:
                if UserSearch in constituency.Get_cDescription()['Name']:
                    print(constituency)
        elif UserInput == 2:
            UserSearch = input('Enter Party Name: ').title()
            for party in Parties:
                if UserSearch == party.Get_pName():
                    print(party)
                    UserInput = input('\nWould You like to display party members? (y/n)').lower()
                    if UserInput == 'y':
                        for mp in MPs:
                            if UserSearch == mp.Get_mpParty():
                                print(mp)
    elif UserInput == 5:    
        csvfile = read_file()
        for row in csvfile:
            print(row)
    
main()