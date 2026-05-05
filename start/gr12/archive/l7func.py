#       Small Pizza - $10
#       Large Pizza - $15

def print_receipt(pizza_size, total):
    print(f"\nYour {pizza_size} pizza: ${total}")
    print("Thank you!")

def calculate_total(size):
    if size=="large":
        total=15
    elif size=="small":
        total=10
    return total

def get_discount(total):
    return total*0.95

if __name__=="__main__":
    size = "large"
    price = calculate_total(size)
    final_price = get_discount(price)
    print_receipt(size, final_price)
