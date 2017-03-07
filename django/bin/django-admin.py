#!/usr/bin/env python
import sys

from django.core import management

sys.path.append('/host/myown/newproj/')
import django
print django.VERSION

if __name__ == "__main__":
    management.execute_from_command_line()
