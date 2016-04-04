from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Mentoring, Plan, Apply, Recommendmentor, Review
from .forms import MentoringForm, PlanForm, ApplyForm
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
    return render(request, 'mentoring/mentoring_detail.html', {
        'mentoring' : mentoring,
        'apply_form' : ApplyForm(),
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
    plan = get_object_or_404(Plan, pk=mentoring.pk)
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
