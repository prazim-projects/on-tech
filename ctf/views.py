from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Challenge
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import login




def dashboard(request):
    return render(request, "users/dashboard.html")

@login_required
def challenge_list(request):
    challenges = Challenge.objects.order_by('name')[:5]
    context = {
        'challenges': challenges,
    }
    return render(request, 'ctf/challenge_list.html', context)

@login_required
def challenge_detail(request, pk):
    challenge = Challenge.objects.get(pk=pk)
    context = {
        'challenge': challenge,
    }
    return render(request, 'ctf/challenge_detail.html', context)

@login_required
def submit_flag(request, pk):
    challenge = Challenge.objects.get(pk=pk)
    if request.method == 'POST':
        submitted_flag = request.POST.get('flag')
        if submitted_flag == challenge.flag:
            message = "Correct flag! Challenge completed."
        else:
            message = "Incorrect flag. Try again."
    template = loader.get_template('ctf/submit_flag.html')
    context = {
        'challenge': challenge,
    }
    return render(request, 'ctf/submit_flag.html', context)


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})