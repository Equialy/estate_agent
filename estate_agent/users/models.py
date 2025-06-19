from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from .manager import MyUserManager

# Create your models here.

class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=50, verbose_name="username", null=True, blank=False, unique=True)

    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Профиль пользователя {self.username}"

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user_profile"
        verbose_name = "Профиль менеджера"
        verbose_name_plural = "Профили менеджеров"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin