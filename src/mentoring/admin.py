from django.contrib import admin
from .models import Mentoring, Plan, Recommendmentor, Review, Mentoring_faq, Mentoring_question, Mentoring_answer, Mentorfeedback, Menteefeedback

# Register your models here.
admin.site.register(Mentoring)
admin.site.register(Plan)
admin.site.register(Recommendmentor)
admin.site.register(Review)
admin.site.register(Mentoring_faq)
admin.site.register(Mentoring_answer)
admin.site.register(Mentoring_question)
admin.site.register(Mentorfeedback)
admin.site.register(Menteefeedback)