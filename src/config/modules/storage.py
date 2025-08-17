from os import makedirs
from os.path import join

from config.base import BASE_DIR

# Ограничение размера данных POST до 3 ГБ (в байтах)
DATA_UPLOAD_MAX_MEMORY_SIZE = 3 * 1024 * 1024 * 1024  # 3 ГБ
# Порог для хранения файла в памяти (при превышении файла он будет сохраняться во временную директорию)
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5 МБ
# Используем обработчик, который сохраняет загружаемые файлы во временные файлы, а не в память
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]
FILE_UPLOAD_TEMP_DIR = join(BASE_DIR.parent, 'data', 'temp')
makedirs(FILE_UPLOAD_TEMP_DIR, exist_ok=True)

# Static | Media
STATICFILES_DIRS = [
    join(BASE_DIR, 'static')
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR.parent / 'static'
MEDIA_ROOT = BASE_DIR.parent / 'media'
