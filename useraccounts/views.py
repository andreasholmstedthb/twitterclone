from django.shortcuts import render, redirect

from .models import UserAccount
from .forms import UsernameForm

# Create your views here.
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

def follow(request, useraccount_id):

    UserAccount.objects.get(user=request.user).follows.add(UserAccount.objects.get(id=useraccount_id))
    return redirect(request.META['HTTP_REFERER'])

def unfollow(request, useraccount_id):

    UserAccount.objects.get(user=request.user).follows.remove(UserAccount.objects.get(id=useraccount_id))
    return redirect(request.META['HTTP_REFERER'])
