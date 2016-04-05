from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.qna_main, name='qna_main'),
    url(r'^list/$', views.question_list, name='question_list'),
    url(r'^(?P<pk>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^new/$', views.question_new, name='question_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.question_edit, name='question_edit'),
    url(r'^(?P<pk>\d+)/answer/new/$', views.answer_new, name='answer_new'),
    url(r'^(?P<pk>\d+)/answer/(?P<answer_pk>\d+)/edit/$', views.answer_edit, name='answer_edit'),
    url(r'^(?P<pk>\d+)/answer/(?P<answer_pk>\d+)/delete/$', views.answer_delete, name='answer_delete'),
    url(r'^FAQ/$', views.faq_list, name='faq_list'),
    url(r'^FAQ/(?P<pk>\d+)/$', views.faq_detail, name='faq_detail'),



]