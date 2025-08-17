from config.base import DEV

MIDDLEWARE = [
    'adjango.middleware.IPAddressMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]
if DEV: MIDDLEWARE.append('adjango.middleware.MediaDomainSubstitutionJSONMiddleware')
if not DEV: MIDDLEWARE.append('silk.middleware.SilkyMiddleware')
