from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Challenge, Submission
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import login
from .forms import FlagSubmitForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum, Q
from django.db.models.functions import Coalesce
import json


@login_required
def scoreboard(request):
    users = User.objects.annotate(
        score=Coalesce(Sum('submission__challenge__points', filter=Q(submission__is_correct=True)), 0),
        solves=Coalesce(Sum(1, filter=Q(submission__is_correct=True)), 0)
    ).order_by('-score')


    usernames = json.dumps([u.username for u in users])
    scores = json.dumps([u.score for u in users])


    nav = [
        ['Home', 'home'],
        ["Blog", "blog_home"],
        ["CTF", "challenge_list"],
    ]
    
    if request.user.is_authenticated:
        nav += [
            ["Scoreboard", "scoreboard"],
        ]

    else:
        nav += [
            ["Login", "login"],
            ["Register", "register"],
        ]

    context = {
        "users": users, "usernames": usernames, "scores": scores, 'nav': nav
    }

    return render(request, 'ctf/scoreboard.html', context)


@login_required
def challenge_list(request):
    challenges = Challenge.objects.order_by('id')[:5]
    nav = [
        ['Home', 'home'],
        ["Blog", "blog_home"],
        ["CTF", "challenge_list"],
    ]

    if request.user.is_authenticated:
        nav += [
            ["Scoreboard", "scoreboard"],
        ]

    else:
        nav += [
            ["Login", "login"],
            ["Register", "register"],
        ]

    context = {
        'challenges': challenges, 'nav': nav
    }
    return render(request, 'ctf/challenge_list.html', context)

@login_required
def challenge_detail(request, pk):
    challenge = Challenge.objects.get(pk=pk)
    form = FlagSubmitForm(initial={'challenge_id': challenge.id})

    if request.method == 'POST':
        flagForm = FlagSubmitForm(request.POST)
        if flagForm.is_valid():
            submitted_flag = flagForm.cleaned_data['flag'].strip()
            #has user submitted flag before?
            submission, created = Submission.objects.get_or_create(
                user=request.user,
                challenge=challenge,
            )

            if submission.is_correct:
                messages.info(request, "You already solved this challenge!")
                return HttpResponseRedirect(request.path_info)

            if submitted_flag == challenge.flag:
                submission.submitted_flag = submitted_flag
                submission.is_correct = True
                submission.save()
                messages.success(request, "Correct flag! Challenge completed.")
            else:
                submission.submitted_flag = submitted_flag
                submission.is_correct = False
                submission.save()
                messages.error(request, "Incorrect flag. Try again.")
            
            return HttpResponseRedirect(request.path_info)
        
    context = {
        'challenge': challenge,
        'form': form,
    }
    return render(request, 'ctf/challenge_detail.html', context)


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("challenge_list"))
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})