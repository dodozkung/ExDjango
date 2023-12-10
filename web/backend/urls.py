from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from backend.views.index import IndexView
from backend.views.login import LoginView
from backend.views.logout import LogoutPage

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^$',IndexView,name='backend-index'),
    re_path(r'^login/$',LoginView,name='backend-login'),
    re_path(r'^logout/$',LogoutPage,name='backend-logout'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += history