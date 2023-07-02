from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('contact',views.contact,name='contact'),
    path('team',views.team,name='team'),
    path('feature',views.feature,name='team'),
    # path('newpage',views.newpage,name='newpage'),
]