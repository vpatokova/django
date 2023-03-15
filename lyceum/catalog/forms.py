from django import forms

from catalog.models import Item, Tag


class TagUpdateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = (Tag.slug.field.name,)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (Item.name.field.name,)

        labels = {
            Item.name.field.name: "Имя поля",
        }

        help_texts = {
            Item.name.field.name: "Подсказка",
        }
