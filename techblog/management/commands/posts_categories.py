from typing import Any
from techblog.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data 
        Category.objects.all().delete()
        
        categories = ['Sports', 'Technology', 'Science', 'Art', 'AI']
      
        for category_name in categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))