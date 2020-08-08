import django
import os
import sys
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

# 将项目根目录添加到 Python 的模块搜索路径中
back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def add_one_record(winner_name, loser_name, winner_score=2, loser_score=0):
    winner = Team.objects.get(name=winner_name)
    loser = Team.objects.get(name=loser_name)
    q = Record.objects.filter(winner=winner, loser=loser)
    if q:
        print('record exists!')
        return
    Record.objects.create(winner=winner, loser=loser, winner_score=winner_score, loser_score=loser_score)
    print(winner_name, winner_score, ':', loser_score, winner_name)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lpl_site.settings")
    django.setup()

    from record.models import Team, Record

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
        if score_a + score_b == 0:
            break
        if score_a < score_b:
            team_a, team_b, score_a, score_b = team_b, team_a, score_b, score_a
        add_one_record(team_a, team_b, score_a, score_b)

    driver.quit()
