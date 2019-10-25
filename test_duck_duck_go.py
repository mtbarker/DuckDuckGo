import pytest
import requests

def presidents_names():
    ddg = 'https://duckduckgo.com/?q=presidents+of+the+united+states&format=json'
    response = requests.get(ddg)
    names_data = response.json()
#create list
    names_list = []
#pass names from data and append to names_list
    for i in names_data['RelatedTopics']:
        names_list.append(i['Text'])
    return names_list

def test_presidents_names():
#call names_list
    names_list = presidents_names()

    #presidents last names from https://www.whitehouse.gov/about-the-white-house/presidents/
    test_names = ["Washington", "Adams", "Jefferson",
                  "Madison", "Monroe", "Adams",
                  "Jackson", "Van Buren", "Harrison",
                  "Tyler", "Polk", "Taylor",
                  "Fillmore", "Pierce", "Buchanan",
                  "Lincoln", "Johnson", "Grant",
                  "Hayes", "Garfield", "Arthur",
                  "Cleveland", "Harrison", "Cleveland,"
                  "McKinley", "Roosevelt", "Taft",
                  "Wilson", "Harding", "Coolidge",
                  "Hoover", "Roosevelt", "Truman",
                  "Eisenhower", "Kennedy", "Johnson",
                  "Nixon", "Ford", "Carter",
                  "Reagan", "Bush", "Clinton",
                  "Bush", "Obama", "Trump"]

    str_name_list = str(names_list)
    found = True

    for name in test_names:
        if name in str_name_list == 0:
            found = False
    assert found == True






