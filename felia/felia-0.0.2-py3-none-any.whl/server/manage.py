#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    BASE_DIR = Path(__file__).resolve().parent.parent
    sys.path.append(BASE_DIR.as_posix())
    try:
        execute_from_command_line(sys.argv)
    except Exception as err:
        from tkinter.messagebox import showerror
        import traceback
        traceback.print_exc()
        showerror(__file__, str(err))


if __name__ == '__main__':
    main()
