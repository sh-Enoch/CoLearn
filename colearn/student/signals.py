from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
# from django.contrib.auth.models import User
from .models import Profile, User
from allauth.account.models import EmailAddress

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
    #update allauth emailaddress if exists
        try:
            email_address = EmailAddress.objects.get_primary(user)
            if email_address.email != user.email:
                email_address.email = user.email
                email_address.verified = False
                email_address.save()

        except:
            #object doesn't exist.
            EmailAddress.objects.create(
                user = user,
                email = user.email,
                primary = True,
                verified = False
            )




@receiver(pre_save, sender=User)
def user_presave(sender, instance, **kwargs):
    """"converts usename to lowercase before saving"""
    if instance.username:
        instance.username = instance.username.lower()
