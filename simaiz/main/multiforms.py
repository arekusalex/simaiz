from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.utils.encoding import force_text
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ProcessFormView

class MultipleFormsMixin(ContextMixin):
    initial = {}
    forms_classes = []
    success_url = None
    prefix = None
    active_form_keyword = "selected_form"

    def get_initial(self):
        return self.initial.copy()

    def get_prefix(self):
        return self.prefix

    def get_forms_classes(self):
        return self.forms_classes

    def get_active_form_number(self):
        if self.request.method in ('POST', 'PUT'):
            try:
                return int(self.request.POST[self.active_form_keyword])
            except (KeyError, ValueError):
                raise ImproperlyConfigured(
                    "You must include hidden field with field index in every form! Example:")

    def get_forms(self, active_form=None):
        all_forms_classes = self.get_forms_classes()
        all_forms = [
            form_class(**self.get_form_kwargs())
            for form_class in all_forms_classes]
        if active_form:
            active_form_number = self.get_active_form_number()
            all_forms[active_form_number] = active_form
        return all_forms

    def get_form(self):
        active_form_number = self.get_active_form_number()
        if active_form_number is not None:
            all_forms_classes = self.get_forms_classes()
            active_form_class = all_forms_classes[active_form_number]
            return active_form_class(**self.get_form_kwargs(is_active=True))

    def get_form_kwargs(self, is_active=False):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }

        if is_active:
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def get_success_url(self):
        if self.success_url:
            # Forcing possible reverse_lazy evaluation
            url = force_text(self.success_url)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url.")
        return url

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(active_form=form))

    def get_context_data(self, **kwargs):
        if 'forms' not in kwargs:
            kwargs['forms'] = self.get_forms(kwargs.get('active_form'))
        return super(MultipleFormsMixin, self).get_context_data(**kwargs)

class MultipleFormsView(TemplateResponseMixin, MultipleFormsMixin, ProcessFormView):
    pass

