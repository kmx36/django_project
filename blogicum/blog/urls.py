from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('',
         views.PostListView.as_view(), name='index'),
    path('posts/<int:post_id>/',
         views.PostDetailView.as_view(), name='post_detail'),
    path('posts/create/',
         views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:post_id>/edit/',
         views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:post_id>/delete/',
         views.PostDeleteView.as_view(), name='post_delete'),

    path('posts/<int:post_id>/comment/',
         views.CommentCreateView.as_view(), name='comment_create'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.CommentUpdateView.as_view(), name='comment_edit'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/',
         views.CommentDeleteView.as_view(), name='comment_delete'),

    path('category/<slug:category_slug>/',
         views.CategoryListView.as_view(), name='category'),

    path('profile/<str:username>/',
         views.ProfileDetailView.as_view(), name='profile'),
    path('accounts/profile/',
         views.ProfileUpdateView.as_view(), name='profile_edit'),
]
