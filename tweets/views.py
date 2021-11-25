from django.shortcuts import render, redirect
from .models import Tweet
from django.http import HttpResponseRedirect

from useraccounts.forms import UsernameForm
from tweets.forms import TweetForm

# Create your views here.
def index(request):

    if request.method == 'POST':
        tweet_form = TweetForm(request.POST)

        if tweet_form.is_valid():
            Tweet(user_account=request.user.user_account, text=tweet_form.cleaned_data['tweet']).save()

            return redirect(request.META['HTTP_REFERER'])

    else:
        tweet_form = TweetForm()
        tweets = Tweet.objects.filter(user_account__in=request.user.user_account.follows.all())

    context = {
        'tweets': tweets,
        'tweet_form': tweet_form,
    }
    return render(request, 'tweets/index.html', context)
