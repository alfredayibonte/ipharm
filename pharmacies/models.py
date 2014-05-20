import re
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _


#users class
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


class MyUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """
    name = models.CharField(_('name'), max_length=100, blank=True)
    is_pharmacy_u = models.BooleanField(_('pharmacy_u'), default=False)
    is_pharmacy_su = models.BooleanField(_('pharmacy_su'), default=False)
    is_customer = models.BooleanField(_('customer'), default=False)
    location = models.CharField(_('location'), max_length=200, blank=True)
    mobile = models.CharField(_('mobile'), max_length=100, blank=True)
    address = models.CharField(_('address'), max_length=100, blank=True)
    images = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    last_visit = models.DateField(_('last_visit'), blank=True, null=True)
    note = models.CharField(_('note'), max_length=200, blank=True)
    username = models.CharField(_('username'), max_length=30, blank=True, unique=False,
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


#pharmacy class
class Pharmacy(models.Model):
    email = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    lat = models.CharField(max_length=200, blank=True)
    lng = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=200, blank=False, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(MyUser)

    def __str__(self):
        return self.name


# client class
class Client(models.Model):
    email = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=200, blank=False, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_activity = models.DateField(blank=True)
    note = models.CharField(max_length=200, blank=True)
    pharmacy = models.ForeignKey(Pharmacy)

