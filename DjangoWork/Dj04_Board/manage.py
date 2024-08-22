#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from utils.Database import Database

def main():
    """database"""
    conn = Database('board.sqlite3')
    conn.connect()
    conn.createTable()
    conn.close()


    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dj04_Board.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
