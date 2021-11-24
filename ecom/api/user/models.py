from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_staffuser(self, email, password):
    #     """
    #     Creates and saves a staff user with the given email and password.
    #     """
    #     user = self.create_user(
    #         email,
    #         password=password,
    #     )
    #     user.staff = True
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):

    name = models.CharField(max_length=50, default='Anonymous')

    email = models.EmailField(max_length=254, unique=True)

    username = None

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()
    #
    # phone = models.CharField(max_length=20, blank=True, null=True)
    #
    # gender = models.CharField(max_length=10, blank=True, null=True)
    #
    session_token = models.CharField(max_length=10, default=0)
    #
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email
