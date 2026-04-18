import os
import django

# 1. Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamingproject.settings')
django.setup()

# 2. Import models
from gameapp.models import Post

# 3. Your original articles from the old design
posts_data = [
    {
        "title": "VICE CITY REBORN: GTA VI LEAKS REVEAL DYNAMIC WEATHER SYSTEM",
        "category": "Breaking News",
        "image_name": "gta-6.jpg",
        "content": "Step into the high-octane world of cybernetic warfare. Limited edition skins available now. Rockstar Games has finally revealed the first glimpses of Vice City in the upcoming GTA VI. The level of detail in the neon-soaked streets and dynamic weather systems is unprecedented. Expect a massive map that feels more alive than any previous simulation.",
        "author": "Rockstar"
    },
    {
        "title": "Shadow of the Erdtree: Exploring the Land of Shadow",
        "category": "DLC REVIEW",
        "image_name": "Elden-Ring.jpg",
        "content": "Miquella's journey continues in what is being hailed as the most challenging expansion in history. The Shadow of the Erdtree expansion brings a new level of challenge and beauty to the Lands Between. With over 10 new major bosses and a vertical world design, FromSoftware has once again redefined the RPG genre.",
        "author": "Miquella"
    },
    {
        "title": "PS5 Pro: Is the Mid-Gen Upgrade Worth Your Credits?",
        "category": "HARDWARE",
        "image_name": "john wick.jpg",
        "content": "We benchmark the latest hardware against the most demanding titles of the year. With enhanced ray tracing and AI upscaling, the Pro version promises 60FPS at 4K resolution, but at a premium price point. Is it the right choice for you?",
        "author": "Sony Tech"
    },
    {
        "title": "The Crimson Desert of Solo Competitive: Shifting Trends in 2026",
        "category": "ESPORTS",
        "image_name": "crimson-desert.JPG",
        "content": "Why individual performance is becoming the focus of major tournament circuits. As team dynamics shift, we analyze the rise of solo stars across the competitive landscape and what it means for the future of professional gaming.",
        "author": "Esport Insider"
    },
    {
        "title": "10 Years of Naughty Dog: A Retrospective",
        "category": "CULTURE",
        "image_name": "lostofus2.jpg",
        "content": "Looking back at the studio that redefined cinematic storytelling in games. From Uncharted to The Last of Us, Naughty Dog has consistently pushed the boundaries of emotional depth and technical excellence in the industry.",
        "author": "Naughty Dog"
    }
]

print("--- Restoring Original Design Content ---")

# Clear current posts if you want a clean slate
# Post.objects.all().delete()

for data in posts_data:
    post, created = Post.objects.get_or_create(
        title=data["title"],
        defaults={
            "category": data["category"],
            "image_name": data["image_name"],
            "content": data["content"],
            "author": data["author"]
        }
    )
    if created:
        print(f"Restored: {post.title}")
    else:
        print(f"Skipped (Already exists): {post.title}")

print("\n--- Restore Complete! Check your Blog page now. ---")
