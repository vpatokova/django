from django import forms

from catalog.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (Item.name.field.name,)

        help_text = {
            "text": "Помогаем",
        }
        label = {
            "text": "Название",
        }


def start_with_a(value):
    if value[0] != "A":
        raise forms.ValidationError("Should start with A!!!")


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        max_length=100,
        validators=[start_with_a],
    )
    email = forms.EmailField(
        label="Почта",
        max_length=100,
    )


class PersonForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    surname = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        ),
    )
    lucky_number = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
