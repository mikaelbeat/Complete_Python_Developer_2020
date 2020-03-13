
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(res.text, "html.parser")

#print(soup.body)
#print(soup.find_all("div"))
#print(soup.title)
#print(soup.find(id="score_22561291"))
#print(soup.select(".score"))
#print(soup.select("#score_22564142"))


links = soup.select(".storylink")
subtext = soup.select(".subtext")
#print(votes[0])

def create_custom_list(links, subtext):
    data = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                data.append({"title": title, "link": href, "votes": points})
    return data


pprint.pprint(create_custom_list(links, subtext))

#create_custom_list(links, subtext)