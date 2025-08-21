# core/services/user/mixer.py
import string
from random import choices
from typing import TYPE_CHECKING

from adjango.services.base import ABaseService
from adjango.utils.base import calculate_age

from utils.common import get_full_name

if TYPE_CHECKING:
    from apps.core.models.user import User


class UserService(ABaseService):
    def __init__(self, obj: 'User'):
        super().__init__(obj)
        self.user = obj

    @property
    def age(self): return calculate_age(self.user.birth_date)

    @property
    def full_name(self): return get_full_name(self.user)

    @staticmethod
    def generate_random_username():
        return 'U' + ''.join(choices(
            string.ascii_uppercase + string.digits, k=11
        ))
