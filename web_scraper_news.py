import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_news(news_counter=None):
    # URL = 'https://www.~~~.com'  #news website
    URL = 'https://www.bbc.com/news'
    page = requests.get(URL)
    

    soup = BeautifulSoup(page.text, 'html.parser')
    # soup = BeautifulSoup(page.text, 'lxml-xml')
    # soup = BeautifulSoup(page.text, 'html5lib')
    # soup = BeautifulSoup(page.text, 'lxml') 취사선택

    news_stories = soup.find_all('h3')  # headline

    news_no = 0
    # news_title = ''
    news_title_list = []
    news_tot = 50

    if news_counter != None:
        if int(news_counter) > 200:
            news_tot = 200
        else:
            # news_tot = news_counter
            news_tot = int(news_counter)
            
    for news_story in news_stories:
        if news_no != 0:
            # news_title += str(news_no) + ': ' + news_story.text.strip() + '\n\n'
            news_title_list.append({'news_no': news_no, 'newstitle':news_story.text.strip()})
            
        news_no += 1
        if news_no > news_tot:
            break
        
    news_df = pd.DataFrame(news_title_list)
    # return news_title
    return news_df
    


