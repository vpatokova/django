import django.forms
import catalog.models


class ItemModelForm(django.forms.ModelForm):
    class Meta:
        model = catalog.models.Item
        fields = ["tags"]

    def __init__(self, *args, **kwargs):
        django.forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields["tags"].queryset = catalog.models.Item.avail.all()
