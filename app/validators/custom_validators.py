from django.core.exceptions import ValidationError
import re
def validate_only_digits(value):
    pattern = r'^[0-9]+$'
    if not re.match(pattern, value):
        raise ValidationError("Value must contain only English digits (0-9).")
    
def validate_semester_code(value):
    pattern = r'^\d{4}$'
    if not re.match(pattern, str(value)):
        raise ValidationError('Semester code must be a 4-digit integer using English numbers only.')

def validate_username(username):
    pattern = r'^[a-z0-9_]+$'
    if not re.match(pattern, username):
        raise ValidationError('Invalid username. Only lowercase letters, numbers, and underscores are allowed.')