from django.urls import path
from .views import Weekdelete,WeekAllget,WeekUpdate,WeekDeeteles
urlpatterns = [
    path('get_all/',WeekAllget.as_view()),
    path('update/:<week_id>/',WeekUpdate.as_view()),
    path('delete/:<week_id>/',Weekdelete.as_view()),
    path('deteles/:<week_id>',WeekDeeteles.as_view())
]