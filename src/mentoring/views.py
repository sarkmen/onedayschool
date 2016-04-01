from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Mentoring, Plan, Apply
from .forms import MentoringForm, PlanForm, ApplyForm
from accounts.models import Profile

# Create your views here.
def index(request):
    return render(request, 'mentoring/index.html')

def mentoring_list(request):
    mentoring_list = Mentoring.objects.all()
    return render(request, 'mentoring/mentoring_list.html', {'mentoring_list' : mentoring_list})

def mentoring_detail(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    return render(request, 'mentoring/mentoring_detail.html', {'mentoring' : mentoring, 'apply_form' : ApplyForm(), })

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

    return render(request, 'mentoring/mentoring_form.html', {'mentoringform' : mentoringform})

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

    return render(request, 'mentoring/mentoring_form.html', {'mentoringform' : mentoringform})


def plan_detail(request, pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    plan = mentoring.plan
    return render(request, 'mentoring/plan_detail.html', {'plan' : plan})



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
    return render(request, 'mentoring/plan_form.html', {'planform' : planform, 'mentoring' : mentoring})

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
    return render(request, 'mentoring/plan_form.html', {'planform' : planform, 'mentoring' : mentoring})


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


def apply_edit(request, pk, apply_pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    apply = get_object_or_404(Apply, pk=apply_pk)
    if request.method == "POST":
        applyform = ApplyForm(request.POST, instance=apply)
        if applyform.is_valid():
            apply = applyform.save(commit=False)
            apply.save()
            return redirect(mentoring_detail, pk=pk)


def mentoring_authenticate(request, pk, apply_pk):
    mentoring = get_object_or_404(Mentoring, pk=pk)
    apply = get_object_or_404(Apply, pk=apply_pk)
    if request.method == "POST":
        mentoring.acceptor = apply.applicant
        mentoring.save()
        return redirect(mentoring_detail, pk=pk)
    return render(request, 'mentoring/mentoring_detail.html', {'mentoring' : mentoring, 'apply_form' : ApplyForm(), })


