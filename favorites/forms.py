from django import forms

from favorites.services import ProductService


class FavoriteProductsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.client = kwargs.pop('client', None)
        super().__init__(*args, **kwargs)

        self.fields['products'] = forms.MultipleChoiceField(
            choices=self._create_choices(),
            widget=forms.CheckboxSelectMultiple,
            required=False
        )

    @staticmethod
    def _create_choices() -> list:
        products = ProductService.list_products()
        return [(product['id'], f"{product['name']} - ${product.get('price', 0)}") for product in products]
