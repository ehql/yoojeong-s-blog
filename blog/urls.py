# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, HomePageView, about_view, WorksView, newsroom_view
from . import views
from .views import works_view


urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),  # 게시물 목록을 위한 경로 변경
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'), 
    path('about/', about_view, name='about'),
    path('works/', works_view, name='works'),
    path('newsroom/', newsroom_view, name='newsroom'),
    path('rks/post_delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('add_project_post/<str:project_type>/', views.add_project_post, name='add_project_post')
]
