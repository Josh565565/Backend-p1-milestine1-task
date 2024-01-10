# urls.py
from django.urls import path
from . import views
from .views import MainObjectListView

urlpatterns = [
    path('', views.ping, name="ping"),
    path('main-objects/', MainObjectListView.as_view(), name='main-object-list'),
    path('search', views.MainObjectSearch.as_view(), name='main-object-search'),
    path('api/main-objects/', views.MainObjectList.as_view(), name='main-object-list'),
    path('api/main-objects/<int:pk>/', views.MainObjectDetail.as_view(), name='main-object-detail'),
]
