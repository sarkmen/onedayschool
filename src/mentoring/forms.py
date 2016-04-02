from django import forms


from .models import Mentoring, Plan, Apply

class MentoringForm(forms.ModelForm):
    class Meta:
        model = Mentoring
        fields = ('major', 'date', 'requirements')


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('major_intro', 'time_manage', 'grade_manage', 'subject_study', 'know_how', 'delivering_message',)


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('content',)

