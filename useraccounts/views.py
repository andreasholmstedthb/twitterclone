from django.shortcuts import render, redirect

from .models import UserAccount

# Create your views here.
def search_results(request, search_string):

    results = UserAccount.objects.filter(user__username__icontains=search_string)

    context = {
        'results': results,
    }
    return render(request, 'useraccounts/search_results.html', context)

def follow(request, useraccount_id):

    UserAccount.objects.get(user=request.user).follows.add(UserAccount.objects.get(id=useraccount_id))
    print('now following')
    return redirect(request.META['HTTP_REFERER'])

def unfollow(request, useraccount_id):

    UserAccount.objects.get(user=request.user).follows.remove(UserAccount.objects.get(id=useraccount_id))
    print('now following')
    return redirect(request.META['HTTP_REFERER'])
