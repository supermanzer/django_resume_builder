"""
=====================================================================
custom/mixin.py
=====================================================================
This file defines custom mixins used to extend the capabilities of
built-in class based views
"""
from django.http import JsonResponse
from django.template.loader import render_to_string

class JsonTemplateMixin:
    """
    A mixnin for returning a rendered template as a JSON response,
    along with a value to indicate to a calling function whether the
    rendering was successful or not.
    """

    def render_to_response(self, context, **response_kwargs):
        """
        Directly overriding the render_to_response function. Inherit like you mean it!
        """
        response = self._get_data(context)
        return JsonResponse(response, **response_kwargs)

    def _get_data(self, context):
        # Checking for proper templates
        if self.template_name:
            template = self.template_name
        else:
            template = self.get_template_names()[0]

        if not template:
            raise ValueError('No template supplied')
        # Instantiating our response as a JSON serializable object (dictionary)
        resp = dict()
        try:
            resp['html']=render_to_string(template, context=context)
            resp['is_valid']=True
        except Exception as e:
            resp['error']=str(e)
            resp['is_valid']=False

        return resp
