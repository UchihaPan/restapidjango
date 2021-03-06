from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
import time


class command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('waiting for its start')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('waiting')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))
