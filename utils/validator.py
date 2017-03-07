__author__ = "Anto.s"

import re
import operator

class DataValidator(object):

    def __init__(self, config, *args, **kwargs):
        self.config = config
        self.err_msg =''
        self._type_map = {'numeric': self.is_numeric, 'alpha': self.is_alpha,
                        'alphanumeric': self.is_alphanumeric, 'normal': self.is_normal,
                        'datetime': self.is_normal,
                        }

    def _pat_match(self, value, pattern):
        if re.match(pattern, value):
            return True
        return False

    def is_normal(self, value):
        """Not Yet implemented"""
        return True

    def is_numeric(self, value):
        """validates the numeric type """
        pattern = "[0-9]*$"
        return self._pat_match(value, pattern)

    def is_alpha(self, value):
        """validates the numeric type """
        pattern = "[A-Za-z]*$"
        return self._pat_match(value, pattern)

    def is_alphanumeric(self, value):
        """validates the numeric type """
        pattern = "[0-9A-Za-z]*$"
        return self._pat_match(value, pattern)

    def validate_type(self, value):
        """validates based on the type of the data"""
        handler_func = self._type_map.get(self.config.get('type', 'normal'))
        if not handler_func(value):
            self.err_msg = "%s must be a %s value"%(self.config.get('name'), self.config.get('type'))
            return False
        return True

    def validate_pattern(self, value):
        """validates the value with current pattern if present
        """
        if not self.config.get('pattern'):
            #No need to validate pattern
            return True
        if not self._pat_match(value, self.config.get('pattern')):
            self.err_msg = "%s is not in valid format"%self.config.get('name')
            return False
        return True

    def check_mandatory(self, value):
        """Decides whether a field is to be validated or not
        """
        if self.config.get('required', False) or value:
            return True
        return False

    def validate(self, value):
        """Strict validation with the given config """
        self.err_msg = ''
        if not self.check_mandatory(value):
            #return None, need not to be validated
            return self.err_msg
        if value and self.validate_type(value) and self.validate_pattern(value):
            #validation passed
            pass
        if not value:
            self.err_msg = "%s must be required"%self.config.get('name')
        return self.err_msg #if none, there is no error


