# Django settings for river project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
LOCAL_DEVELOPMENT = True
PATH = '/Users/eboyer/Sites/River/'
INTERNAL_IPS = ('127.0.0.1',)
	
DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = PATH+'data.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
)


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PATH+'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bmp)bztfe)ngy3!kp$()z7)nyo=n%f44i(pi%u^&!l9d0lof*4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'userprofile.middleware.UserProfileMiddleware',
)

ROOT_URLCONF = 'River.urls'

TEMPLATE_DIRS = (PATH+'templates/')

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.markup',
	'post',
	'project',
	'userprofile',
	'django_extensions',
)

# Authentication
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/user/login'
AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

#Email Testing: python -m smtpd -n -c DebuggingServer localhost:1025
ACCOUNT_ACTIVATION_DAYS = 2

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'testing@example.com'