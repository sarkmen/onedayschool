from django import forms


from .models import Mentoring, Plan, Apply, Mentorfeedback, Menteefeedback, Mentoring_question, Mentoring_answer, MAJOR_CHOICES

class MentoringForm(forms.ModelForm):
    class Meta:
        model = Mentoring
        fields = ('name', 'area_highschool', 'grade', 'phone_mentee', 'phone_keeper', 'date', 'wannabe', 'university', 'major1', 'major2', 'major3', 'rating', 'will_to_study', 'questions', 'requirements')
        widgets = {
            'will_to_study' : forms.RadioSelect(attrs={'style':'display: none'}),

        }


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('mentor_intro','mentor_spec','major_intro', 'time_manage', 'grade_manage', 'subject_study', 'know_how','answering_question', 'delivering_message',)
        widgets = {
            'mentor_intro' : forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'프로그램 소개 -> 멘토 소개 참고'}),
            'mentor_spec' : forms.Textarea(attrs={'style':'resize:none;', 'rows':8, 'placeholder':'프로그램 소개 -> 멘토 소개 참고'}),
            'major_intro' : forms.Textarea(attrs={'style':'resize:none;', 'rows':14, 'placeholder':' 자신의 전공에 대한 설명을 배우는 교과목, 추후 진로등에 대해 멘티들이 이해하기 쉽고 구체적으로 설명해 주세요. 학과 소개 자료 및 멘티들에게 알려 줄 수 있는 내용이 있으면 함께 첨부 해 주셔도 됩니다. (300자 내외)'}),
            'time_manage' : forms.Textarea(attrs={'style':'resize:none;', 'rows':14, 'placeholder':' 학습 계획표 세우는 법을 구체적으로 설명해 주세요. (200자 내외)'}),
            'grade_manage' : forms.Textarea(attrs={'style':'resize:none;', 'rows':14, 'placeholder':' 내신 관리 비법을 구체적으로 설명해 주세요. (200자 내외)'}),
            'subject_study' : forms.Textarea(attrs={'style':'resize:none;', 'rows':14, 'placeholder':' 과목별 공부법을 구체적으로 설명해 주세요. (과목별 100자 내외)'}),
            'know_how' : forms.Textarea(attrs={'style':'resize:none;', 'rows':14, 'placeholder':' 기타 멘티들에게 알려주고 싶은 본인만의 특별한 공부법을 구체적으로 상세히 설명해 주세요. '}),
            'answering_question' : forms.Textarea(attrs={'style':'resize:none;', 'rows':16, 'placeholder':' 위의 멘토링 정보 탭을 참고하여 멘티가 멘토에게 궁금한 질문에 대한 답변을 성실하게 작성해 주세요. '}),
            'delivering_message' : forms.Textarea(attrs={'style':'resize:none;', 'rows':8,}),
            }


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('content',)


