from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # home del progetto
    path('', views.home, name='home'),       # home del progetto
    path('post_list/', views.post_list, name='post_list'),
    path('n_post_user/', views.n_post_user, name='n_post_user'),
    path('utente/<int:id>/', views.id_page, name='id_page'),
    path('posts/', views.posts, name='posts'),
    path('posts_last_h/', views.posts_last_h, name='posts_last_h'),
]