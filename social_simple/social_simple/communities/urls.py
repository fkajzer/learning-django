from django.urls import path, re_path
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.ListCommunities.as_view(), name='all'),
    path('new/', views.CreateCommunity.as_view(), name='new'),
    re_path(
        r'^p/in/(?P<slug>[\w|-]+)',
        views.SingleCommunity.as_view(),
        name='single'),
    re_path(
        r'^join/(?P<slug>[\w|-]+)',
        views.JoinCommunity.as_view(),
        name='join'),
    re_path(
        r'^leave/(?P<slug>[\w|-]+)',
        views.LeaveCommunity.as_view(),
        name='leave'),
]
