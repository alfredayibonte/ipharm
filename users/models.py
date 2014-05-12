import re
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
# from django.dispatch.dispatcher import receiver
# from django_facebook.models import FacebookModel
# from django.db.models.signals import post_save
# from django_facebook.utils import get_user_model, get_profile_model
# from ipharmProject import settings

# class MyCustomProfile(FacebookModel):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
# @receiver(post_save)
# def create_profile(sender, instance, created, **kwargs):
#     """Create a matching profile whenever a user object is created."""
#     if sender == get_user_model():
#         user = instance; profile_model = get_profile_model()
#         if profile_model == MyCustomProfile and created:
#             profile, new = MyCustomProfile.objects.get_or_create(user=instance)


#Customer user
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)


class Customer(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """
    is_pharmacy = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)
    mobile = models.CharField(max_length=100)
    address = models.CharField(_('address'), max_length=100, blank=True)
    images = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

<<<<<<< HEAD
    username = models.CharField(_('username'), max_length=30, unique=True,
=======
    username = models.CharField(_('username'), max_length=30, blank=True, unique=True,
>>>>>>> ec65e5038f38012b5edd77711d18ca082d3a7d42
                                help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                                            '@/./+/-/_ characters'),
                                validators=[
                                    validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'),
                                                              'invalid')
                                ])
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        # TODO: use reverse "/users/%s/" % urlquote(self.username)
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        #"Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])