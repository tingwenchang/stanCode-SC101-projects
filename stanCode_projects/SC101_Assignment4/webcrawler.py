"""
File: webcrawler.py
Name: Tingwen
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.tbody.find_all('tr')

        male = 0
        female = 0
        for tag in tags[:-1]:
            all = tag.text
            lists = all.split("\n")
            list = lists[1].split(" ")
            male_number = list[1].replace(",", "")
            male += int(male_number)
            female_number = list[3].replace(",", "")
            female += int(female_number)
        print(f'Male Number: {male}')
        print(f'Female Number: {female}')


if __name__ == '__main__':
    main()
