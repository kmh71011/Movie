from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    path('', views.main, name='main'),
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:movie_id>/detail/', views.detail, name='detail'),
]