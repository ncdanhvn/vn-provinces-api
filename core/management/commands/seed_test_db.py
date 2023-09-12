from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import os


class Command(BaseCommand):
    help = 'Populates the database'

    def handle(self, *args, **options):        
        file_name = 'test_db.sql'
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, file_name)
        sql = Path(file_path).read_text(encoding='utf8')
        
        print(f'Populating the database with {file_name}...')
        with connection.cursor() as cursor:
            cursor.execute(sql)
