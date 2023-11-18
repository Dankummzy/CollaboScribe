from django.urls import path
from .views import create_article, edit_article, delete_article, view_article

app_name = 'articles'

urlpatterns = [
    path('create/', create_article, name='create_article'),
    path('<int:article_id>/edit/', edit_article, name='edit_article'),
    path('<int:article_id>/delete/', delete_article, name='delete_article'),
    path('<int:article_id>/', view_article, name='view_article'),
    # Add more URL patterns as needed
]
