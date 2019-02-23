from django.conf.urls import url
from . import views

app_name = 'blogapp'

urlpatterns = [

    url('^$', views.PostListView.as_view(), name='post_list'),
    url('^about/$', views.AboutView.as_view(), name='about'),
    url('^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='detail_list'),
    url('^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url('^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url('^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url('^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url('^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url('^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url('^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url('^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),

]
