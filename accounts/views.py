from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm


# Create your views here.
def signup_view(request):
    form = UserChangeForm()
    return render(request, 'accounts/signup.html', {'form':form})
