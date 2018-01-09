"""
Django settings for euth_wagtail project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import ugettext_lazy as _

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.contrib.wagtailstyleguide',
    'wagtail.contrib.settings',

    'modelcluster',
    'taggit',
    'widget_tweaks',
    'easy_thumbnails',
    'parler',
    'ckeditor',
    'ckeditor_uploader',
    'background_task',

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'rest_framework',
    'autofixture',
    'rules.apps.AutodiscoverRulesConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'micawber.contrib.mcdjango',

    'adhocracy4.images.apps.ImagesConfig',
    'adhocracy4.phases.apps.PhasesConfig',
    'adhocracy4.projects.apps.ProjectsConfig',
    'adhocracy4.ratings.apps.RatingsConfig',
    'adhocracy4.reports.apps.ReportsConfig',
    'adhocracy4.modules.apps.ModulesConfig',
    'adhocracy4.categories.apps.CategoriesConfig',
    'adhocracy4.comments.apps.CommentsConfig',
    'adhocracy4.maps.apps.MapsConfig',
    'adhocracy4.filters.apps.FiltersConfig',
    'adhocracy4.rules.apps.RulesConfig',

    'euth.users.apps.UsersConfig',
    'euth.actions.apps.ActionsConfig',
    'euth.organisations.apps.OrganisationsConfig',
    'euth.projects.apps.ProjectsConfig',
    'euth.ideas.apps.IdeaConfig',
    'euth.dashboard.apps.DashboardConfig',
    'euth.memberships.apps.MembershipsConfig',
    'euth.documents.apps.DocumentConfig',
    'euth.flashpoll.apps.FlashpollConfig',
    'euth.maps.apps.MapConfig',
    'euth.follows.apps.FollowsConfig',
    'euth.offlinephases.apps.OfflinephaseConfig',
    'euth.blueprints.apps.BlueprintsConfig',
    'euth.contrib',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'euth.contrib.middleware.TimezoneMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'euth_wagtail.urls'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'euth_wagtail.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
        }
    }
}


# Auth
# https://docs.djangoproject.com/en/1.8/topics/auth/customizing/

AUTH_USER_MODEL = 'euth_users.User'

AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = 'username'
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink']
        ]
    },
    'image-editor': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Image'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink']
        ]
    }
}

BLEACH_LIST = {
    'default' : {
        'tags': ['p','strong','em','u','ol','li','ul','a'],
        'attributes': {
            'a': ['href', 'rel'],
        },
    },
    'image-editor': {
        'tags': ['p','strong','em','u','ol','li','ul','a','img'],
        'attributes': {
            'a': ['href', 'rel'],
            'img': ['src', 'alt', 'style']
        },
        'styles': [
            'float',
            'margin',
            'padding',
            'width',
            'height',
            'margin-bottom',
            'margin-top',
            'margin-left',
            'margin-right',
        ],
    }
}

MICAWBER_PROVIDERS = 'euth.contrib.oembed.oembed_providers'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('de', _('German')),
    ('it', _('Italien')),
    ('fr', _('French')),
    ('sv', _('Swedish')),
    ('sl', _('Slovene')),
    ('da', _('Danish')),
    ('el', _('Greek')),
    ('ka', _('Georgian')),
    ('mk', _('Macedonian')),
]

PARLER_LANGUAGES = {
    1:[{'code': language_code } for language_code, language in LANGUAGES]
}

# fixtures

FIXTURE_DIRS = [ os.path.join(PROJECT_DIR, 'fixtures') ]
FILE_ALIASES  = {
    '*': {
        'fileformats': (
            ('.png', 'image/png'),
            ('.jpeg', 'image/jpeg'),
            ('.pdf', 'application/pdf'),
            ('.doc', 'application/msword'),
            ('.docx', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'),
            ('.txt', 'text/plain'),
            ('.md', 'text/markdown'),
            ('.xls', 'application/msexcel'),
            ('.xlsx', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
            ('.ppt', 'application/mspowerpoint')
        )
    }
}
IMAGE_ALIASES = {
    '*': {
        'max_size': 5*10**6,
        'fileformats': ('image/png', 'image/jpeg', 'image/gif')
    },
    'heroimage': {'min_resolution': (1300, 600)},
    'logo': {'min_resolution': (200, 200), 'aspect_ratio': (1, 1)},
    'avatar': {'min_resolution': (200, 200)},
    'idea_image': {'min_resolution': (800, 200)},
    'tileimage': {},
}

THUMBNAIL_ALIASES = {
    '': {
        'heroimage': {'size': (1500, 500), 'crop': 'smart'},
        'heroimage_preview': {'size': (880, 220), 'crop': 'smart'},
        'project_thumbnail': {'size': (520, 330), 'crop': 'smart'},
        'idea_image': {'size': (800, 0), 'crop': 'scale'},
        'idea_thumbnail': {'size': (240, 240), 'crop': 'smart'},
        'map_thumbnail': {'size': (400, 200), 'crop': 'smart'},
        'organisation_thumbnail': {'size': (740, 540), 'crop': 'smart'},
        'avatar_small': {'size': (60, 60), 'crop': 'smart'},
        'org_avatar_small': {'size': (60, 60), 'crop': 'scale'},
        'org_avatar_medium': {'size': (200, 200), 'crop': 'scale'},
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'node_modules/flatpickr/dist'),
    os.path.join(BASE_DIR, 'node_modules/leaflet/dist'),
    os.path.join(BASE_DIR, 'node_modules/leaflet-draw/dist'),
    os.path.join(BASE_DIR, 'node_modules/typeahead.js/dist'),
    os.path.join(BASE_DIR, 'node_modules/highcharts/js'),
    os.path.join(BASE_DIR, 'node_modules/highcharts/css'),
    os.path.join(PROJECT_DIR, 'static'),
    os.path.join(PROJECT_DIR, 'static/bundles'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

EMAIL_SUBJECT_PREFIX = '[OPIN] '

# Wagtail settings

WAGTAIL_SITE_NAME = "euth_wagtail"

# Authentification

LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_ADAPTER = 'euth.users.adapters.EuthAccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = EMAIL_SUBJECT_PREFIX
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_FORM_CLASS = 'euth.users.forms.SignUpForm'
ACCOUNT_USER_DISPLAY = 'euth.users.services.account_user_display'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300  # seconds
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_EMAIL_VERIFICATION = False

# Rest framework

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

ACTIONABLE = [
    ('euth_ideas', 'Idea'),
    ('a4comments', 'Comment')
]

FLASHPOLL_URL = "https://opin.flashpoll.eu/"
FLASHPOLL_BACK_URL = "http://backend.flashpoll.eu/flashpoll/api/v7/management"
FLASHPOLL_BACK_USER = "fp_management"
FLASHPOLL_BACK_PASSWORD = "53c4100e8ab143fe59fcb2e743cf4aba662ad25lacab0eb37fb9c69d8f27363fa19f0531bd681"
GOOGLE_API_KEY = "AIzaSyC8kq3VbEzLA1xqe0ItRk-y4bgAg89h4Qc"

A4_MAP_ATTRIBUTION = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
A4_MAP_BASEURL = 'https://{s}.tile.openstreetmap.org/'
A4_MAP_BOUNDING_BOX = [
    [[34.95799531086792,-28.388671875],
     [71.35706654962706,-28.388671875],
     [71.35706654962706,50.88867187499999],
     [34.95799531086792,50.88867187499999],
     [34.95799531086792,-28.388671875]]
]

# Adhocracy4

A4_ORGANISATIONS_MODEL = 'euth_organisations.Organisation'

A4_COMMENTABLES = (
    ('euth_ideas', 'idea'),
    ('euth_maps', 'mapidea'),
    ('euth_documents', 'paragraph'),
    ('euth_documents', 'document'),
    ('a4comments', 'comment'),
)

A4_RATEABLES = (
    ('euth_ideas', 'idea'),
    ('euth_maps', 'mapidea'),
    ('a4comments', 'comment'),
)

A4_REPORTABLES = (
    ('euth_ideas', 'ideas'),
    ('euth_maps', 'mapidea'),
    ('a4comments', 'comment'),
)
