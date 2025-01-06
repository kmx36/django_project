from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('',
         views.PostListView.as_view(),
         name='post_list'),
    path('<int:post_id>/',
         views.PostDetailListView.as_view(),
         name='post_detail'),
    path('create/',
         views.PostCreateView.as_view(),
         name='create_post'),
    path('<int:post_id>/edit/',
         views.PostUpdateView.as_view(),
         name='edit_post'),
    path('<int:post_id>/delete/',
         views.PostDeleteView.as_view(),
         name='delete_post'),

    path('<int:post_id>/comment/',
         views.CommentCreateView.as_view(),
         name='create_comment'),
    path('<int:post_id>/edit_comment/<int:comment_id>/',
         views.CommentUpdateView.as_view(),
         name='edit_comment'),
    path('<int:post_id>/delete_comment/<int:comment_id>/',
         views.CommentDeleteView.as_view(),
         name='delete_comment'),

    path('<slug:category_slug>/',
         views.CategoryPostsListView.as_view(),
         name='category_posts'),
]
