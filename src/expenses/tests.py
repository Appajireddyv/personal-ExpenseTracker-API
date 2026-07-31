from decimal import Decimal

from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.utils import timezone

from .forms import ExpenseForm
from .models import Expense
from .views import (
    dashboard,
    add_expense,
    edit_expense,
    delete_expense,
    reset_all,
)


# ==========================================================
# Model Tests
# ==========================================================

class ExpenseModelTest(TestCase):

    def setUp(self):
        self.expense = Expense.objects.create(
            title="Lunch",
            amount=Decimal("250.50"),
            category="food",
            date=timezone.now().date(),
            notes="Office lunch"
        )

    def test_expense_creation(self):
        self.assertEqual(self.expense.title, "Lunch")
        self.assertEqual(self.expense.amount, Decimal("250.50"))
        self.assertEqual(self.expense.category, "food")

    def test_string_representation(self):
        self.assertEqual(str(self.expense), "Lunch — $250.50")

    def test_category_color(self):
        self.assertEqual(self.expense.category_color(), "#FF6B6B")

    def test_category_label(self):
        self.assertEqual(
            self.expense.category_label(),
            "🍔 Food & Dining"
        )


# ==========================================================
# Form Tests
# ==========================================================

class ExpenseFormTest(TestCase):

    def test_valid_form(self):
        form = ExpenseForm(data={
            "title": "Fuel",
            "amount": "500.00",
            "category": "transport",
            "date": "2026-07-31",
            "notes": "Bike fuel"
        })

        self.assertTrue(form.is_valid())

    def test_invalid_form_without_title(self):
        form = ExpenseForm(data={
            "title": "",
            "amount": "500.00",
            "category": "transport",
            "date": "2026-07-31",
            "notes": ""
        })

        self.assertFalse(form.is_valid())


# ==========================================================
# View Tests
# ==========================================================

class ExpenseViewTests(TestCase):

    def setUp(self):
        self.expense = Expense.objects.create(
            title="Lunch",
            amount=Decimal("250.00"),
            category="food",
            date=timezone.now().date(),
            notes="Office lunch"
        )

    def test_dashboard_page(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_add_expense(self):
        response = self.client.post(
            reverse("add_expense"),
            {
                "title": "Fuel",
                "amount": "400.00",
                "category": "transport",
                "date": "2026-07-31",
                "notes": ""
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Expense.objects.count(), 2)

    def test_edit_expense(self):
        response = self.client.post(
            reverse("edit_expense", args=[self.expense.pk]),
            {
                "title": "Updated Lunch",
                "amount": "300.00",
                "category": "food",
                "date": self.expense.date.strftime("%Y-%m-%d"),
                "notes": "Updated notes"
            }
        )

        self.expense.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.expense.title, "Updated Lunch")
        self.assertEqual(self.expense.amount, Decimal("300.00"))
        self.assertEqual(self.expense.notes, "Updated notes")

    def test_delete_expense(self):
        response = self.client.post(
            reverse("delete_expense", args=[self.expense.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Expense.objects.count(), 0)

    def test_reset_all(self):
        Expense.objects.create(
            title="Fuel",
            amount="500",
            category="transport"
        )

        response = self.client.post(reverse("reset_all"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Expense.objects.count(), 0)


# ==========================================================
# URL Tests
# ==========================================================

class URLTests(SimpleTestCase):

    def test_dashboard_url(self):
        url = reverse("dashboard")
        self.assertEqual(resolve(url).func, dashboard)

    def test_add_url(self):
        url = reverse("add_expense")
        self.assertEqual(resolve(url).func, add_expense)

    def test_edit_url(self):
        url = reverse("edit_expense", args=[1])
        self.assertEqual(resolve(url).func, edit_expense)

    def test_delete_url(self):
        url = reverse("delete_expense", args=[1])
        self.assertEqual(resolve(url).func, delete_expense)

    def test_reset_url(self):
        url = reverse("reset_all")
        self.assertEqual(resolve(url).func, reset_all)