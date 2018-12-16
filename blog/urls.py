from django.urls import path, re_path, include

from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/search', views.get_posts_by_keyword, name='posts-by-keyword'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/category/<str:category_name>', views.get_posts_by_category, name='posts-by-category'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]