from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction
from register.models import CustomUser
from django.db import transaction as django_transaction, transaction
from django.contrib import messages

@login_required
def dashboard(request):
    user = request.user
    transactions = Transaction.objects.filter(sender=user) | Transaction.objects.filter(recipient=user)
    return render(request, 'payapp/dashboard.html', {'transactions': transactions, 'balance': user.balance})

@login_required
def send_money(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')
        amount = float(request.POST.get('amount'))

        try:
            recipient = CustomUser.objects.get(email=recipient_email)
        except CustomUser.DoesNotExist:
            messages.error(request, "Recipient not found.")
            return redirect('send_money')

        if request.user.balance < amount:
            messages.error(request, "Insufficient funds.")
            return redirect('send_money')

        with transaction.atomic():
            request.user.balance -= amount
            recipient.balance += amount
            request.user.save()
            recipient.save()
            Transaction.objects.create(sender=request.user, recipient=recipient, amount=amount, transaction_type='SEND', status='COMPLETED')

        messages.success(request, f"Sent £{amount} to {recipient_email}.")
        return redirect('dashboard')

    return render(request, 'payapp/send_money.html')

@login_required
def request_money(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')
        amount = float(request.POST.get('amount'))

        try:
            recipient = CustomUser.objects.get(email=recipient_email)
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('request_money')

        Transaction.objects.create(sender=request.user, recipient=recipient, amount=amount, transaction_type='REQUEST', status='PENDING')
        messages.success(request, f"Requested £{amount} from {recipient_email}.")
        return redirect('dashboard')

    return render(request, 'payapp/request_money.html')

@login_required
def manage_requests(request):
    pending_requests = Transaction.objects.filter(recipient=request.user, transaction_type='REQUEST', status='PENDING')

    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        action = request.POST.get('action')
        txn = get_object_or_404(Transaction, id=transaction_id)

        if action == 'approve' and request.user.balance >= txn.amount:
            with django_transaction.atomic():
                request.user.balance -= txn.amount
                txn.sender.balance += txn.amount
                request.user.save()
                txn.sender.save()
                txn.status = 'COMPLETED'
                txn.save()
            messages.success(request, "Payment request approved.")
        elif action == 'reject':
            txn.status = 'REJECTED'
            txn.save()
            messages.warning(request, "Payment request rejected.")
        else:
            messages.error(request, "Insufficient balance.")

        return redirect('manage_requests')

    return render(request, 'payapp/manage_requests.html', {'pending_requests': pending_requests})

