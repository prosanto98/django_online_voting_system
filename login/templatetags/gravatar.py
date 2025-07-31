import hashlib
from django import template

register = template.Library()

@register.filter
def gravatar_url(email, size=42):
    if not email:
        return f"https://www.gravatar.com/avatar/?s={size}&d=mp"
    email = email.strip().lower()
    hash_email = hashlib.md5(email.encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{hash_email}?s={size}&d=identicon"
