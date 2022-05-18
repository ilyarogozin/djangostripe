import json

from django.core.management.base import BaseCommand

from payments.models import Item


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--path', help='file path', type=str)

    def handle(self, *args, **options):
        file_path = options['path']

        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                Item.objects.create(
                    name=item['name'],
                    description=item['description'],
                    price=item['price']
                )
