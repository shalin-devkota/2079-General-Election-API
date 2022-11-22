from bs4 import BeautifulSoup as soup
import requests



def get_election_json (pradesh,district:str,area):
    url = f"https://election.ekantipur.com/pradesh-{pradesh}/district-{district.lower()}?lng=eng"


    data_html = requests.get(url)
    data_soup = soup(data_html.text,"html.parser")

    main_election_class = data_soup.find('div',{"class":"election-2079"})
    election_const_data = main_election_class.findAll('div',{"class":'card-body'})

    election_data = election_const_data[area - 1]
    candidate_names = []
    parties = []
    votes = []
    election_json = {}
    candidate_name_list = election_data.findAll("div",{"class":"nominee-name"})
    for candidate in candidate_name_list:
        try:    
            candidate_names.append(candidate.a.contents[0])
        except AttributeError:
            pass

    candidate_party_list =election_data.findAll("div",{"class":"candidate-party-name"})
    i = 0
    for party in candidate_party_list:
        try:
            if i == 0:
                parties.append(party.a.contents[0].strip())
                i =  1
            else:
                i = 0
        except AttributeError:
            pass


    candidate_votes = election_data.findAll("div",{"class":"vote-count"})
    for vote in candidate_votes:
        try:
            votes.append(vote.text.strip())
        except AttributeError:
            pass

    temp_list = list(zip(parties,votes))
    
    election_json = dict(zip(candidate_names,temp_list))
    return election_json







