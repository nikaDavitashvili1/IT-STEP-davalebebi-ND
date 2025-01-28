from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = 'localhost'
port = '5432'
user = 'postgres'
password = 'zaqwsx123'
database = 'davaleba30'

base = declarative_base()

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

class Product(base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    quantity_in_stock = Column(Integer)

class CartItems(base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer)

class Order(base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False)
    total_amount = Column(Integer, nullable=False)

class OrderItem(base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    quantity = Column(Integer)
    price_per_item = Column(Float, nullable=False)

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_products():
    products = [
        Product(name='Banana', price=10, quantity_in_stock=100),
        Product(name='Pineapple', price=20, quantity_in_stock=10),
        Product(name='Apple', price=4.3, quantity_in_stock=200),
        Product(name='Pear', price=5.6, quantity_in_stock=98),
        Product(name='Tomato', price=7.7, quantity_in_stock=100),
        Product(name='Pomegranate', price=19, quantity_in_stock=23),
        Product(name='Shmanana', price=20999, quantity_in_stock=999),
    ]
    session.add_all(products)
    session.commit()

add_products()

# UI

def view_cart():
    cart_items = session.query(CartItems).all()
    if not cart_items:
        print('Your cart is empty.')
        return
    for cart_item in cart_items:
        product = session.query(Product).get(cart_item.product_id)
        print(f"{product.name} - {cart_item.quantity} units.")

def add_to_cart():
    product_id = int(input("Enter product id to add to the cart: "))
    quantity = int(input("Enter how many units of this product you want to add: "))
    product = session.query(Product).get(product_id)
    if not product:
        print('Invalid product id.')
        return
    if product.quantity_in_stock < quantity:
        print('Not enough units in stock.')
        return
    cart_item = session.query(CartItems).filter_by(product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItems(product_id=product_id, quantity=quantity)
        session.add(cart_item)
    product.quantity_in_stock -= quantity
    session.commit()

def remove_from_cart():
    product_id = int(input("Enter product id to remove from the cart: "))
    cart_item = session.query(CartItems).filter_by(product_id=product_id).first()
    if not cart_item:
        print('Product is not in your cart.')
        return
    product = session.query(Product).get(product_id)
    product.quantity_in_stock += cart_item.quantity
    session.delete(cart_item)
    session.commit()
    print('Product has been removed from your cart.')

def place_order():
    cart_items = session.query(CartItems).all()
    if not cart_items:
        print('Your cart is empty.')
        return
    total_amount = 0
    for cart_item in cart_items:
        product = session.query(Product).get(cart_item.product_id)
        total_amount += product.price * cart_item.quantity
    new_order = Order(order_date=datetime.now(), total_amount=total_amount)
    session.add(new_order)
    session.commit()
    for item in cart_items:
        order_item = OrderItem(order_id=new_order.id, product_id=item.product_id, quantity=item.quantity, price_per_item=session.query(Product).get(item.product_id).price)
        session.add(order_item)
        session.delete(item)
    session.commit()
    print(f'Your order has been placed. Order ID: {new_order.id}')

def view_orders():
    orders = session.query(Order).all()
    if not orders:
        print('No orders.')
        return
    for order in orders:
        print(f'Order ID: {order.id}, Date: {order.order_date}, Total Amount: {order.total_amount}')

def main():
    while True:
        print("\nMenu:")
        print("1. View Cart")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. Place Order")
        print("5. View Orders")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_cart()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            remove_from_cart()
        elif choice == '4':
            place_order()
        elif choice == '5':
            view_orders()
        elif choice == '6':
            print("Thank you for using the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
