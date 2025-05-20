from customer import Customer
from coffee import Coffee
from order import Order

def sample_data():
 
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all_orders.clear()
    

    c1 = Customer("Jett")
    c2 = Customer("Brimstone")
    
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    
    c1.create_order(coffee1, 5.0)
    c1.create_order(coffee2, 3.5)
    c2.create_order(coffee1, 4.5)
    
    return c1, c2, coffee1, coffee2

def test_relationships():
    jett, brimstone, latte, espresso = sample_data()
    
    print("\n=== Debug Output ===")
    print(f"{jett.name}'s orders: {len(jett.orders())} (should be 2)")
    print(f"{brimstone.name}'s coffees: {[c.name for c in brimstone.coffees()]} (should be ['Latte'])")
    print(f"Latte orders: {latte.num_orders()} (should be 2)")
    print(f"Latte avg price: {latte.average_price()} (should be 4.75)")
    
 
    aficionado = Customer.most_aficionado(latte)
    print(f"Latte aficionado: {aficionado.name if aficionado else 'None'} (should be Jett)")

if __name__ == "__main__":
    test_relationships()