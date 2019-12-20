import requests
from random import randint


url = "https://icanhazdadjoke.com/search"

user_in = input('Enter a keyword to search for a joke: ')

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_in}
)

data = response.json()
jokes_n = len(data["results"])



if jokes_n > 1:
    joke = data["results"][randint(1,jokes_n)]['joke']
    print(f'I have {jokes_n} about {user_in}. Here\'s one:')
    print(joke)
elif jokes_n == 1:
    print(f'I have {jokes_n} about {user_in}: ')
    joke = data["results"]['joke']
    print(joke)
else:
    print('There are no jokes with that keyword')
