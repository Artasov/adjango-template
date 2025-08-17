# core/models/user.py

from adjango.models.base import AAbstractUser
from django.db.models import (
    CharField, BooleanField,
    EmailField, DateField
)
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit
from timezone_field import TimeZoneField

from apps.core.managers.user import UserManager
from apps.core.services.user.base import UserService
from utils.pictures import CorrectOrientation


class User(AAbstractUser):
    service_class = UserService
    objects = UserManager()

    email = EmailField(_('Email'), blank=True, null=True, db_index=True)
    middle_name = CharField(_('Middle name'), max_length=150, blank=True)
    birth_date = DateField(_('Birth date'), null=True, blank=True)
    avatar = ProcessedImageField(
        verbose_name=_('Avatar'), upload_to='user/images/avatar/',
        processors=(ResizeToFit(500, 500), CorrectOrientation()),
        format='JPEG', options={'quality': 70}, null=True, blank=True
    )
    timezone = TimeZoneField(verbose_name=_('Timezone'), default='UTC')
    is_email_confirmed = BooleanField(_('Is email confirmed'), default=False)
    is_test = BooleanField(_('Is test'), default=False)

    def __str__(self): return self.service.full_name

    def save(self, *args, **kwargs):
        if not self.username: self.username = self.service.generate_random_username()
        super().save(*args, **kwargs)
