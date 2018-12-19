from django.urls import path, re_path, include

from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/search', views.get_posts_by_keyword, name='posts-by-keyword'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/tag/<str:tag>', views.get_posts_by_tag, name='posts-by-tag'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]