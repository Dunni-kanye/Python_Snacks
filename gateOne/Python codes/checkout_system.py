from datetime import datetime

def checkout_system():
    customer_name = input("What is the customer's name? ")

    product_names = []
    product_prices = []
    product_quantities = []

    now = datetime.now()
    formatted_datetime = now.strftime("%d-%m-%Y %H:%M:%S")
    flag = ""

    while flag.lower() != "no":
        product_name = input("What did the user buy? ")
        product_names.append(product_name)

        quantity = int(input("How many pieces? "))
        product_quantities.append(quantity)

        price = float(input("How much per unit? "))
        product_prices.append(price)

        flag = input("Add more items? (yes/no) ")

    cashier_name = input("What is the cashier's name? ")

    vat_rate = 0.175
    discount_rate = 0.0

    sub_total = sum(price * quantity for price, quantity in zip(product_prices, product_quantities))
    print(f"Subtotal calculated: {sub_total:.2f}")

    discount_rate = float(input("How much discount do you want to give (%): "))
    discount = sub_total * (discount_rate / 100)

    vat = sub_total * vat_rate
    total = sub_total - discount + vat

    amount_paid = float(input("Amount Paid: "))
    balance = amount_paid - total

    print(f"\nSEMICOLON STORES")
    print(f"MAIN BRANCH")
    print(f"LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")
    print(f"TEL: 0329382843")
    print(f"Date and Time: {formatted_datetime}")
    print(f"Cashier: {cashier_name}")
    print(f"Customer Name: {customer_name}")
    print("====================================================================================")

    print("ITEM              QTY    PRICE   TOTAL (NGN)")
    print("-------------------------------------------------------------------------------------")

    for product_name, quantity, price in zip(product_names, product_quantities, product_prices):
        item_total = price * quantity
        print(f"{product_name:<18} {quantity:<5} {price:>7.2f} {item_total:>12.2f}")

    print("------------------------------------------------------------------------------------------")
    print(f"{'Sub Total:':<28} {sub_total:>12.2f}")
    print(f"{'Discount:':<28} {discount:>12.2f}")
    print(f"{'VAT @ 17.5%:':<28} {vat:>12.2f}")
    print("=" * 60)
    print(f"{'Bill Total:':<28} {total:>12.2f}")
    print(f"{'Amount Paid:':<28} {amount_paid:>12.2f}")
    print(f"{'Balance:':<28} {balance:>12.2f}")
    print("============================================================================================")
    print("THANK YOU FOR YOUR PATRONAGE")
    print("-------------------------------------------------------------------------------------------")

checkout_system()
