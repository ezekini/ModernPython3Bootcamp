'''
In this project you'll be building a quotes guessing game. When run, your program will scrape a website for a collection of quotes. Pick one at random and display it. The player will have four chances to guess who said the quote. After every wrong guess they'll get a hint about the author's identity.
Requirements

Create a file called `scraping_project.py` which, when run, grabs data on every quote from the website http://quotes.toscrape.com

You can use `bs4` and `requests` to get the data. For each quote you should grab the text of the quote, the name of the person who said the quote, and the href of the link to the person's bio. Store all of this information in a list.

Next, display the quote to the user and ask who said it. The player will have four guesses remaining.

After each incorrect guess, the number of guesses remaining will decrement. If the player gets to zero guesses without identifying the author, the player loses and the game ends. If the player correctly identifies the author, the player wins!
After every incorrect guess, the player receives a hint about the author.
For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell the player the author's birth date and location.

The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the author's last name, the number of letters in one of the names, etc.

When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. If no, the program is complete.
'''
import os
import requests
from bs4 import BeautifulSoup
from csv import DictWriter
from random import choice

url_base = 'http://quotes.toscrape.com'
url = '/page/1'


def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def findData(quotes, alldata):
    alldata = []
    for block in quotes:
        quote = block.find(class_='text').get_text()
        author = block.find(class_='author').get_text()
        biourl = block.find('a')['href']
        getbio = scrape(url_base + biourl)
        bio_date = getbio.find(class_='author-born-date').get_text()
        bio_place = getbio.find(class_='author-born-location').get_text()
        alldata.append({
            'quote': quote, 'author': author, 'bio': bio_date + ' ' + bio_place
        })
        print(f'Scraping {url_base}{url}')
    return alldata


if not os.path.isfile('./quotes.csv'):

    while url:
        soup = scrape(f'{url_base}{url}')
        quotes = soup.find_all(class_="quote")
        data = findData(quotes, alldata)
        next_btn = soup.find(class_='next')
        url = next_btn.find('a')['href'] if next_btn else None
    with open('quotes.csv', 'w') as fp:
        headers = ['quote', 'author', 'bio']
        csv_writer = DictWriter(fp, fieldnames=headers)
        csv_writer.writeheader()
        for quote in alldata:
            csv_writer.writerow(quote)
else:
    print('Quotes have already been scraped')


quote = choice(alldata)
rem_guesses = 4

print('Here is a quote:')
print(quote['quote'])

while guess.lower() != quote['author'].lower() and rem_guesses <= 1:
    guess = input(f'who said this? Guesses remaining {rem_guesses}')
    rem_guesses -= 1
    quote = choice(alldata)
    print(quote['quote'])
