from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://lpl.qq.com/index.shtml')
sleep(1)

soup = BeautifulSoup(driver.page_source, 'lxml')
container = soup.find(id='LPL_R_S_top_swiper_container')
ul = container.find('ul', class_='swiper-wrapper')
game_lists = ul.find_all('li')

for li in game_lists:
    team_a = li.find(class_='gamelist-team-a').a.string
    team_b = li.find(class_='gamelist-team-b').a.string
    score = li.find(class_='gamelist-score').find_all('a')
    score_a = int(score[0].string)
    score_b = int(score[2].string)
    print(team_a, score_a, ':', score_b, team_b)

driver.quit()
