from django.shortcuts import render, redirect
from .models import Tweet
from django.http import HttpResponseRedirect

from useraccounts.forms import UsernameForm
from tweets.forms import TweetForm

# Create your views here.
def index(request):

    if request.method == 'POST':
        username_form = UsernameForm(request.POST)
        tweet_form = TweetForm(request.POST)

        if username_form.is_valid():
            return HttpResponseRedirect('/results/' + username_form.cleaned_data['username'])
        if tweet_form.is_valid():
            Tweet(user_account=request.user.user_account, text=tweet_form.cleaned_data['tweet']).save()

            return redirect(request.META['HTTP_REFERER'])

    else:
        username_form = UsernameForm()
        tweet_form = TweetForm()
        follows = request.user.user_account.follows.all()
        tweets = Tweet.objects.filter(user_account__in=follows)

    context = {
        'tweets': tweets,
        'username_form': username_form,
        'tweet_form': tweet_form,
    }
    return render(request, 'tweets/index.html', context)
