"""
File: webcrawler.py
Name: David Lin
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
        soup = BeautifulSoup(html, features="html.parser")
        # ----- Write your code below this line ----- #
        sum_male = 0
        sum_female = 0
        ranks = soup.find_all('table', {'class': 't-stripe'})
        for tag in ranks:
            ele = str(tag.tbody.text)     # extract the text from t-stripe
            ele_lst = ele.split()       # split text into list
            for i in range(200):
                if 2+5*i < 1000:
                    m_num = (ele_lst[2+5*i]).replace(",", "")  # Male number
                    f_num = (ele_lst[4+5*i]).replace(",", "")   # Female number
                    sum_male += int(m_num)
                    sum_female += int(f_num)
            print("Male number: " + str(sum_male))
            print("FeMale number: " + str(sum_female))



if __name__ == '__main__':
    main()
