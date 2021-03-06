from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )


def validation_number(value):
    number = value
    if ".edu" in number:
        raise ValidationError("It is not a valid number")