class MentorfeedbackForm(forms.ModelForm):
    class Meta:
        model = Mentorfeedback
        fields = ('dream', 'happiness', 'worry', 'subjects', 'future_path', 'lifestyle', 'sw', 'reference', )
        widgets = {
            'dream' : forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'과학자, 의사, 예술가 등'}),
            'happiness' : forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'영화나 다큐멘터리 보면서 관련 자료 조사하고 친구들, 엄마, 아빠에게 설명할 때 행복해 보입니다 등'}),
            'worry' : forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'성적이 생각만큼 좋지 않아 원하는 대학 갈 수 있을지 고민하고 있고 동시에 이성문제로 인해 학업에 집중하지 못하고 있어요 등'}),
            'subjects' : forms.Textarea(attrs={'style':'resize:none;', 'rows':12, 'placeholder':'과학을 좋아하지만 성적이 잘 나오지는 않고 수학은 잘 합니다. 국어 성적과 사회 성적은 잘 안나오는 편. 학생은 생각하고 논리적으로 추론하는 것을 좋아하지만 암기하는 것은 잘 못합니다. 책을 많이 읽지 않아 글 읽는 속도가 느리고 문맥을 빨리 파악하지 못해 국어와 사회 점수가 잘 안나오고 과학 또한 흥미에 비해서는 점수가 잘 나오지 않습니다. 독서 습관이 없어 좋아하는 책에 대한 독서를 시작으로 하여 책읽는 습관을 붙이고 이를 바탕으로 관련 교과랑 연결지어 폭넓은 공부를 하는 것이 장기적으로 도움이 될 것입니다 등'}),
            'future_path' : forms.Textarea(attrs={'style':'resize:none;', 'rows':12, 'placeholder':'어릴적 우연히 보게된 영화 ‘어벤저스’를 보고 영웅들에 대해 관심 가지게 되었고, 과학을 통해 인간의 능력을 무한히 끌어올리는 것에 대해 신기함과 동시에 흥미를 느끼게 되었습니다. 영화속 등장인물이 정말 가능할지 관련 문헌을 인터넷 웹페이지에서 시작해서, 뉴스기사, 과학 저널, 논문으로 이어진다면 자연스럽게 독서, 논문으로 이어질 것이고 과학에 대한 탄탄한 지식과 읽고 쓰는 국어능력 아울러 사회적 측면까지 고려하게 되는 눈을 가지게 될 것입니다.  영화만 계속 본다면 문제가 있겠지만 이런 종류의 영화가 자극이 되어 좀 더 학문의 세계와 학교공부로 이어질 수 있다면 원하는 꿈에 한 발자국 더 다가갈 수 있을 것입니다. 학교에서 국어, 과학, 사회 시간에 이런 주제로 조별활동, 개별 발표가 종종 있습니다. 그때 학생들에게 인정받으며 자신감을 키우고 생활기록부에 진로, 특기사항으로 기록되어 차후 자소서나 추천서 쓸 때 도움이 될 것입니다 등'}),
            'lifestyle' : forms.Textarea(attrs={'style':'resize:none;', 'rows':8, 'placeholder':'학교- 학원-집 의 규칙적인 생활을 하며 성실하게 임하고 있습니다. 하지만 학원에 밤 12시까지 있으면서 ~~~입니다. 오랜 시간 앉아서 공부하는 것보다 하루하루의 목표량을 정하고 달성하면 쉴수 있는 보상을 주어 좀 더 효율적인 공부를 할 수 있을 것입니다 등'}),
            'sw' : forms.Textarea(attrs={'style':'resize:none;', 'rows':8, 'placeholder':'자신이 흥미를 가지고 꽃히면 물불 가리지 않고 빠져들어가는 성향이 있습니다. 하지만 관심이 없는 것에 대해서는 집중을 할 수 없고 딴생각을 합니다. 관심 없는 것에 흥미를 느낄 수 있도록 하는 것이 가장 좋은 방법이지만 현실적으로는 단기적인 목표를 설정하여 필요한 수준까지는 해낼 수 있는 동기부여가 필요합니다 등'}),
            'reference' : forms.Textarea(attrs={'style':'resize:none;', 'rows':8, 'placeholder':'너무 공부공부 하면서 실증 느끼게 하는 것보다 적당히 휴식과 동기를 주면서 스스로 흥미를 느껴 할 수 있는 환경이 만들어지면 좋을 것 같습니다 등'}),
        }


class MenteefeedbackForm(forms.ModelForm):
    class Meta:
        model = Menteefeedback
        fields = ('impression', 'expect', 'inconvinience', 'touring_rating', 'touring_rating_reason', 'mentor_rating', 'mentor_rating_reason', 'mirroring', 'wannabe', 'mentoring_rating', 'mentoring_rating_reason', 'helpness', 'onetime', )
        widgets = {
            'touring_rating': forms.HiddenInput,
            'mentor_rating': forms.HiddenInput,
            'mentoring_rating': forms.HiddenInput,
            'impression': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'색으로 표현하면? 향기로 표현하면? 음악으로 표현하면? 등 자유롭게' }),
            'expect': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'평가와 후기를 남겨주세요' }),
            'inconvinience': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':' 이 글을 읽는 멘토가 바로 해결해 줄 거에요' }),
            'touring_rating_reason': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'평가와 후기를 남겨주세요' }),
            'mentor_rating_reason': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'평가와 후기를 남겨주세요' }),
            'mirroring': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'평가와 후기를 남겨주세요' }),
            'wannabe': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'~한 멘토였으면 좋겠어요' }),
            'mentoring_rating_reason': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'~한 점이 좋았어요' }),
            'helpness': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'~한 점들이 도움이 되었어요' }),
            'onetime': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'1번이면 충분해요, 멘토와 앞으로도 연락하고 싶어요 등' }),

        }


class Mentoring_questionForm(forms.ModelForm):
    class Meta:
        model = Mentoring_question
        fields = ('title', 'content')


class Mentoring_answerForm(forms.ModelForm):
    class Meta:
        model = Mentoring_answer
        fields = ('content',)