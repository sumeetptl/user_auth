from django.urls import path, include
# from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from account.views import UserRegisterationView, UserLoginView, UserProfileView

urlpatterns = [
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # Optional UI:
    # path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('register/',UserRegisterationView.as_view(), name="Registeration" ),
    path('login/',UserLoginView.as_view(), name="Login" ),
    path('profile/',UserProfileView.as_view(), name="Profile"),
    # path('change_password/',UserChangePassword.as_view(), name="Change_Password"),
    # path('reset_password_email/',SendPasswordResetEmailView.as_view(), name="Send_Email"),
    # path('reset_password/<str:uid>/<str:token>/',ResetPasswordView.as_view(), name="Reset Password"),
    # path('activate/<str:uid>/<str:token>/',ActivateView.as_view(), name="Activate")
    
]
