from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        UserModel = User
        if email is None:
            return
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
