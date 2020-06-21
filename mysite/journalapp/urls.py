from django.urls import path
from . import views


app_name = journalapp
urlpatterns = [
    #ex: /
    path('', views.index, name='index'),

    #ex: /home/1/
    path('home/<int:user_id>/', views.home, name='home'),

    #ex: /home/1/2/
    path('home/<int:user_id>/<int:journal_id>/', views.journal_view, name='journal_view'),

    #ex: /home/1/2/6/
    path('home/<int:user_id>/<int:journal_id>/<int:entry_id>/', views.entry_view, name='entry_view'),

    #ex: /home/1/2/
    path('home/<int:user_id>/<int:journal_id>/new/', views.new_entry, name='new_entry'),
]
