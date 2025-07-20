from django.urls import path

from weblog import views

urlpatterns = [
    path('', views.index_page, name="index_page")
]