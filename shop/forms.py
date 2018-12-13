from django import forms
from . import models 


class OrderForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = ['product_name', 'product_id', 'user_name', 'user_email', 'user_phone', 'user_address', 'user_add_info']
        widgets = {
            'product_name': forms.widgets.HiddenInput(),
            'product_id': forms.widgets.HiddenInput(),
            'user_name': forms.widgets.TextInput(
                attrs={ 
                    'class': 'input-style',
                    'placeholder': 'Name',
                    'required': 'True'
                },
            ),
            'user_email': forms.widgets.TextInput(
                attrs={ 
                    'class': 'input-style',
                    'placeholder': 'Email',
                },
            ),
            'user_phone': forms.widgets.TextInput(
                attrs={ 
                    'class': 'input-style',
                    'type': "tel", 
                    'placeholder': 'Phone',
                    'required': 'True'
                },
            ),
            'user_address': forms.widgets.TextInput(
                attrs={ 
                    'class': 'input-style',
                    'placeholder': 'Address',
                    'required': 'True'
                },
            ),
            'user_add_info': forms.widgets.Textarea(
                attrs={
                    'class': 'input-style',
                    'rows': '10',
                    'placeholder': 'Additional information',
                }
            )
        }
