from django.core.mail import send_mail
from django.conf import settings


def send_verification_email(user, verification_token):
    """Send an email verification link to the user"""
    verification_link = f"http://{settings.SITE_DOMAIN}/api/users/verify-email/{verification_token}/"

    subject = "Verify your email for Muscle Nutrition App"
    message = f"""
    test
    """

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # Use DEFAULT_FROM_EMAIL here
        [user.email],
        fail_silently=False,
    )