
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home, name='index'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.Logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('addNotes', views.addNotes, name='addNotes'),
    path('viewNotes', views.viewNotes, name='viewNotes'),
    path('editNotes/<int:pid>', views.editNotes, name='editNotes'),
    path('deleteNotes/<int:pid>', views.deleteNotes, name='deleteNotes'),
    path('changePassword', views.changePassword, name='changePassword'),
   
]
