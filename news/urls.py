from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from news import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_for_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_post/', views.create_post, name='create_post'),
    path('<int:post_id>/update_post/', views.update_post, name='update_post'),

    path('', views.post_list, name='post_list'),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    re_path(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
            views.post_detail,
            name='post_detail'),
]

