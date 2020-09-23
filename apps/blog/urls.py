# apps/blog/urls.py

from django.conf.urls import url

from .views import *


urlpatterns = (
    url('^$', BlogPostList.as_view(), name='blog_post_list'),
    url('^acronyms/$', view_acronyms, name='view_acronyms'),
    url('^tags/(?P<tag>.*)/$', BlogPostList.as_view(), name='blog_post_list_tag'),
    url("^post/(?P<slug>.*)/$", BlogPostList.as_view(template_name="blog_post_detail.html"), name="blog_post_detail"),
)
