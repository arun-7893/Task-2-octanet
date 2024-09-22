def add_item():
    item_name = input("Enter the item name: ")
    price = float(input(f"Enter the price for {item_name}: $"))
    quantity = int(input(f"Enter the quantity of {item_name}: "))
    return (item_name, price, quantity)

def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item[1] * item[2]
    return subtotal

def print_receipt(items, subtotal, tax_rate):
    print("\n--- Receipt ---")
    for item in items:
        print(f"{item[2]} x {item[0]} @ ${item[1]:.2f} = ${item[1] * item[2]:.2f}")
    
    tax = subtotal * tax_rate
    grand_total = subtotal + tax

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax ({tax_rate*100}%): ${tax:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")
    print("----------------")

def receipt_calculator():
    items = []
    tax_rate = 0.07  # 7% tax rate (can be modified)

    while True:
        print("\n1. Add item")
        print("2. Print receipt and exit")
        choice = input("Choose an option: ")

        if choice == "1":
            item = add_item()
            items.append(item)
        elif choice == "2":
            if not items:
                print("No items added!")
                continue
            subtotal = calculate_subtotal(items)
            print_receipt(items, subtotal, tax_rate)
            break
        else:
            print("Invalid choice. Please choose again.")

receipt_calculator()
