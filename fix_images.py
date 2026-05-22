import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamingproject.settings')
django.setup()

from gameapp.models import Post

# Map post slugs/title keywords to static image filenames
IMAGE_MAP = {
    'gta': 'gta-6.jpg',
    'elden': 'Elden-Ring.jpg',
    'god of war': 'god-of-war-4.jpg',
    'venom': 'venom.jpg',
    'batman': 'batman.jpg',
    'vice city': 'gta-6.jpg',
    'erdtree': 'Elden-Ring.jpg',
    'ps5': 'god-of-war-4.jpg',
    'crimson desert': 'crimson-desert.JPG',
    'naughty dog': 'lostofus2.jpg',
    'shadow of the erdtree': 'Elden-Ring.jpg',
    'spider': 'spiderman2.jpg',
    'cyberpunk': 'cyberpunk.jpg',
    'ghost': 'ghost-of-tsushima.jpg',
    'dead by daylight': 'dead-by-daylight.jpg',
    'rdr': 'rdr2.jpg',
    'resident evil': 'resident-evil-9.jpeg',
    'uncharted': 'uncharted.jpg',
    'last of us': 'lostofus2.jpg',
    'john wick': 'john wick.jpg',
    'infamous': 'infamous-second-son.jpg',
    'assassination': 'assassin-creed.jpg',
    'assassin': 'assassin-creed.jpg',
}

DEFAULT_IMAGE = 'gta-6.jpg'

posts = Post.objects.all()
updated = 0

for post in posts:
    if post.image_name:
        print(f'SKIP (already has image): {post.title[:50]}')
        continue

    title_lower = post.title.lower()
    assigned = None
    for keyword, img in IMAGE_MAP.items():
        if keyword in title_lower:
            assigned = img
            break

    if not assigned:
        assigned = DEFAULT_IMAGE

    post.image_name = assigned
    post.save()
    updated += 1
    print(f'UPDATED: {post.title[:50]} -> {assigned}')

print(f'\nDone! Updated {updated} posts.')
