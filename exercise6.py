# Exercise6 - training.
from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.nytimes.com")
data = r.text
soup = BeautifulSoup(data,'html.parser')

# old way - good if we want to search in specific tags (h2 for example)
#for link in soup.findAll(True, {"class": "story-heading"}):
#    print link.get_text()

# proper way - to search in the entire page
for link in soup.find_all(class_='story-heading'):
    print link.get_text().strip()


