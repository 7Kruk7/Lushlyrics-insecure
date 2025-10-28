from django.contrib import admin
from django.urls import path, include
from main import views
from django.contrib.auth import views as auth_views # added

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # added
    path('signup/', views.registration, name='registration'), # added 
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            #template_name='registration/password_reset.html',
            html_email_template_name='registration/email.html',
            subject_template_name='registration/subject.txt',
        ),
        name='password_reset'
    ),# added
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), # added
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), # added
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), # added
]