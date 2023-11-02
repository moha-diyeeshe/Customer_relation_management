from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from Customer.models import Customer
from Finance.forms import TransactionChangeForm, TransactionForm

from Finance.models import Transaction
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count
from django.contrib.auth import decorators

# Create your views here.
@login_required
def transactions_view(request):
    transactions = Transaction.objects.all()
    return render(request,'Transactions/all_transactions.html',{'transactions':transactions})
@login_required
def transaction_register(request):
    customers =Customer.objects.all()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other desired action
            return HttpResponseRedirect(reverse('finance:transactions'))
    else:
        form = TransactionForm()

    return render(request, 'Transactions/registeration.html', {'form': form, 'customers':customers})

@login_required
def transaction_update(request,transaction_id):
    customers =Customer.objects.all()
    transaction = get_object_or_404(Transaction,id=transaction_id)
    if request.method == 'POST':
        form = TransactionChangeForm(request.POST, instance = transaction)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('finance:transactions'))
        else:
            print(form.errors)

    else:
        form = TransactionChangeForm(instance = transaction)
    return render(request,'Transactions/transaction_update.html',{'form': form,'transaction':transaction,'customers':customers})
@login_required
def transaction_delete(request,transaction_id):
    transaction = get_object_or_404(Transaction,id=transaction_id)
    transaction.delete()
    return HttpResponseRedirect(reverse('finance:transactions'))

@login_required
def multi_selected_delete(request):
    transaction_ids = request.GET.get('ids', '').split(',')
    for transaction_id in transaction_ids:
        transaction = get_object_or_404(Transaction, id=transaction_id)
        transaction.delete()
    return HttpResponseRedirect(reverse('finance:transactions'))


@login_required
def dashboard_view(request):
    # Get customer count
    customer_count = Customer.objects.count()
    # Get total transactions amount
    total_transactions_amount = Transaction.objects.aggregate(Sum('amount'))['amount__sum']
    
    # Get yearly transaction data (for example, for the year 2023)
    yearly_transactions = Transaction.objects.filter(transaction_date__year=2023)
    
    # Aggregate yearly transaction data
    yearly_transaction_amount = yearly_transactions.aggregate(Sum('amount'))['amount__sum']
    
    context = {
        'customer_count': customer_count,
        'total_transactions_amount': total_transactions_amount,
        'yearly_transaction_amount': yearly_transaction_amount,
    }
    return render(request, 'Transactions/financial_data.html', context)




#yearly reports
@login_required
def yearly_report(request):
    current_year = timezone.now().year
    ten_years_ago = current_year - 10

    # Filter transactions for the last 10 years
    yearly_transactions = Transaction.objects.filter(transaction_date__year__gte=ten_years_ago)

    # Aggregate data for each year
    yearly_data = yearly_transactions.values('transaction_date__year').annotate(
        total_transactions=Count('id'),
        total_amount=Sum('amount'),
        total_customers=Count('customer', distinct=True)
    ).order_by('transaction_date__year')

    return render(request, 'admin_dashboard/yearly_report.html', {'yearly_data': yearly_data})


def payments(request):
    transactions = Transaction.objects.all()
    return render(request,'Transactions/payments.html',{'transactions':transactions})






        