from django.core.exceptions import ValidationError

def validate_only_digits(value):
    if not value.isdigit():
        raise ValidationError("Value must contain only digits.")