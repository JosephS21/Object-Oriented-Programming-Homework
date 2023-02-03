# Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program
# The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.

class AmazonShoppingCart:
    
    def __init__(self):
        self.items = []
        
    def add_items(self):
        item = input('What item would you like to add? ')
        quantity = input('How many do you want? ')
        new_item = Items(item,quantity)
        self.items.append(new_item)
            
    def delete_items(self):
        delete_name = input('What item do you want to delete? ')
        for i in range(len(self.items)):
            if self.items[i].item.lower() == delete_name.lower():
                self.items.pop(i)
                print('Contact Deleted')
                return
            
        print(f'{delete_name} was not found.')
    
    def print_items(self):
        for product in self.items:
            print(f'{product.item}')
            print(f'Quantity: {product.quantity}')
    
    def run(self):
        while True:
            question = input('"Do you want to : Show, Add, Delete or Quit?" ').lower()
            if question == 'add':
                self.add_items()
            elif question == 'delete':
                self.delete_items()
            elif question == 'show':
                self.print_items()
            elif question == 'quit':
                self.print_items()
                print('All DONE!')
                return
            else:
                print('Incorect input, try again. ')
class Items:
    def __init__(self,item,quantity):
        self.item = item
        self.quantity = quantity
        
new_cart = AmazonShoppingCart()
new_cart.run()