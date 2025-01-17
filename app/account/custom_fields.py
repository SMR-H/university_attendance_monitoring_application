from django.core.validators import validate_email
from django.db import models

class CaseInsensitiveEmailField(models.EmailField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(validate_email)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None:
            value = value.lower()
        return value

    # def from_db_value(self, value, expression, connection):
    #     return self.get_prep_value(value)

    # def to_python(self, value):
    #     return self.get_prep_value(value)

#########################


class CaseInsensitiveUsernameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None:
            value = value.lower()
        return value