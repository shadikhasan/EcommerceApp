import random
from django.core.management.base import BaseCommand
from shop.models import Products

class Command(BaseCommand):
    help = 'Add 100+ random products to the database'

    def handle(self, *args, **kwargs):
        categories = ['Electronics', 'Books', 'Clothing', 'Home Appliances', 'Sports']
        descriptions = [
            'A great product for daily use.',
            'High-quality and durable.',
            'Best in class and affordable.',
            'Stylish and modern design.',
            'Limited edition product.'
        ]

        for i in range(1, 101):  # Generates 100 products
            product = Products(
                title=f'Product {i}',
                price=round(random.uniform(10.99, 999.99), 2),  # Random price between $10.99 and $999.99
                discount_price=round(random.uniform(5.99, 499.99), 2),  # Random discount price
                category=random.choice(categories),
                description=random.choice(descriptions),
                image=f'https://via.placeholder.com/150?text=Product+{i}'  # Placeholder image URL
            )
            product.save()

        self.stdout.write(self.style.SUCCESS('Successfully added 100+ products!'))
