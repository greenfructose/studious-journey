from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):

  class MembershipLevel(models.TextChoices):
    FREE = 'FR', _('Free')
    BRONZE = 'BR', _('Bronze')
    SILVER = 'SI', _('Silver')
    GOLD = 'GO', _('Gold')
    PLATINUM = 'PL', _('Platinum')
    CONTRIBUTOR = 'CO', _('Contributor')
    FOUNDER = 'FO', _('Founder')
  
  def get_membership_level(self) -> MembershipLevel:
    return self.MembershipLevel[self.membership_level]

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  membership_level = models.CharField(
    max_length=2,
    choices=MembershipLevel.choices,
    default=MembershipLevel.FREE,
    )

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

  def __str__(self):
    return self.user.username

