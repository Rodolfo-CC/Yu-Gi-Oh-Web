from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    """
    Form for creating or updating a Card object.
    """
    class Meta:
        model = Card
        fields: list[str] = [
            'id', 'name', 'text', 'level', 'attack', 'defense', 'card_type', 'attribute', 'rarity', 'image',
        ]
        widgets: dict[str, forms.Widget] = {
            'text': forms.Textarea(attrs={'rows': 4})
        }
        help_texts: dict[str, str] = {
            'id': 'Enter the unique card ID (e.g., LOB-001).',
        }
