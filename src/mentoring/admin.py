from django.contrib import admin
from .models import Mentoring, Plan, Recommendmentor, Review

# Register your models here.
admin.site.register(Mentoring)
admin.site.register(Plan)
admin.site.register(Recommendmentor)
admin.site.register(Review)