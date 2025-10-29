from django.shortcuts import render
from django.template import loader

# Create your views here.
from .models import Challenge

def challenge_list(request):
    challenges = Challenge.objects.order_by('created_at')
    template = loader.get_template('ctf/challenge_list.html')
    context = {
        'challenges': challenges,
    }
    return render(request, 'ctf/challenge_list.html', context)

def challenge_detail(request, pk):
    challenge = Challenge.objects.get(pk=pk)
    template = loader.get_template('ctf/challenge_detail.html')
    context = {
        'challenge': challenge,
    }
    return render(request, 'ctf/challenge_detail.html', context)

def submit_flag(request, pk):
    challenge = Challenge.objects.get(pk=pk)
    if request.method == 'POST':
        submitted_flag = request.POST.get('flag')
        # Logic to check the flag and create a Submission object
        # ...
    template = loader.get_template('ctf/submit_flag.html')
    context = {
        'challenge': challenge,
    }
    return render(request, 'ctf/submit_flag.html', context)

