from .base import *  # noqa:F403

DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
]

INSTALLED_APPS += [  # noqa:F405
        'debug_toolbar',
        'silk',
    ]

MIDDLEWARE += [  # noqa:F405
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'silk.middleware.SilkyMiddleware',
    ]

# Silk
SILKY_AUTHENTICATION = True

SILKY_AUTHORISATION = True

SILKY_PERMISSIONS = lambda user: user.is_superuser  # noqa:E731
