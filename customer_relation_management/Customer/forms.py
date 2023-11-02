from django import forms

from .models import Customer

class CustomerRegisterationForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']

class CustomerChangeForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']

class MultiSelectedCustomer(forms.Form):
    selected_customers = forms.ModelMultipleChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )