#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamingproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamingproject.settings')
django.setup()

from gameapp.models import Post

posts_data = [
    {
        "title": "GTA VI: Vice City Reimagined",
        "category": "Breaking News",
        "image_name": "gta-6.jpg",
        "content": "Rockstar Games has finally revealed the first glimpses of Vice City in the upcoming GTA VI. The level of detail in the neon-soaked streets is unprecedented.",
        "author": "Lucia"
    },
    {
        "title": "Elden Ring: Shadow of the Erdtree",
        "category": "Epic Review",
        "image_name": "elden-ring.jpg",
        "content": "The Lands Between just got bigger. We explore the massive new bosses and the vertical world design of the Land of Shadow.",
        "author": "Miquella"
    },
    {
        "title": "Batman: Night in Gotham",
        "category": "Game Profile",
        "image_name": "batman.jpg",
        "content": "Step back into the cape and cowl. We examine the enduring legacy of the Arkham series and why Gotham remains so atmospheric.",
        "author": "Bruce Wayne"
    }
]

for data in posts_data:
    Post.objects.get_or_create(
        title=data["title"],
        defaults={
            "category": data["category"],
            "image_name": data["image_name"],
            "content": data["content"],
            "author": data["author"]
        }
    )

print("Check complete! Your database is now populated.")
