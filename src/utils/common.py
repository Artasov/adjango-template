# utils/common.py
from typing import Any, Generator, TYPE_CHECKING

from django.apps import apps

if TYPE_CHECKING:
    from apps.core.models.user import User


def get_full_name(user: 'User') -> str:
    """
    Возвращает полное имя пользователя в формате "Фамилия Имя".
    Если first_name отсутствует, возвращается только фамилия.
    Если last_name отсутствует, возвращается только имя.
    Если ни имя, ни фамилия не заданы, возвращается username.
    """
    # Если заданы и фамилия, и имя
    if getattr(user, 'last_name', None) and getattr(user, 'first_name', None):
        full_name = f"{user.last_name} {user.first_name}"
        return full_name

    # Если задана только фамилия
    if getattr(user, 'last_name', None):
        return user.last_name

    # Если задано только имя
    if getattr(user, 'first_name', None):
        return user.first_name

    # Если ни имя, ни фамилия не заданы — возвращаем username
    return getattr(user, 'username', '')


def get_models_list() -> Generator[str, Any, None]:
    """
    Функция возвращает список строк вида 'app.Model' для всех зарегистрированных моделей.
    """
    models = apps.get_models()
    return (f'{model._meta.app_label}.{model.__name__}' for model in models)  # noqa
