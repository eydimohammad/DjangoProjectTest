from django.urls import path

from weblog import views

urlpatterns = [
    path('', views.articles_json, name="index_page")
]
