from django.urls import path

from .views import post_list, post_detail, comment_create, post_search

app_name = 'post'
urlpatterns = [
    path('', post_list, name='post-list'),
    path('<int:pk>/', post_detail, name='post-detail'),
    path('<int:pk>/comment/create/', comment_create, name='comment-create'),
    path('search/', post_search, name='post-search'),
]