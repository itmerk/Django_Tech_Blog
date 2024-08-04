from typing import Any
from techblog.models import Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data 
        Category.objects.all().delete()

        categories = ['AI', 'New Innovation', 'Launches', 'Tech Events', 'Problems']

        for category_name in categories:
            #category = random.choice(categories)
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))