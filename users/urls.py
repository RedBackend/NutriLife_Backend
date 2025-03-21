from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserProfileView, VerifyEmailView

urlpatterns = [
    path('/register/', RegisterView.as_view(), name='register'),
    path('/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(route='/token/', view=TokenObtainPairView.as_view(), name='token_obtain'),
    path('/profile/', UserProfileView.as_view(), name='profile'),
    path('/verify-email/<uuid:token>/', VerifyEmailView.as_view(), name='verify-email'),
]