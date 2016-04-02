from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.mentoring_list, name='mentoring_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.mentoring_detail, name='mentoring_detail'),
    url(r'^new/$', views.mentoring_new, name='mentoring_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.mentoring_edit, name='mentoring_edit'),
    url(r'^(?P<pk>[0-9]+)/plan/new/$', views.plan_new, name='plan_new'),
    url(r'^(?P<pk>[0-9]+)/plan/edit/$', views.plan_edit, name='plan_edit'),
    url(r'^(?P<pk>[0-9]+)/plan/$', views.plan_detail, name='plan_detail'),
    url(r'^(?P<pk>\d+)/apply/new/$', views.apply_new, name='apply_new'),
    url(r'^(?P<pk>\d+)/apply/(?P<apply_pk>\d+)/edit/$', views.apply_edit, name='apply_edit'),
    url(r'^(?P<pk>\d+)/apply/(?P<apply_pk>\d+)/mentoring_authenticate/$', views.mentoring_authenticate, name='mentoring_authenticate'),
    url(r'^recommendmentor/$', views.recommendmentor_list, name='recommendmentor_list'),
    url(r'^review/$', views.review_list, name='review_list'),
    url(r'^review/(?P<pk>\d+)/$', views.review_detail, name='review_detail')

]