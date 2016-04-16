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
    url(r'^(?P<pk>[0-9]+)/mentorfeedback/new/$', views.mentorfeedback_new, name='mentorfeedback_new'),
    url(r'^(?P<pk>[0-9]+)/mentorfeedback/edit/$', views.mentorfeedback_edit, name='mentorfeedback_edit'),
    url(r'^(?P<pk>[0-9]+)/mentorfeedback/$', views.mentorfeedback_detail, name='mentorfeedback_detail'),
    url(r'^(?P<pk>[0-9]+)/menteefeedback/new/$', views.menteefeedback_new, name='menteefeedback_new'),
    url(r'^(?P<pk>[0-9]+)/menteefeedback/edit/$', views.menteefeedback_edit, name='menteefeedback_edit'),
    url(r'^(?P<pk>[0-9]+)/menteefeedback/$', views.menteefeedback_detail, name='menteefeedback_detail'),
    url(r'^(?P<pk>\d+)/apply/new/$', views.apply_new, name='apply_new'),
    url(r'^(?P<pk>\d+)/apply/(?P<apply_pk>\d+)/edit/$', views.apply_edit, name='apply_edit'),
    url(r'^(?P<pk>\d+)/apply/(?P<apply_pk>\d+)/mentoring_authenticate/$', views.mentoring_authenticate, name='mentoring_authenticate'),
    url(r'^recommendmentor/$', views.recommendmentor_list, name='recommendmentor_list'),
    url(r'^review/$', views.review_list, name='review_list'),
    url(r'^review/(?P<pk>\d+)/$', views.review_detail, name='review_detail'),
    url(r'^Q&A/$', views.mentoring_qna_main, name='mentoring_qna_main'),
    url(r'^Q&A/list/$', views.mentoring_question_list, name='mentoring_question_list'),
    url(r'^Q&A/(?P<pk>\d+)/$', views.mentoring_question_detail, name='mentoring_question_detail'),
    url(r'^Q&A/new/$', views.mentoring_question_new, name='mentoring_question_new'),
    url(r'^Q&A/(?P<pk>\d+)/edit/$', views.mentoring_question_edit, name='mentoring_question_edit'),
    url(r'^Q&A/(?P<pk>\d+)/delete/$', views.mentoring_question_delete, name='mentoring_question_delete'),
    url(r'^Q&A/(?P<pk>\d+)/answer/new/$', views.mentoring_answer_new, name='mentoring_answer_new'),
    url(r'^Q&A/(?P<pk>\d+)/answer/(?P<mentoring_answer_pk>\d+)/edit/$', views.mentoring_answer_edit, name='mentoring_answer_edit'),
    url(r'^Q&A/(?P<pk>\d+)/answer/(?P<mentoring_answer_pk>\d+)/delete/$', views.mentoring_answer_delete, name='mentoring_answer_delete'),
    url(r'^Q&A/FAQ/$', views.mentoring_faq_list, name='mentoring_faq_list'),
    url(r'^Q&A/FAQ/(?P<pk>\d+)/$', views.mentoring_faq_detail, name='mentoring_faq_detail'),



]