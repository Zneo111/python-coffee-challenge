# Python Coffee Challenge

This project models a simple coffee shop system using Python classes. It demonstrates object-oriented programming concepts such as relationships, class methods, and data encapsulation.

## Features
- **Customer**: Represents a customer with a name and their coffee orders.
- **Coffee**: Represents a coffee type, tracks all orders for that coffee, and provides statistics like average price.
- **Order**: Represents an order linking a customer, a coffee, and a price.

## Main Classes
- `Customer`:
  - Create new customers
  - Place orders for coffee
  - Retrieve all orders and coffees for a customer
  - Find the customer who spent the most on a specific coffee
- `Coffee`: 
  - Create new coffee types
  - Retrieve all orders and customers for a coffee
  - Get the number of orders and average price for a coffee
- `Order`: 
  - Create new orders (customer, coffee, price)
  - Validate order data

## Usage
Run the debug script to see sample data and relationships:

```bash
python debug.py
```

Sample output:
```
=== Debug Output ===
Jett's orders: 2 (should be 2)
Brimstone's coffees: ['Latte'] (should be ['Latte'])
Latte orders: 2 (should be 2)
Latte avg price: 4.75 (should be 4.75)
Latte aficionado: Jett (should be Jett)
```

## Project Structure
- `customer.py`: Customer class
- `coffee.py`: Coffee class
- `order.py`: Order class
- `debug.py`: Script to test and debug relationships
- `tests/`: Unit tests for all classes

## Running Tests
To run all tests:

```bash
pytest
```

## Notes
- Customer names must be 1-15 characters.
- Coffee names must be at least 3 characters and are immutable after creation.
- Order prices must be floats between 1.0 and 10.0.

---

This project is for educational purposes and demonstrates basic OOP and relationships in Python.