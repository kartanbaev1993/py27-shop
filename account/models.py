from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, phone, **kwargs):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **kwargs)
        # self.model = User
        user.set_password(password) # heshirovanie parolya
        user.save(using=self._db) # sohranyaem usera v baze dannyh
        return user

    def create_superuser(self, email, password, phone, **kwargs):
        if not email:
            raise ValueError("Email is required")
        kwargs["is_staff"] = True
        kwargs["is_superuser"] = True
        kwargs["is_active"] = True
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **kwargs)
        # self.model = User
        user.set_password(password) # heshirovanie parolya
        user.save(using=self._db) # sohranyaem usera v baze dannyh
        return user


class User(AbstractUser):
    username = None # ubiraem username iz lyudei
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    bio = models.TextField()

    USERNAME_FIELD = 'email' # ukazyvaem kakoe pole ispol'zovat' pri logine
    REQUIRED_FIELDS = ['phone']

    objects = UserManager() # ukazyvaem novogo managera
