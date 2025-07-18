#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    #! This is not from the Tutorial
    # The main() function runs when the manage script runs
    # so this ensures that SECRET_KEY in mysite/settings.py is loaded
    # i'm not sure if there's any better file path to add this line.
    load_dotenv()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            """Couldn't import Django. Are you sure it's installed and
            available on your PYTHONPATH environment variable? Did you
            forget to activate a virtual environment?"""
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
