
from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('songs',views.songs,name='songs'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    # path("", views.DashboardView.as_view(), name="dashboard"),
]
    