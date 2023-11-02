from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from Customer.models import Customer

from Finance.models import Transaction
from .models import InvalidLOgins, User

from users.forms import UserRegistrationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.hashers import make_password 
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count

# Create your views here.
@login_required
def index(request):
      # Get customer count
    customer_count = Customer.objects.count()
    # Get total transactions amount
    total_transactions_amount = Transaction.objects.aggregate(Sum('amount'))['amount__sum']
    
    # Get yearly transaction data (for example, for the year 2023)
    yearly_transactions = Transaction.objects.filter(transaction_date__year=2023)
    
    # Aggregate yearly transaction data
    yearly_transaction_amount = yearly_transactions.aggregate(Sum('amount'))['amount__sum']

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
    
    context = {
        'customer_count': customer_count,
        'total_transactions_amount': total_transactions_amount,
        'yearly_transaction_amount': yearly_transaction_amount,
        'yearly_data':yearly_data,
    }


    return render (request,'admin_dashboard/index.html',context)

# user registration and giving staff or admin 
def registerion(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # redirect to index page
            return HttpResponseRedirect(reverse('users:index'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'admin_dashboard/registration.html', {'form': form})


#users list 
@login_required
def user_list(request):
    users = User.objects.all()
    return render (request,'admin_dashboard/allusers.html',{'users':users})
        

@login_required
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            # Update user password only if provided
            password = form.cleaned_data.get('password1')
            if password:
                user.set_password(password)
            form.save()
            return HttpResponseRedirect(reverse('users:all_users'))
    else:
        form = UserRegistrationForm(instance=user)

    return render(request, 'admin_dashboard/update_user.html', {'form': form, 'user': user})


# user delete
@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect(reverse('users:all_users'))





# user log in 

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the appropriate page after successful login
                # For example, you can redirect to a dashboard page:
                return HttpResponseRedirect (reverse('users:index'))
            else:
                # Handle invalid login credentials
                print(form.errors)
                attempts = InvalidLOgins(user_email = request.POST['email'],
                                         password=request.POST['password'],
                                         at_attempted = datetime.now())
                attempts.save()
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))



def profile(request):
    user = User.objects.all()
    return render(request,'admin_dashboard/user_profile.html',{'user':user})



