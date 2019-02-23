from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User

from django_weasyprint import WeasyTemplateResponseMixin
from custom.mixins import JsonTemplateMixin

from res_app import models
from resumes import settings

# Create your views here.
class IndexView(generic.TemplateView):
    """
    The home page for the Resume App
    """
    template_name = 'res_app/index.html'

class ResumeModelView(generic.DetailView):
    """
    A parent CBV for our PDF printing view
    """
    model = models.Resume

    # Overriding the default get_template_names() function
    # to allow us to dynamically select template names from
    # the admin console
    def get_template_names(self):
        return self.object.template_name

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['skills'] = models.KSA.objects.filter(type='sk')
        context['tech'] = models.KSA.objects.filter(type='tc')

        return context

class ResumePrinter(WeasyTemplateResponseMixin, ResumeModelView):
    """
    This view generates the PDF of the resume template
    """
    pdf_attachment=False
    pdf_filename = 'resume.pdf'


    def get_pdf_stylesheets(self):
        return [
        settings.STATIC_ROOT + '/res_app/css/' + self.object.css_file_name, ]

class ResumeList(JsonTemplateMixin, generic.ListView):
    """
    A simple JSON list of available resumes to convert to PDFs
    """
    model = User
    template_name = 'res_app/resume_list.html'
