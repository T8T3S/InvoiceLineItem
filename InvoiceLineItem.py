def get_price():
    while True:
        try:
            price = float(input('Enter Price: '))
            return price
        except ValueError:
            print('Invalid decimal number. Please try again.')

def get_quantity():
    while True:
        try:
            quantity = int(input('Enter Quantity: '))
            return quantity
        except ValueError:
            print('Invalid integer number. Please try again.')
def print_info(price, quantity, total):
    print(f'\nPRICE:      {price: .2f}')
    print(f'QUANTITY:   {quantity}')
    print(f'TOTAL:      {total: .2f}')

if __name__ == "__main__":
    print('The Invoice Line Item Calculator\n')
    answer = 'y'
    while answer.lower() == 'y':
        price = get_price()
        quantity = get_quantity()
        total = price * quantity
        print_info(price, quantity, total)
        answer = input("Enter another line item? (y/n): ")
        print()
    print('Bye!')