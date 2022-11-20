from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, username, password, email, fn=None):
        user = self.model(username=username, email=self.normalize_email(email), fn=fn)
        user.set_password(password)
        user.is_active = user.is_staff = user.is_superuser = False
        user.save()
        return user

    def create_superuser(self, username, password, email, fn=None):
        user = self.model(username=username, email=self.normalize_email(email), fn=fn)
        user.set_password(password)
        user.is_active = user.is_staff = user.is_superuser = True
        user.save()
        return user



class Account(AbstractBaseUser):
    fn = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, blank=False)
    email = models.CharField(max_length=256, unique=True, blank=False)
    # password = models.CharField(max_length=20, )
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]  # contact means email or phone number
    objects = AccountManager()
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)  # if you are an active and busy member of the site
    is_staff = models.BooleanField(default=False)

    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_superuser

    def has_module_perms(self, perm, obj=None):
        return self.is_superuser and self.is_active

    def __str__(self):
        return self.username
    
