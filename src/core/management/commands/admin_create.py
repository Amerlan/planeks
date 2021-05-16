from django.conf import settings
from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = settings.ADMIN_USERNAME
        email = ''
        password = settings.ADMIN_PASSWORD
        admin = User.objects.create_superuser(email=email, username=username, password=password)
        admin.is_active = True
        admin.is_admin = True
        admin.save()
        print('Admin created')
