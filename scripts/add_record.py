import os
import pathlib
import random
import sys
from datetime import datetime

import django
from django.utils import timezone

# 将项目根目录添加到 Python 的模块搜索路径中
back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lpl_site.settings")
    django.setup()

    from record.models import Team, Record

    w, l, s1, s2 = sys.argv[1:5]
    s1, s2 = int(s1), int(s2)
    w = Team.objects.get(name=w)
    l = Team.objects.get(name=l)
    
    if len(sys.argv) > 5:
        m, d, h = sys.argv[5:]
        m, d, h = int(m), int(d), int(h)
        dt = datetime(2020, m, d, h)
    else:
        dt = timezone.now()

    Record.objects.create(winner=w, loser=l, winner_score=s1, loser_score=s2, date=dt)