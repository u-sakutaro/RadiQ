from django.shortcuts import render


def signup(request):
    form = UserCreationForm()
    return render(request, 'user/signup.html', {'form':form})

