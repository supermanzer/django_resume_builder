from django.contrib import admin

from res_app import models
# Register your models here.
@admin.register(models.PhoneNumber)
class PhoneAdmin(admin.ModelAdmin):
    model = models.PhoneNumber
    list_display = ('phone_number', 'type', 'date_created')

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    model = models.Address
    list_display = ('street_1', 'city', 'state','zip_code')

@admin.register(models.ContactInfo)
class ContactAdmin(admin.ModelAdmin):
    model = models.ContactInfo
    list_display = ('person', 'email')

@admin.register(models.KSA)
class KsaAdmin(admin.ModelAdmin):
    model = models.KSA
    list_display = ('name', 'years')

@admin.register(models.Employment)
class EmploymentAdmin(admin.ModelAdmin):
    model = models.Employment
    list_display = ('employer', 'created_by', 'position', 'start_date', 'end_date')

@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    model = models.Resume
    list_display = ('person', 'style_class', 'date_created')

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    model = models.Project
    list_display = ('name', 'url')

@admin.register(models.SocialMedia)
class MediaAdmin(admin.ModelAdmin):
    modle = models.SocialMedia
    list_display=('media_name', 'href', 'icon')
