"""onedayschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static


from django.contrib import admin

from mentoring import views as mentoring_views
from accounts import views as accounts_views

urlpatterns = [
    url(r'^$', mentoring_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^intro/$', mentoring_views.intro, name='intro'),
    url(r'^program_info/$', mentoring_views.program_info, name='program_info'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^mentoring/', include('mentoring.urls')),
    url(r'^Q&A/', include('QNA.urls')),
    url(r'^access_terms/$', accounts_views.access_terms, name='access_terms'),
    url(r'^personal_info_terms/$', accounts_views.personal_info_terms, name='personal_info_terms'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)