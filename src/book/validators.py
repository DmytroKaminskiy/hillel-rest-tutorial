from datetime import datetime

from django.core.exceptions import ValidationError


def year_validator(value):
    if value > datetime.now().year:
        raise ValidationError(
            '%(value)s is not a correct year!',
            params={'value': value},
        )


def date_should_be_in_past_validator(value):
    if value > datetime.now().date():
        raise ValidationError(
            '%(value)s should be in past!',
            params={'value': value},
        )
