from bs4 import BeautifulSoup
import requests
import re
import os


def url_to_string(url):
    res = requests.get(url)

    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))


ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
print(ny_bb)
with open(os.path.join("data", "random_text.txt"), "w", encoding="utf-8") as scraped_file:
    scraped_file.write(ny_bb)
