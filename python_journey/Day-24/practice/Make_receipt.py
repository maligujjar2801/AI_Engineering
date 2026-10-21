def make_receipt(customer,*items,discount = 0, **metadata):
    receipt = {
        "name": customer,
        "items": items,
        "Discount": discount,
        "Metadata": metadata
    }
    return receipt # Returns a receipt dictionary with customer name, items, discount, and metadata.

