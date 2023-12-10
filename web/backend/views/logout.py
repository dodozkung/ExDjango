from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse

def LogoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse('backend-login'))