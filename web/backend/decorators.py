from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import resolve
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def superuser_authenticate_required(function):
    def wrap(request, *args, **kwargs):
    	if not request.user.is_authenticated or not request.user.is_superuser  :
            logout(request)
            return HttpResponseRedirect(reverse('backend-login'))
    	return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
