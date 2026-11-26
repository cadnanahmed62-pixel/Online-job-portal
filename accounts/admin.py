
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, JobSeekerProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('role', 'is_employer_approved')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('role', 'is_employer_approved')
        }),
    )

    list_display = (
        'username',
        'email',
        'role',
        'is_employer_approved',
        'is_staff'
    )

    list_filter = ('role', 'is_employer_approved')
    search_fields = ('username', 'email')


@admin.register(JobSeekerProfile)
class JobSeekerProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'phone_number',
        'address'
    )

    search_fields = (
        'user__username',
        'phone_number',
        'address'
    )
