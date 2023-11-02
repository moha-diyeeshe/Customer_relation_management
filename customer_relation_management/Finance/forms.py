from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['customer', 'amount', 'transaction_date']  # Add other fields as needed


class TransactionChangeForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['customer', 'amount', 'transaction_date']  