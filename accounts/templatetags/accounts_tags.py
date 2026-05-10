from django import template
from accounts.models import Profile

register = template.Library()

@register.simple_tag
def get_user_role(user):
    try:
        profile = Profile.objects.get(user=user)
        return profile.role
    except Profile.DoesNotExist:
        return 'student'  # Default to student if no profile exists