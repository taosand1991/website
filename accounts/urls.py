
from django.urls import path, include
from accounts import views


urlpatterns = [


        path('Registration/', views.sign_up, name='register'),
        path('profile/', views.profile_page, name='profile'),
        path('profile/edit', views.profile_update, name='edit'),
        path('profile/edit/change-password', views.password_change, name='password'),
        path('accounts/', include('django.contrib.auth.urls')),






]