import os
import django
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
    User = get_user_model()
    if not User.objects.filter(is_superuser=True).exists():
        import os
        username=os.environ.get('DJANGO_SUPERUSER_NAME')
        email=os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password=os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        User.objects.create_superuser(username=username,email=email,password=password)
except OperationalError as e:
    print(f"Migrate error: {e}")

application = get_wsgi_application()
