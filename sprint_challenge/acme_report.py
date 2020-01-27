import random
from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''
    should generate a given number of products (default30),
    randomly, and return them as a list
    '''
    products = []
    for _ in range(num_products):
        ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        adj_sample = random.sample(ADJECTIVES, 1)
        noun_sample = random.sample(NOUNS, 1)

        # using list comprehension + zip()
        # interlist element concatenation
        name_list = [f'{i} {j}'for i, j in zip(adj_sample, noun_sample)]

        name = name_list
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        # TODO - your code! Generate and add random products.
        prod = Product(name, price=price, weight=weight,
                       flammability=flammability)
        products.append(prod)
    return products


def inventory_report(products):
    unique_products = []
    total_weight = 0
    total_price = 0
    total_flammability = 0
    for product in products:
        if product.name not in unique_products:
            unique_products.append(product.name)

        total_weight += product.weight
        total_price += product.price
        total_flammability += product.flammability

    avg_weight = total_weight/len(products)
    avg_price = total_price / len(products)
    avg_flammability = total_flammability/len(products)

    print('\nACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(unique_products)}')
    print(f'Average Price: {avg_price:.1f}')
    print(f'Average Weight: {avg_weight:.1f}')
    print(f'Average Flammability: {avg_flammability:.1f}')


if __name__ == '__main__':
    inventory_report(generate_products())
