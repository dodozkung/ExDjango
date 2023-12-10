from django.shortcuts import render
from backend.forms.login import LoginForm
from django.contrib.auth import authenticate, login, logout
from backend.models.login import LoginHistory
from base.utils import get_client_ip,is_ajax
from django.http import JsonResponse

def LoginView(request):
    
    if request.method == 'POST' and is_ajax(request):
        form = LoginForm(request.POST)
        username = form.data['username']
        password = form.data['password']
        user = authenticate(username=username, password=password)
        
        if user is not None and (user.groups.filter(name='admin').exists() or user.is_superuser):
            if user.is_active:
                # sets the exp. value of the session
                remember = request.POST.get('remember',None)
                if remember is not None and remember == 'on':
                    request.session.set_expiry(86400)
                login(request, user)  # the user is now logged in

                LoginHistory.objects.create(
                    user=user,
                    status=1,
                    ip_address= get_client_ip(request)
                )
                return JsonResponse({
                    'message': 'บันทึกสำเร็จ',
                    'success': True
                },status=200)
        else:
            return JsonResponse({
                    'message': 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง',
                    'success': False
                },status=400)
    
    context = {
        "title": "Login"
    }
    
    return render(request, 'backend/layout/login.html', context)
