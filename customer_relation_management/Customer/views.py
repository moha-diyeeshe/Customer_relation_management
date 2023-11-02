from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from Customer.forms import CustomerChangeForm, CustomerRegisterationForm, MultiSelectedCustomer

from Customer.models import Customer

# Create your views here.
def customers_list(request):
    customers = Customer.objects.all()
    return render (request,'customers_dashboard/customers.html',{'customer':customers})

def customer_registeration(request):
    if request.method == 'POST':
        form = CustomerRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:customers'))
        else:
            print(form.errors)
    else:
        form = CustomerRegisterationForm()

    return render(request, 'customers_dashboard/customers_regiseration.html', {'form': form})


def customer_update(request, user_id):
    customer = get_object_or_404(Customer, id=user_id)
    if request.method == 'POST':
        form = CustomerChangeForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            # Redirect or do something else after successful update
    else:
        form = CustomerChangeForm(instance=customer)

    return render(request, 'customers_dashboard/customer_update.html', {'form': form, 'customer': customer})


def customer_delete(request, user_id):
    customer = get_object_or_404(Customer, id=user_id)
    customer.delete()
    return HttpResponseRedirect(reverse('customers:customers'))


def multi_selected_delete(request):
    customer_ids = request.GET.get('ids', '').split(',')
    for customer_id in customer_ids:
        customer = get_object_or_404(Customer, id=customer_id)
        customer.delete()
    return HttpResponseRedirect(reverse('customers:customers'))