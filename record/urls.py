from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, RecordViewSet, team_detail

router = DefaultRouter()
router.register('team', TeamViewSet, basename='team')
router.register('record', RecordViewSet, basename='record')

urlpatterns = [
    path('', include(router.urls)),
    path('detail/<str:name>/', team_detail),
]