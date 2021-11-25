from django.shortcuts import render, redirect

from .models import UserAccount
from .forms import UsernameForm

# search results lists all users matching the query in the url
def search_results(request, search_string=""):

    if request.method == 'POST':
        username_form = UsernameForm(request.POST)

        if username_form.is_valid():
            search_string = username_form.cleaned_data['username']

    else:
        username_form = UsernameForm()

    if not search_string == '':
        results = UserAccount.objects.filter(user__username__icontains=search_string)
    else:
        results = None

    context = {
        'username_form': username_form,
        'results': results,
        'search_string': search_string,
    }
    return render(request, 'useraccounts/search_results.html', context)

# let currently logged in follow a user. Both this and the unfollow view can easily be added to any page.
def follow(request, useraccount_id):

    UserAccount.objects.get(user=request.user).follows.add(UserAccount.objects.get(id=useraccount_id))
    return redirect(request.META['HTTP_REFERER'])

# let currently logged in unfollow a user.
def unfollow(request, useraccount_id):

    UserAccount.objects.get(user=request.user).follows.remove(UserAccount.objects.get(id=useraccount_id))
    return redirect(request.META['HTTP_REFERER'])

# lists all other users following the currently logged in user.
def user_followers(request):

    followers = UserAccount.objects.filter(follows=request.user.user_account)

    context = {
        'followers': followers,
    }
    return render(request, 'useraccounts/user_followers.html', context)
