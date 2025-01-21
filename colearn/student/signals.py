from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from .models import Profile, User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a profile for the user when the user is created."""
    user = instance

    if created:
        print('Profile created')
        Profile.objects.create(
            user=user,
            )
    else:
        print('Profile already exists')

print("Signal module loaded")  # Add this line to verify the signal module is loaded