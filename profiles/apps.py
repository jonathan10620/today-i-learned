from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = "profiles"
    default_auto_field = "django.db.models.AutoField"


from allauth.account.apps import AccountConfig
from allauth.socialaccount.apps import SocialAccountConfig


class ModifiedAccountConfig(AccountConfig):
    default_auto_field = "django.db.models.AutoField"


class ModifiedSocialAccountConfig(SocialAccountConfig):
    default_auto_field = "django.db.models.AutoField"
