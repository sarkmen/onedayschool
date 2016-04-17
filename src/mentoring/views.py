from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Mentoring, Plan, Apply, Recommendmentor, Review, Mentorfeedback, Menteefeedback, Mentoring_question, Mentoring_answer, Mentoring_faq
from .forms import MentoringForm, PlanForm, ApplyForm, MentorfeedbackForm, MenteefeedbackForm, Mentoring_questionForm, Mentoring_answerForm
from accounts.models import Profile

# Create your views here.
def index(request):
    return render(request, 'mentoring/index.html')


def intro(request):
    return render(request, 'mentoring/intro.html')

def program_info(request):
    return render(request, 'mentoring/program_info.html')


def mentoring_list(request):
    mentoring_list = Mentoring.objects.all()
    return render(request, 'mentoring/mentoring_list.html', {
        'mentoring_list' : mentoring_list
        })


def mentoring_detail(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    plan = mentoring.plan
    return render(request, 'mentoring/mentoring_detail.html', {
        'mentoring' : mentoring,
        'apply_form' : ApplyForm(),
        'plan' : plan,
        })


@login_required
def mentoring_new(request):
    if request.method == 'POST':
        mentoringform = MentoringForm(request.POST)
        if mentoringform.is_valid():
            mentoring = mentoringform.save(commit=False)
            mentoring.author = request.user
            mentoring.save()
            messages.success(request, "멘토링이 성공적으로 등록되었습니다.")
            return redirect(mentoring_detail, pk=mentoring.pk)
    else:
        mentoringform = MentoringForm()
    return render(request, 'mentoring/mentoring_form.html', {
        'mentoringform' : mentoringform
        })


@login_required
def mentoring_edit(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    if request.method == "POST":
        mentoringform = MentoringForm(request.POST, instance=mentoring)
        if mentoringform.is_valid():
            mentoring = mentoringform.save(commit=False)
            mentoring.save()
            messages.success(request, "멘토링이 성공적으로 수정되었습니다.")
            return redirect("/")
    else:
        mentoringform = MentoringForm(instance=mentoring)
    return render(request, 'mentoring/mentoring_form.html', {
        'mentoringform' : mentoringform
        })


@login_required
def mentoring_delete(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    if request.user != mentoring.author:
        messages.error(request, "자신이 신청한 멘토링만 삭제할 수 있습니다.")
        return redirect(mentoring_detail, pk=mentoring.pk)
    mentoring.delete()
    messages.error(request, "멘토링 신청이 취소되었습니다.")
    return redirect(mentoring_list)


def plan_detail(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    plan = mentoring.plan
    return render(request, 'mentoring/plan_detail.html', {
        'plan' : plan
        })


@login_required
def plan_new(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    if request.method == "POST":
        planform = PlanForm(request.POST)
        if planform.is_valid():
            plan = planform.save(commit=False)
            plan.mentoring = mentoring
            plan.mentor = request.user
            plan.save()
            return redirect(plan_detail, pk=pk)
    else:
        planform = PlanForm()
    return render(request, 'mentoring/plan_form.html', {
        'planform' : planform,
        'mentoring' : mentoring
        })


@login_required
def plan_edit(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    plan = mentoring.plan
    if request.method == "POST":
        planform = PlanForm(request.POST, instance=plan)
        if planform.is_valid():
            plan = planform.save(commit=False)
            plan.mentoring = mentoring
            plan.mentor = request.user
            plan.save()
            return redirect(plan_detail, pk=pk)
    else:
        planform = PlanForm()
    return render(request, 'mentoring/plan_form.html', {
        'planform' : planform,
        'mentoring' : mentoring
        })


@login_required
def plan_delete(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.user != plan.mentor:
        messages.error(request, "자신이 작성한 계획서만 삭제할 수 있습니다.")
        return redirect(plan_detail, pk=plan.pk)
    plan.delete()
    messages.error(request, "멘토링 계획서가 삭제되었습니다.")
    return redirect(mentoring_list)


@login_required
def apply_new(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    if request.method == "POST":
        applyform = ApplyForm(request.POST)
        if applyform.is_valid():
            apply = applyform.save(commit=False)
            apply.mentoring = mentoring
            apply.applicant = request.user
            apply.created_at = timezone.now()
            apply.save()
            return redirect(mentoring_detail, pk=pk)


@login_required
def apply_edit(request, pk, apply_pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    apply = get_object_or_404(Apply, pk=apply_pk)
    if request.method == "POST":
        applyform = ApplyForm(request.POST, instance=apply)
        if applyform.is_valid():
            apply = applyform.save(commit=False)
            apply.save()
            return redirect(mentoring_detail, pk=pk)


@login_required
def apply_delete(request, pk, apply_pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    apply = get_object_or_404(Apply, pk=apply_pk)
    if request.user != apply.applicant:
        messages.error(request, "지원자 본인만 취소할 수 있습니다.")
        return redirect(mentoring_detail, pk=mentoring.pk)
    apply.delete()
    messages.error(request, "멘토링 지원이 취소되었습니다.")
    return redirect(mentoring_detail, pk=mentoring.pk)


@login_required
def mentoring_authenticate(request, pk, apply_pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    apply = get_object_or_404(Apply, pk=apply_pk)
    mentoring.acceptor = apply.applicant
    mentoring.save()
    return redirect(mentoring_detail, pk=pk)


def recommendmentor_list(request):
    recommendmentor_list = Recommendmentor.objects.all()
    return render(request, 'mentoring/recommendmentor_list.html', {'recommendmentor_list' : recommendmentor_list
        })


def review_list(request):
    review_list = Review.objects.all()

    #페이지네이션 파트
    paginator = Paginator(review_list, 9)
    page = request.GET.get('page')

    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    return render(request, 'mentoring/review_list.html', {'review_list' : review_list,
        'reviews' : reviews,
        })


def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, "mentoring/review_detail.html", {
        "review" : review,
        })

@login_required
def mentorfeedback_new(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    if request.method == "POST":
        mentorfeedbackform = MentorfeedbackForm(request.POST)
        if mentorfeedbackform.is_valid():
            mentorfeedback = mentorfeedbackform.save(commit=False)
            mentorfeedback.mentoring = mentoring
            mentorfeedback.mentor = request.user
            mentorfeedback.save()
            return redirect(mentorfeedback_detail, pk=pk)
    else:
        mentorfeedbackform = MentorfeedbackForm()
    return render(request, 'mentoring/mentorfeedback_form.html', {
        'mentorfeedbackform' : mentorfeedbackform,
        'mentoring' : mentoring
        })


@login_required
def mentorfeedback_edit(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    mentorfeedback = mentoring.mentorfeedback
    if request.method == "POST":
        mentorfeedbackform = MentorfeedbackForm(request.POST, instance=mentorfeedback)
        if mentorfeedbackform.is_valid():
            mentorfeedback = mentorfeedbackform.save(commit=False)
            mentorfeedback.mentoring = mentoring
            mentorfeedback.mentor = request.user
            mentorfeedback.save()
            return redirect(mentorfeedback_detail, pk=pk)
    else:
        mentorfeedbackform = MentorfeedbackForm()
    return render(request, 'mentoring/mentorfeedback_form.html', {
        'mentorfeedbackform' : mentorfeedbackform,
        'mentoring' : mentoring,
        })


def mentorfeedback_detail(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    mentorfeedback = mentoring.mentorfeedback
    return render(request, 'mentoring/mentorfeedback_detail.html', {
        'mentorfeedback' : mentorfeedback,
        'mentoring' : mentoring,
        })


@login_required
def menteefeedback_new(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    if request.method == "POST":
        menteefeedbackform = MenteefeedbackForm(request.POST)
        if menteefeedbackform.is_valid():
            menteefeedback = menteefeedbackform.save(commit=False)
            menteefeedback.mentoring = mentoring
            menteefeedback.mentee = request.user
            menteefeedback.save()
            return redirect(menteefeedback_detail, pk=pk)
    else:
        menteefeedbackform = MenteefeedbackForm()
    return render(request, 'mentoring/menteefeedback_form.html', {
        'menteefeedbackform' : menteefeedbackform,
        'mentoring' : mentoring
        })


@login_required
def menteefeedback_edit(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    menteefeedback = mentoring.menteefeedback
    if request.method == "POST":
        menteefeedbackform = MenteefeedbackForm(request.POST, instance=menteefeedback)
        if menteefeedbackform.is_valid():
            menteefeedback = menteefeedbackform.save(commit=False)
            menteefeedback.mentoring = mentoring
            menteefeedback.mentor = request.user
            menteefeedback.save()
            return redirect(menteefeedback_detail, pk=pk)
    else:
        menteefeedbackform = MenteefeedbackForm()
    return render(request, 'mentoring/menteefeedback_form.html', {
        'menteefeedbackform' : menteefeedbackform,
        'mentoring' : mentoring,
        })


def menteefeedback_detail(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    menteefeedback = mentoring.menteefeedback
    return render(request, 'mentoring/menteefeedback_detail.html', {
        'menteefeedback' : menteefeedback,
        'mentoring' : mentoring,
        })


def mentoring_qna_main(request):
    mentoring_faq_list = Mentoring_faq.objects.all()
    mentoring_question_list = Mentoring_question.objects.all()
    return render(request, 'mentoring/mentoring_qnamain.html', {
        'mentoring_question_list' : mentoring_question_list,
        'mentoring_faq_list' : mentoring_faq_list,
        })

def mentoring_question_list(request):
    mentoring_question_list = Mentoring_question.objects.all()
    return render(request, 'mentoring/mentoring_question_list.html', {
        'mentoring_question_list' : mentoring_question_list,
        })

def mentoring_question_detail(request, pk):
    mentoring_question = get_object_or_404(Mentoring_question, pk=pk)
    return render(request, 'mentoring/mentoring_question_detail.html', {
        'mentoring_question' : mentoring_question,
        'mentoring_answer_form' : Mentoring_answerForm(),
        })


@login_required
def mentoring_question_new(request):
    if request.method == 'POST':
        mentoring_questionform = Mentoring_questionForm(request.POST)
        if mentoring_questionform.is_valid():
            mentoring_question = mentoring_questionform.save(commit=False)
            mentoring_question.author = request.user
            mentoring_question.save()
            messages.success(request, "질문이 성공적으로 등록되었습니다.")
            return redirect(mentoring_question_detail, pk=mentoring_question.pk)
    else:
        mentoring_questionform = Mentoring_questionForm()

    return render(request, 'mentoring/mentoring_question_form.html', {
        'mentoring_questionform' : mentoring_questionform,
        })

@login_required
def mentoring_question_edit(request, pk):
    mentoring_question = get_object_or_404(Mentoring_question, pk=pk)
    if mentoring_question.author == request.user:
        if request.method == "POST":
            mentoring_questionform = Mentoring_questionForm(request.POST, instance=mentoring_question)
            if mentoring_questionform.is_valid():
                mentoring_question = mentoring_questionform.save(commit=False)
                mentoring_question.save()
                messages.success(request, "질문이 성공적으로 수정되었습니다.")
                return redirect("/")
        else:
            mentoring_questionform = Mentoring_questionForm(instance=mentoring_question)

    else:
        messages.error(request, "질문 작성자만 수정할 수 있습니다.")
        return redirect(mentoring_question_detail, pk=mentoring_question.pk)

    return render(request, 'mentoring/mentoring_question_form.html', {
        'mentoring_questionform' : mentoring_questionform
        })

@login_required
def mentoring_question_delete(request, pk):
    mentoring_question = get_object_or_404(Mentoring_question, pk=pk)
    if request.user != mentoring_question.author:
        messages.error(request, "자신이 작성한 질문만 삭제할 수 있습니다.")
        return redirect(mentoring_question_detail, pk=mentoring_question.pk)
    mentoring_question.delete()
    messages.error(request, "질문이 삭제되었습니다.")
    return redirect(mentoring_question_list)


@staff_member_required
@login_required
def mentoring_answer_new(request, pk):
    mentoring_question = get_object_or_404(Mentoring_question, pk=pk)
    if request.method == "POST":
        mentoring_answerform = Mentoring_answerForm(request.POST)
        if mentoring_answerform.is_valid():
            mentoring_answer = mentoring_answerform.save(commit=False)
            mentoring_answer.question = mentoring_question
            mentoring_answer.author = request.user
            mentoring_answer.created_at = timezone.now()
            mentoring_answer.save()
            return redirect(mentoring_question_detail, pk=pk)

@staff_member_required
@login_required
def mentoring_answer_edit(request, pk, answer_pk):
    mentoring_question = get_object_or_404(Mentoring_question, pk=pk)
    mentoring_answer = get_object_or_404(Mentoring_answer, pk=mentoring_answer_pk)
    if request.method == "POST":
        mentoring_answerform = Mentoring_answerForm(request.POST, instance=mentoring_answer)
        if mentoring_answerform.is_valid():
            mentoring_answer = mentoring_answerform.save(commit=False)
            mentoring_answer.save()
            return redirect(mentoring_question_detail, pk=pk)


@staff_member_required
@login_required
def mentoring_answer_delete(request, pk, mentoring_answer_pk):
    mentoring_question = get_object_or_404(Mentoring_question, pk=pk)
    mentoring_answer = get_object_or_404(Mentoring_answer, pk=mentoring_answer_pk)
    if request.user != mentoring_answer.author:
        messages.error(request, "자신이 작성한 답변만 삭제할 수 있습니다.")
        return redirect(mentoring_question_detail, pk=mentoring_question.pk)
    mentoring_answer.delete()
    messages.error(request, "답변이 삭제되었습니다.")
    return redirect(mentoring_question_detail, pk=mentoring_question.pk)

def mentoring_faq_list(request):
    mentoring_faq_list = Mentoring_faq.objects.all()
    return render(request, 'mentoring/mentoring_faq_list.html', {
        'mentoring_faq_list' : mentoring_faq_list
        })

def mentoring_faq_detail(request, pk):
    mentoring_faq = get_object_or_404(Mentoring_faq, pk=pk)
    return render(request, 'mentoring/mentoring_faq_detail.html', {
        'mentoring_faq' : mentoring_faq,
        })
