from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from accounts.models import Profile

# Create your views here.
def question_list(request):
    question_list = Question.objects.all()
    return render(request, 'QNA/question_list.html', {
        'question_list' : question_list
        })

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'QNA/question_detail.html', {
        'question' : question,
        'answer_form' : AnswerForm(),
        })


@login_required
def question_new(request):
    if request.method == 'POST':
        questionform = QuestionForm(request.POST)
        if questionform.is_valid():
            question = questionform.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, "질문이 성공적으로 등록되었습니다.")
            return redirect(question_detail, pk=question.pk)
    else:
        questionform = QuestionForm()

    return render(request, 'QNA/question_form.html', {
        'questionform' : questionform,
        })

@login_required
def question_edit(request, pk):
    question = get_object_or_404(question, pk=pk)
    if request.method == "POST":
        questionform = QuestionForm(request.POST, instance=question)
        if questionform.is_valid():
            question = questionform.save(commit=False)
            question.save()
            messages.success(request, "질문이 성공적으로 수정되었습니다.")
            return redirect("/")
    else:
        questionform = QuestionForm(instance=question)

    return render(request, 'QNA/question_form.html', {
        'questionform' : questionform
        })

@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user != question.author:
        messages.error(request, "자신이 작성한 질문만 삭제할 수 있습니다.")
        return redirect(question_detail, pk=question.pk)
    question.delete()
    messages.error(request, "질문이 삭제되었습니다.")
    return redirect(question_list)


@login_required
def answer_new(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        answerform = AnswerForm(request.POST)
        if answerform.is_valid():
            answer = answerform.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.created_at = timezone.now()
            answer.save()
            return redirect(question_detail, pk=pk)

@login_required
def answer_edit(request, pk, answer_pk):
    question = get_object_or_404(Question, pk=pk)
    answer = get_object_or_404(Answer, pk=answer_pk)
    if request.method == "POST":
        answerform = AnswerForm(request.POST, instance=answer)
        if answerform.is_valid():
            answer = answerform.save(commit=False)
            answer.save()
            return redirect(question_detail, pk=pk)


@login_required
def answer_delete(request, pk, answer_pk):
    question = get_object_or_404(Question, pk=pk)
    answer = get_object_or_404(Answer, pk=answer_pk)
    if request.user != answer.author:
        messages.error(request, "자신이 작성한 답변만 삭제할 수 있습니다.")
        return redirect(question_detail, pk=question.pk)
    answer.delete()
    messages.error(request, "답변이 삭제되었습니다.")
    return redirect(question_detail, pk=question.pk)

