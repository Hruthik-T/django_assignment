import os
import django
import random
from decimal import Decimal

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

# Import models
from products.models import Category, Tag, Product

# Create Categories
def create_categories():
    categories = [
        {'name': 'Electronics', 'description': 'Electronic devices and accessories'},
        {'name': 'Clothing', 'description': 'Apparel and fashion items'},
        {'name': 'Books', 'description': 'Books, novels, and textbooks'},
        {'name': 'Home & Kitchen', 'description': 'Home appliances and kitchen equipment'},
        {'name': 'Sports & Outdoors', 'description': 'Sports equipment and outdoor gear'},
        {'name': 'Toys & Games', 'description': 'Children toys and games'},
    ]
    
    created_categories = []
    for category_data in categories:
        category, created = Category.objects.get_or_create(**category_data)
        created_categories.append(category)
        print(f"Category {'created' if created else 'already exists'}: {category.name}")
    
    return created_categories

# Create Tags
def create_tags():
    tags = [
        {'name': 'Sale'},
        {'name': 'New Arrival'},
        {'name': 'Best Seller'},
        {'name': 'Limited Edition'},
        {'name': 'Eco-Friendly'},
        {'name': 'Handmade'},
        {'name': 'Premium'},
        {'name': 'Exclusive'},
        {'name': 'Featured'},
        {'name': 'Recommended'},
        {'name': 'Top Rated'},
        {'name': 'Clearance'},
    ]
    
    created_tags = []
    for tag_data in tags:
        tag, created = Tag.objects.get_or_create(**tag_data)
        created_tags.append(tag)
        print(f"Tag {'created' if created else 'already exists'}: {tag.name}")
    
    return created_tags

# Create Products
def create_products(categories, tags):
    products = [
        {
            'name': 'Smartphone XYZ',
            'description': 'Latest model with advanced features and 5G connectivity',
            'price': Decimal('699.99'),
            'category': categories[0],  # Electronics
            'is_available': True
        },
        {
            'name': 'Laptop Pro',
            'description': 'Powerful laptop with high performance and long battery life',
            'price': Decimal('1199.99'),
            'category': categories[0],  # Electronics
            'is_available': True
        },
        {
            'name': 'Wireless Earbuds',
            'description': 'True wireless earbuds with noise cancellation',
            'price': Decimal('149.99'),
            'category': categories[0],  # Electronics
            'is_available': True
        },
        {
            'name': 'Smart Watch',
            'description': 'Track your fitness and stay connected with this stylish smart watch',
            'price': Decimal('249.99'),
            'category': categories[0],  # Electronics
            'is_available': False
        },
        {
            'name': 'Men\'s T-Shirt',
            'description': 'Comfortable cotton t-shirt for everyday wear',
            'price': Decimal('24.99'),
            'category': categories[1],  # Clothing
            'is_available': True
        },
        {
            'name': 'Women\'s Jeans',
            'description': 'Classic fit jeans with stretch material',
            'price': Decimal('59.99'),
            'category': categories[1],  # Clothing
            'is_available': True
        },
        {
            'name': 'Winter Jacket',
            'description': 'Warm and water-resistant jacket for cold weather',
            'price': Decimal('129.99'),
            'category': categories[1],  # Clothing
            'is_available': True
        },
        {
            'name': 'Running Shoes',
            'description': 'Lightweight and comfortable shoes for running',
            'price': Decimal('89.99'),
            'category': categories[1],  # Clothing
            'is_available': True
        },
        {
            'name': 'The Great Novel',
            'description': 'Bestselling novel that has captivated readers worldwide',
            'price': Decimal('15.99'),
            'category': categories[2],  # Books
            'is_available': True
        },
        {
            'name': 'Cookbook Collection',
            'description': 'Collection of recipes from around the world',
            'price': Decimal('29.99'),
            'category': categories[2],  # Books
            'is_available': True
        },
        {
            'name': 'Science Textbook',
            'description': 'Comprehensive textbook covering various science topics',
            'price': Decimal('49.99'),
            'category': categories[2],  # Books
            'is_available': False
        },
        {
            'name': 'Coffee Maker',
            'description': 'Automatic coffee maker for perfect brews every time',
            'price': Decimal('79.99'),
            'category': categories[3],  # Home & Kitchen
            'is_available': True
        },
        {
            'name': 'Blender',
            'description': 'High-speed blender for smoothies and food processing',
            'price': Decimal('69.99'),
            'category': categories[3],  # Home & Kitchen
            'is_available': True
        },
        {
            'name': 'Cookware Set',
            'description': 'Complete set of pots and pans for your kitchen',
            'price': Decimal('199.99'),
            'category': categories[3],  # Home & Kitchen
            'is_available': True
        },
        {
            'name': 'Yoga Mat',
            'description': 'Non-slip yoga mat for your workout sessions',
            'price': Decimal('29.99'),
            'category': categories[4],  # Sports & Outdoors
            'is_available': True
        },
        {
            'name': 'Tennis Racket',
            'description': 'Professional tennis racket for improved performance',
            'price': Decimal('119.99'),
            'category': categories[4],  # Sports & Outdoors
            'is_available': True
        },
        {
            'name': 'Camping Tent',
            'description': 'Spacious tent for outdoor camping adventures',
            'price': Decimal('149.99'),
            'category': categories[4],  # Sports & Outdoors
            'is_available': True
        },
        {
            'name': 'Building Blocks Set',
            'description': 'Creative building blocks for children',
            'price': Decimal('34.99'),
            'category': categories[5],  # Toys & Games
            'is_available': True
        },
        {
            'name': 'Board Game',
            'description': 'Family board game for hours of fun',
            'price': Decimal('25.99'),
            'category': categories[5],  # Toys & Games
            'is_available': True
        },
        {
            'name': 'Puzzle Set',
            'description': '1000-piece puzzle for challenging entertainment',
            'price': Decimal('19.99'),
            'category': categories[5],  # Toys & Games
            'is_available': True
        }
    ]
    
    created_products = []
    for product_data in products:
        # Extract tags to add after product creation
        category = product_data.pop('category')
        
        # Get or create the product
        product_data['category'] = category  # Re-add category for get_or_create
        product, created = Product.objects.get_or_create(**product_data)
        
        # Add random tags to each product (2-4 tags)
        selected_tags = random.sample(tags, random.randint(2, 4))
        product.tags.set(selected_tags)
        
        created_products.append(product)
        print(f"Product {'created' if created else 'already exists'}: {product.name}")
    
    return created_products

if __name__ == '__main__':
    print('Starting database population...')
    categories = create_categories()
    tags = create_tags()
    products = create_products(categories, tags)
    print('Database population completed!')