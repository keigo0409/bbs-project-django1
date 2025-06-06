import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

django.setup()

from django.core.management import call_command
from django.contrib.auth.models import get_user_model
from django.db import OperationalError

User = get_user_model()

try:
    call_command('migrate',interactive=False)
except OperationalError as e:
    print(f"Migrate error: {e}")
    pass

if not User.objects.filter(username=SUPERUSER_NAME).exists():
    User.objects.create_superuser(
        username=SUPERUSER_NAME,
        email=SUPERUSER_EMAIL,
        password=SUPERUSER_PASSWORD,
    )
