from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from bbs.views import custom_permission_denied_view

handler403 = custom_permission_denied_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbs/', include('bbs.urls')),
    path('', RedirectView.as_view(url='/bbs/')),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
