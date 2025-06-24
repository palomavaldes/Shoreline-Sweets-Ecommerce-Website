#from django import forms
#from .models import Order

#class OrderCreateForm(forms.ModelForm):
 #   class Meta:
  ##     fields = ["full_name", "email", "shipping_address"]


# orders/forms.py
from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'shipping_address']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your full name (e.g., John Doe)'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address (e.g., example@domain.com)'}),
            'shipping_address': forms.TextInput(attrs={'placeholder': 'Your full shipping address'}),
            # You might want forms.Textarea for address if it's long, with a placeholder
            # 'address': forms.Textarea(attrs={'placeholder': 'Your full shipping address', 'rows': 3}),
        }