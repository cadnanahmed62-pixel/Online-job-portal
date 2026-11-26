
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Role(models.TextChoices):
        JOB_SEEKER = 'JOB_SEEKER', 'Job Seeker'
        EMPLOYER = 'EMPLOYER', 'Employer'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.JOB_SEEKER
    )

    is_employer_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='job_seeker_profile'
    )

    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    skills = models.TextField(blank=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    cv = models.FileField(
        upload_to='cvs/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username} Profile"
