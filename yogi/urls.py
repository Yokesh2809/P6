from django.urls import path
from yogi import views

app_name="yogi"
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name="home"),
    path('fact/<n>',views.fact,name="fact"),
    path('child/',views.child,name="child"),
]