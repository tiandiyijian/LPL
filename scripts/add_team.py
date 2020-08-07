import os
import pathlib
import random
import sys
from datetime import timedelta

import django
from django.utils import timezone

# 将项目根目录添加到 Python 的模块搜索路径中
back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
img_root = 'images/'

def add_one_team(name):
    team = Team(name=name, logo=os.path.join(img_root + name+'.png'))
    team.save()

def add_many_teams(*names):
    for name in names:
        add_one_team(name)

def add_lpl_teams():
    teams = ['IG', 'TES', 'FPX', 'JDG', 'LGD', 'RNG', 'EDG', 'WE',
            'LNG', 'SN', 'ES', 'BLG', 'DMO', 'RW', 'V5', 'VG', 'OMG']
    add_many_teams(*teams)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lpl_site.settings")
    django.setup()

    from record.models import Team

    if len(sys.argv) > 1:
        add_many_teams(*sys.argv[1:])
    else:
        add_lpl_teams()