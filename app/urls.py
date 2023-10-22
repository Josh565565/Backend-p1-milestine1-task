from django.urls import path
from . import views
from .views import MainObjectListView


urlpatterns = [
    path('', views.ping, name="ping"),
    path('main-objects/', MainObjectListView.as_view(), name='main-object-list'),
]