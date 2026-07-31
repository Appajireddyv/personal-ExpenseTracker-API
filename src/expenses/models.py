from django.db import models
from django.utils import timezone


CATEGORY_CHOICES = [
    ('food', '🍔 Food & Dining'),
    ('transport', '🚗 Transport'),
    ('housing', '🏠 Housing'),
    ('entertainment', '🎬 Entertainment'),
    ('health', '💊 Health'),
    ('shopping', '🛍️ Shopping'),
    ('travel', '✈️ Travel'),
    ('utilities', '💡 Utilities'),
    ('education', '📚 Education'),
    ('other', '📦 Other'),
]

CATEGORY_COLORS = {
    'food': '#FF6B6B',
    'transport': '#4ECDC4',
    'housing': '#45B7D1',
    'entertainment': '#A855F7',
    'health': '#22C55E',
    'shopping': '#F59E0B',
    'travel': '#3B82F6',
    'utilities': '#EC4899',
    'education': '#14B8A6',
    'other': '#94A3B8',
}


class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.title} — ${self.amount}"

    def category_color(self):
        return CATEGORY_COLORS.get(self.category, '#94A3B8')

    def category_label(self):
        return dict(CATEGORY_CHOICES).get(self.category, 'Other')
