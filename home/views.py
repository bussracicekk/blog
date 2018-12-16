from django.shortcuts import render, HttpResponse


def home_view(request):
    if request.user.is_authenticated:
        context = {
            'user': 'Büşra',
        }
    else:
        context = {
            'user': 'Guest',
        }
    return render(request, 'home.html', context)
