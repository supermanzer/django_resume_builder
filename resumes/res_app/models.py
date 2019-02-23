from django.db import models
from django.urls import reverse


SHORT_FORMAT = '%b %Y'
KSA_TYPES=(
    ('sk', 'Skill'),
    ('tc', 'Technology'),
)
# Create your models here.

class PhoneNumber(models.Model):
    """
    A simple model capturing phone numbers
    """
    # CHOICES
    TYPES = (
        ('h', 'Home'),
        ('w', 'Work'),
        ('m', 'Mobile')
    )
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='PhoneNumber_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='PhoneNumber_modified')
    phone_number = models.CharField(max_length=100, null=True, blank=True, help_text='Enter your phone number')
    type = models.CharField(max_length=1, choices=TYPES, null=True, blank=True, help_text='The type of phone number represented by this record')

    class Meta:
        app_label = 'res_app'

    def __str__(self):
        return self.phone_number

class SocialMedia(models.Model):
    """
    A simple model to house social media accounts we wish to share.
    """
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='SocialMedia_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='SocialMedia_modified')
    media_name = models.CharField(max_length=200, null=True, blank=True, help_text='The name of the social media platform (e.g. GitHub)')
    href = models.URLField(max_length=200, null=True, blank=True, help_text='The URL used to connect to this social media profile')
    icon = models.CharField(max_length=200, null=True, blank=True, help_text='The Font Awesome icon code to be applied.')

    def __str__(self):
        return self.media_name

    class Meta:
        app_label = 'res_app'
        verbose_name_plural = 'Social Media'

class Address(models.Model):
    """
    A simple model for capturing a physical address
    """
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Address_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Address_modified')
    street_1 = models.CharField(max_length=100, null=True, blank=True, help_text='First line in a street address')
    street_2 = models.CharField(max_length=100, null=True, blank=True, help_text='Second line for street address')
    street_3 = models.CharField(max_length=100, null=True, blank=True, help_text='Third line in street address')
    city = models.CharField(max_length=100, null=True, blank=True, help_text='City')
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        app_label = 'res_app'

    def __str__(self):
        return self.street_1 + ', ' + self.city


class ContactInfo(models.Model):
    """
    A model of contact information, linking to a given user
    """
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='ContactInfo_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='ContactInfo_modified')
    person = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)
    phone_numbers = models.ManyToManyField(PhoneNumber)
    email = models.EmailField(null=True, blank=True, help_text='Enter a valid email address')
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    social_media = models.ManyToManyField(SocialMedia)

    class Meta:
        app_label = 'res_app'
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.person.get_full_name() + " contact info"

class KSA(models.Model):
    """
    A model capturing records of Knowledge, Skills, and Abilities.
    """
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='KSA_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='KSA_modified')
    name = models.CharField(max_length=100, null=True, blank=True, help_text='The short name for this KSA')
    years = models.FloatField(default=0, help_text='The number of years experience with this KSA')
    description = models.TextField(help_text='A description of this particular KSA')
    type = models.CharField(max_length=2, choices=KSA_TYPES, null=True, blank=True, help_text='The type of knowledge, skill, or ability this record represents')

    class Meta:
        app_label = 'res_app'
        verbose_name_plural = 'KSAs'

    def __str__(self):
        return self.name + ' ' + str(self.years) + ' years'

class Employment(models.Model):
    """
    A model for employment history
    """
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Employment_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Employment_modified')
    employer = models.CharField(max_length=200, null=True, blank=True, help_text='The name of the employer')
    position = models.CharField(max_length=200, null=True, blank=True, help_text='The name of the position held at this employer')
    start_date = models.DateField(help_text='The approximate start date for this employment')
    end_date = models.DateField(help_text='The approximate end date for this employment', blank=True, null=True)
    description = models.TextField(help_text='A description of this employment')
    ksas = models.ManyToManyField(KSA, help_text='The Knowledge, Skills, and Abilities used in this employment', verbose_name="KSA's")

    class Meta:
        app_label = 'res_app'
        ordering = ['-start_date', ]

    def get_start_date(self):
        return self.start_date.strftime(SHORT_FORMAT)

    def get_end_date(self):
        return self.end_date.strftime(SHORT_FORMAT) if self.end_date else 'Present'

    def __str__(self):
        return self.employer + ": " + self.start_date.strftime(SHORT_FORMAT) + ' - ' + self.get_end_date()

class Project(models.Model):
    """
    A model for capturing individual projects (like GitHub repos) that you may want to include on a resume.
    """
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Project_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Project_modified')
    name = models.CharField(max_length=200, null=True, blank=True, help_text='The brief name of this projects')
    url = models.URLField(max_length=200, null=True, blank=True, help_text='A URL to point people towards this project')
    description = models.TextField(help_text='A description of this project')

    class Meta:
        app_label = 'res_app'

    def __str__(self):
        return self.name

class EducationHistory(models.Model):
    """
    A model to capture specific education histories.
    """
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Eduction_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Eduction_modified')
    institution = models.CharField(max_length=200, null=True, blank=True, help_text='The name of the educational institution')
    start_date = models.DateField(null=True, blank=True, help_text='The start date for this education history')
    end_date = models.DateField(null=True, blank=True, help_text='The end date for this education history')
    graduated = models.BooleanField(default=False, help_text='Whether or not a person graduated from this particular institution')
    degree_attained = models.CharField(max_length=100, null=True, blank=True, help_text='The degree (if any) attained at this institution')
    focus = models.CharField(max_length=200, null=True, blank=True, help_text='The focus (e.g. major, thesis, etc.) of this academic history')

    def get_start_date(self):
        return self.start_date.strftime(SHORT_FORMAT)

    def get_end_date(self):
        return self.end_date.strftime(SHORT_FORMAT)

    def __str__(self):
        return self.institution + ' ' + self.get_start_date() + ' - ' + self.get_end_date

    class Meta:
        app_label = 'res_app'


class Resume(models.Model):
    """
    A model defining a specific resume to be generated
    """
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Resume_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Resume_modified')
    person = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)
    ksas = models.ManyToManyField(KSA)
    employment_histories = models.ManyToManyField(Employment)
    projects = models.ManyToManyField(Project)
    style_class = models.CharField(max_length=100, null=True, blank=True, help_text='The CSS style class to be applied when rendering this resume')
    css_file_name = models.CharField(max_length=100, null=True, blank=True, help_text='The specific css file that will be loaded for this resume')
    template_name = models.CharField(max_length=100, null=True, blank=True, help_text='The string identifying the template to be used to render this resume.')
    name = models.CharField(max_length=200, null=True, blank=True, help_text='A simple name to identify this resume')
    summary = models.TextField(null=True, blank=True, help_text='A personal summary or general description of an employment goal to top the resume.')
    headline = models.CharField(max_length=200, null=True, blank=True, help_text='The title to appear under your name')

    class Meta:
        app_label = 'res_app'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('res_app:res-pdf', kwargs={'pk':self.id})
