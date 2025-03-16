from django.urls import path
from .views import *
urlpatterns = [
    path('',Loginuser,name='login'),
    path('home',home,name='home'),
    path('book1/',book1,name='help'),
    path('feedback/',feedbackuser,name='feedback'),
    path('foodbook/',foodbookuser,name='foodbook'),
    path('booklist/',booklist,name='booklist'),
    path('logout/',Logoutuser,name='Logoutuser'),
    path('helplist/',helplist,name='helplist'),
    path('feedbacklist/',feedbacklist,name='feedbacklist'),
    path('delete/<int:id>',deleteuser,name='delete'),
    path('helpview/<int:id>',helpview,name='helpview'),
    path('feedbackview/<int:id>',feedbackview,name='feedbackview'),
]
