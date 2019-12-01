import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://liquipedia.net/leagueoflegends/LCS/2019/Spring/Group_Stage'

class LeagueScraper:
    def scrape(self):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        # DATE INFORMATION
        weeks = soup.select("table.matchlist > tbody > tr:not(.match-row)")
        home_team = soup.select("table.matchlist > tbody > tr[class=match-row] > td:nth-child(1)")
        away_team = soup.select("table.matchlist > tbody > tr[class=match-row] > td:nth-child(4)")
        home_team_score = soup.select("table.matchlist > tbody > tr[class=match-row] > td:not(.matchlistslot)")
        away_team_score = soup.select("table.matchlist > tbody > tr[class=match-row] > td:nth-child(3)")

        results = zip(home_team, away_team, home_team_score, away_team_score)

        for team in home_team_score:
            print(team.text)

        # for team in results:
        #     ht, at, hts, ats = team
        #     # print(ht.text)
        #     # print(at.text)
        #     print(hts.text)
            # print(ats.text)
        time.sleep(3)


scraper = LeagueScraper()
scraper.scrape()

