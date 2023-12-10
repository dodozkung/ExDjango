from django.shortcuts import render
from backend.decorators import superuser_authenticate_required

@superuser_authenticate_required
def IndexView(request):
    
    context = {
        "title": "หน้าแรก"
    }
    
    return render(request, 'dashboard/index.html', context)
