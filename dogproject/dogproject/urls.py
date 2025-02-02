# dogproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Root URL path logic to handle the redirection
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('dogapp.urls')),  # Include dogapp URLs under accounts

    # Redirect user to login page if not logged in
    path('', lambda request: redirect(settings.LOGIN_URL) if not request.user.is_authenticated else redirect('random_dog')),
]
