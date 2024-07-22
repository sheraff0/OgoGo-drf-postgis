from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailOrUsernameModelBackend(BaseBackend):
    """
    This is a ModelBacked that allows authentication
    with either a username or an email address.
    
    """
    User = get_user_model()

    @classmethod
    def obtain_user(cls, username, key="username"):
        try:
            return cls.User.objects.get(**{key: username})
        except: ...

    def authenticate(self, request, username=None, password=None):

        if '@' in username:
            user = self.obtain_user(username.lower(), key="email") or \
                self.obtain_user(username)
        else:
            user = self.obtain_user(username)
        try:
            if user.check_password(password):
                return user
        except: ...

    def get_user(self, user_id):
        return self.obtain_user(user_id, key="pk")
