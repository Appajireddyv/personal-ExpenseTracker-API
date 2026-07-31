from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Count
from django.utils import timezone
from django.contrib import messages
from datetime import date, timedelta
import json

from .models import Expense, CATEGORY_CHOICES, CATEGORY_COLORS
from .forms import ExpenseForm


def dashboard(request):
    today = date.today()
    first_of_month = today.replace(day=1)

    category_filter = request.GET.get('category', '')
    month_filter = request.GET.get('month', '')

    expenses_qs = Expense.objects.all()
    if category_filter:
        expenses_qs = expenses_qs.filter(category=category_filter)
    if month_filter:
        try:
            year, month = month_filter.split('-')
            expenses_qs = expenses_qs.filter(date__year=int(year), date__month=int(month))
        except Exception:
            pass

    expenses = expenses_qs[:50]

    this_month_qs = Expense.objects.filter(date__gte=first_of_month)
    monthly_total = this_month_qs.aggregate(total=Sum('amount'))['total'] or 0
    monthly_count = this_month_qs.count()
    all_time_total = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0

    category_data = (
        this_month_qs
        .values('category')
        .annotate(total=Sum('amount'), count=Count('id'))
        .order_by('-total')
    )
    category_labels = []
    category_totals = []
    category_colors_list = []
    for item in category_data:
        label = dict(CATEGORY_CHOICES).get(item['category'], item['category'])
        category_labels.append(label)
        category_totals.append(float(item['total']))
        category_colors_list.append(CATEGORY_COLORS.get(item['category'], '#94A3B8'))

    thirty_days_ago = today - timedelta(days=29)
    daily_qs = (
        Expense.objects.filter(date__gte=thirty_days_ago)
        .values('date')
        .annotate(total=Sum('amount'))
        .order_by('date')
    )
    daily_map = {item['date'].strftime('%b %d'): float(item['total']) for item in daily_qs}
    daily_labels = []
    daily_values = []
    for i in range(30):
        d = thirty_days_ago + timedelta(days=i)
        label = d.strftime('%b %d')
        daily_labels.append(label)
        daily_values.append(daily_map.get(label, 0))

    context = {
        'expenses': expenses,
        'monthly_total': monthly_total,
        'monthly_count': monthly_count,
        'all_time_total': all_time_total,
        'category_labels': json.dumps(category_labels),
        'category_totals': json.dumps(category_totals),
        'category_colors': json.dumps(category_colors_list),
        'daily_labels': json.dumps(daily_labels),
        'daily_values': json.dumps(daily_values),
        'categories': CATEGORY_CHOICES,
        'category_filter': category_filter,
        'month_filter': month_filter,
        'today': today.strftime('%Y-%m-%d'),
    }
    return render(request, 'expenses/dashboard.html', context)


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('dashboard')
    else:
        form = ExpenseForm(initial={'date': date.today()})
    return render(request, 'expenses/form.html', {'form': form, 'action': 'Add'})


def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated!')
            return redirect('dashboard')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/form.html', {'form': form, 'action': 'Edit', 'expense': expense})


def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted.')
        return redirect('dashboard')
    return render(request, 'expenses/confirm_delete.html', {'expense': expense})


def reset_all(request):
    if request.method == 'POST':
        Expense.objects.all().delete()
        messages.success(request, 'All expenses have been reset.')
        return redirect('dashboard')

    return render(request, 'expenses/confirm_reset.html')