from datetime import timedelta

from config.base import DOMAIN_URL, MAIN_DOMAIN, DEV

USER_AGENTS_CACHE = 'default'
APPEND_SLASH = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_TRUSTED_ORIGINS = [
    DOMAIN_URL,
]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
ALLOWED_HOSTS = [
    'localhost',
    'web',
    MAIN_DOMAIN,
]
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60 * 24 * 2 if DEV else 60 * 24 * 2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:3000',
]
