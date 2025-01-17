from django.urls import path
from .views import ArticleListView,ArticleDetailView
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_page'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='article_detail_page'),
]

# how to store a list in django postgresql model