# Change the secret key! In your Django shell:
from django.utils.crypto import get_random_string


chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

print(get_random_string(50, chars))