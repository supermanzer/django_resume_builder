# django_resume_builder
A Django application built with Docker for creating resume web pages and exporting them as PDFs using Django WeasyPrint


This was born out of a desire to leverage relational database techniques to make building resumes easier.  In this case I am using the default Django Admin page as the UI into which I enter employment histories, KSAs, projects, etc.  I would be excited to see what more talented front end developers could do with this approach!


If you want to play around with this application you will need to have `docker` and `docker-compose` installed.  Once those requirements are met simply follow these directions:

```
git clone git@github.com:supermanzer/django_resume_builder.git .
docker-compose up -d --build
```
The command in the `docker-compose.yml` file will run the start_app.sh script to perform initial migrations and spin up the development server.  In the process it will create a default superuser to get you started.  The login credentials for the default superuser can be found in the Default User dropdown menu in the navbar on the home page.

Then simply navigate to `localhost:8123` to start building your resume

An example of an output is the EXAMPLE_RESUME.pdf file in this repo.



##### <text style="color:red">Running the start_app.sh script will generate a .user file.  This is used to determine whether the default superuser account has been created.  If this file is deleted, the start_app.sh script will attempt to create a new superuser account.  This may cause the server to not to start up.</text>

## Customized Classes and Methods
I have included a few cusomizations that I regularly employ that others might find useful.

#### `JsonTemplateMixin` in `custom.mixins.py`
This is a stupid simple mixin I use to simply return rendered Django templates as JSON responses.  It follows a basic methodology that I have grown used to in my work.  Rendering the template to a string is wrapped in a `try..except` block which will return a JSON response containing an `is_valid` Boolean value and either an `html` or `error` attribute depending on the success or failure of the `render_to_string` operation.

#### Custom `get_pdf_stylesheets` function in view using `WeasyTemplateResponseMixin`
I built the `Resume` model to allow users to specify the stylesheet to be applied when rendering the resume template.  Overriding the `get_pdf_stylesheets` function in the `WeasyTemplateResponseMixin` class allows me to select the stylesheet defined in the Resume model being accessed by the view.
