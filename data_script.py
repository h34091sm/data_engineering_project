import json
import os
import csv

# Traverse Dictionary Helper Function
    # Retreive nested value from dictionary 
    # If key doesn't exist or if structure is not a dict, return None
def traverse_dict(d, *keys):
    for key in keys:
        if not isinstance(d, dict): # structure not a dict 
            return {}
        d = d.get(key, {}) # get key or empty dict if not found
    return d 

# Load Input JSON File
with open('orders.json/orders.json') as f:
    data = json.load(f)

# Output lists
all_events = []
all_orders = []
all_stores = []
all_billing = []
all_shipping = []
all_items = []


# for each datum in data, extract only the relevant information and store in lists
event_id = 1
for datum in data:
    # Event entity
    event = {
        "event_id": event_id,
        "event_name": datum.get('event_name')
    }
    all_events.append(event)

    # Order entity
    order = traverse_dict(datum, 'event_payload', 'order') 
    order_id = order.get('orderId')

    order_entry = {
        "order_id": order_id,
        "event_id": event_id,
        "total": traverse_dict(order, 'amounts', 'total'),
        "currency": order.get('currency'),
        "channel": order.get('channel'),
        "customer_reference": order.get('customerReference'),

    }
    all_orders.append(order_entry)

    # Store entity
    store = traverse_dict(datum, 'event_payload', 'store') 
    store_entry = {
        "store_id": store.get('id'),
        "store_name": store.get('name'),
        "event_id": event_id
    }
    all_stores.append(store_entry)

    # Billing details 
    billing = traverse_dict(order, 'billingDetails')
    billing_addr = billing.get('address', {})
    billing_entry = {
        "order_id": order_id,
        "customer_name": f"{billing.get('firstName', '')} {billing.get('lastName', '')}".strip(),
        "phone_number": billing.get('phone'),
        "address": ", ".join(filter(None, [
            billing_addr.get('line1'),
            billing_addr.get('city'),
            billing_addr.get('county'),
            billing_addr.get('country'),
            billing_addr.get('postcode')
        ]))
    }
    all_billing.append(billing_entry)

    # Shipping Details
    shipping = traverse_dict(order, 'shippingDetails') 
    shipping_addr = shipping.get('address', {})
    shipping_entry = {
        "order_id": order_id,
        "customer_name": f"{shipping.get('firstName', '')} {shipping.get('lastName', '')}".strip(),
        "phone_number": shipping.get('phone'),
        "address": ", ".join(filter(None, [
            shipping_addr.get('line1'),
            shipping_addr.get('city'),
            shipping_addr.get('county'),
            shipping_addr.get('country'),
            shipping_addr.get('postcode')
        ]))
    }
    all_shipping.append(shipping_entry)

    # List of line items 
    for item in order.get('lineItems', []):
        item_entry = {
            "item_id": item.get('id'),
            "order_id": order_id,
            "product_id": item.get('productId'),
            "quantity": item.get('quantity'),
            "total": traverse_dict(item, 'amounts', 'total')
        }
        all_items.append(item_entry)

    event_id += 1

# Make a dictionary of all tables
# Each table is a list of dictionaries, where each dictionary represents a row in the table
tables = {
    "events": all_events,
    "orders": all_orders,
    "stores": all_stores,
    "billing": all_billing,
    "shipping": all_shipping,
    "line_items": all_items
}

os.makedirs("output", exist_ok=True)


# write output data to CSV files in output directory
for name, records in tables.items():
    if not records:
        continue
    keys = records[0].keys()
    with open(f"output/{name}.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(records)

print("Data extraction complete. CSV files saved in /output.")
