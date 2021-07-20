from django_extensions.management.jobs import DailyJob
from user.models import User
from placement.models import Placement
from intern.models import Intern
from django.utils import timezone
from src.settings_email import (
    EMAIL_BODY,
    EMAIL_HOST_USER,
    EMAIL_SUBJECT,
)
from django.core.mail import send_mail

class Job(DailyJob):
    help = "Daily Mailer"

    def execute(self):
        self.placementMailer()
        self.internMailer()

    def placementMailer(self):
        users = User.objects.all()
        for user in users:
            count = 0
            placements = Placement.objects.all()
            email_body = """NAME\tCOMPANY\tROLE\n"""
            for placement in placements:
                time_difference = placement.deadline - timezone.now()
                if time_difference.total_seconds() <= 86500:
                    if placement in user.placements_applied_for.all():
                        placement_data = f"""{placement.placement_name}\t{placement.company}\t{placement.role}\n"""
                        email_body = email_body+placement_data
                        count = count+1
                        print(time_difference.total_seconds())
            if count != 0:
                sender = EMAIL_HOST_USER
                recipient = user.email
                name = user.name 
                subject = EMAIL_SUBJECT["PlacementMailer"]
                body = EMAIL_BODY["PlacementMailer"].format(name=name, body=email_body)
                send_mail(subject, body, sender, [recipient], fail_silently=False)

    def internMailer(self):
        users = User.objects.all()
        for user in users:
            count = 0
            interns = Intern.objects.all()
            email_body = """NAME\tCOMPANY\tROLE\n"""
            for intern in interns:
                time_difference = intern.deadline - timezone.now()
                if time_difference.total_seconds() <= 86500:
                    if intern in user.interns_applied_for.all():
                        intern_data = f"""{intern.intern_name}\t{intern.company}\t{intern.role}\n"""
                        email_body = email_body+intern_data
                        count = count+1
            if count != 0:
                sender = EMAIL_HOST_USER
                recipient = user.email
                name = user.name 
                subject = EMAIL_SUBJECT["InternMailer"]
                body = EMAIL_BODY["InternMailer"].format(name=name, body=email_body)
                send_mail(subject, body, sender, [recipient], fail_silently=False)
