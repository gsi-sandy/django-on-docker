from django.core.management.base import BaseCommand
from django.core import mail
from ...models import User
from decouple import config
import sys


class Command(BaseCommand):
    help = 'Create a super user'

    def handle(self, *args, **options):
        print("Enter first name")
        first_name = input()

        print("Enter last name")
        last_name = input()

        print("Enter email")
        email = input()

        print("Enter password")
        password = input()

        print("Confirm password")
        password_confirm = input()

        if first_name == "":
            self.stdout.write(self.style.ERROR(
                'Fist name is empty'
            ))
            exit(0)

        if last_name == "":
            self.stdout.write(self.style.ERROR(
                'Last name is empty'
            ))
            exit(0)

        if email == "":
            self.stdout.write(self.style.ERROR(
                'Email is empty'
            ))
            exit(0)

        if password == "":
            self.stdout.write(self.style.ERROR(
                'Password is empty'
            ))
            exit(0)

        if password != password_confirm:
            self.stdout.write(self.style.ERROR(
                'Password do not match'
            ))
            exit(0)

        try:
            user = User()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.set_password(password)

            user.is_active = True
            user.is_superuser = True
            user.is_staff = True

            # user.save()

        except:
            self.stdout.write(self.style.ERROR(
                'Failed super user creation'
            ))
            exit(0)

        try:
            mail.send_mail(
                'Email de prueba',
                'Here is the message.',
                config('EMAIL_HOST_USER'),
                ['sgsantos@nauta.cu', 'adielys91@nauta.cu'],
                fail_silently=False,
            )

        except:
            self.stdout.write(self.style.ERROR(
                sys.exc_info()
            ))
            exit(0)

        self.stdout.write(self.style.SUCCESS(
            'Super user was created successfully'
        ))



