"""
Django command to wait for the database to be availabe.
"""
import time

from psycopg2 import OperationalError as Pycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("Waiting for database...\n")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Pycopg2OpError, OperationalError):
                self.stdout.write(
                    "Database unavailable, waiting 1 second...\n"
                    )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!\n"))
