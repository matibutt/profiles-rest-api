from django.db import models

#import Base frm AbstractBaseUser i.e. Base for our django models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

#it allows us to give permission to our different user for accessing.

#we have to tell to django how we use our object for UserProfileManager
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user models."""

    def creat_user(self, email, name, password=None):
        """Creats a new user profile object"""
        if not email:
            raise ValueError('Users must have an Email address')

            email = self.normalize_email(email)
            user = self.model(email=email, name= name)

            user.set_password(password)
            user.save(using=self._db)

            return user

        def create_superuser(self, email, name, password):
            """Creates and servers a new superuser with given details"""

            user = self.create_user(email, name, password)

            user.is_superuser = True
            user.is_staff = True

            user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represnts a "UserProfile" inside our system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """Used to get user full name."""

        return self.name

    def get_short_name(self):
        """Used to get user short name"""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email
