from django import forms


from .models import Mentoring, Plan, Apply, MAJOR_CHOICES

class MentoringForm(forms.ModelForm):
    class Meta:
        model = Mentoring
        fields = ('name', 'area_highschool', 'grade', 'phone_mentee', 'phone_keeper', 'date', 'wannabe', 'university', 'major1', 'major2', 'major3', 'rating', 'will_to_study', 'questions', 'requirements')
        widgets = {
            'will_to_study' : forms.RadioSelect(attrs={'style':'display:none'})

        }


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('major_intro', 'time_manage', 'grade_manage', 'subject_study', 'know_how', 'delivering_message',)


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('content',)

