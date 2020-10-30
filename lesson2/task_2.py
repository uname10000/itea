class Store:
    total_sold_items = 0

    def __init__(self, name, items_sold):
        self.store_name = name
        self.items_sold = items_sold
        Store.total_sold_items += items_sold

        print(f'Opening {self.store_name} selling: {self.items_sold}')

    def selling(self, amount):
        self.items_sold += amount
        Store.total_sold_items += amount

        print(f'{self.store_name} selling {amount} items')

    def show_sold_items(self):
        print(f'{self.store_name}: sold: {self.items_sold}')

    def get_total_sold_items(self):
        print(f'Total sold: {Store.total_sold_items}')


store1 = Store('store1', 10)
store2 = Store('store2', 20)
store1.show_sold_items()
store2.show_sold_items()
store1.get_total_sold_items()

print("-"*40)

store1.selling(5)
store2.selling(2)
store1.show_sold_items()
store2.show_sold_items()
store1.get_total_sold_items()

print("-"*40)

store3 = Store('store3', 50)
store1.show_sold_items()
store2.show_sold_items()
store3.show_sold_items()
store1.get_total_sold_items()
