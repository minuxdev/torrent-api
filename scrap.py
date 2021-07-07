from bs4 import BeautifulSoup
import requests


class Getting():
    def __init__(self, title):
        
        url = f"https://eztv.re/search/{title}"

        r = requests.get(url)

        bs = BeautifulSoup(r.content, "lxml")
        self.results = bs.findAll(class_="magnet")


    def Show(self):
        try:
            self.info = []
            self.magnets = []
            for link in self.results:
                self.info.append(link["title"][:-11])
                self.magnets.append(link["href"])
            
            return self.info, self.magnets
        except:
            return None
