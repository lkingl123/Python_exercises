import HW as hw

parts = hw.Parts()
parts.fetch()
#
# parts.add("Dr Pepper")
# parts.add("Headphones")
# parts.add("MacBook Pro")
#
# print(parts.fetch(None, "Headphones"))
# print(parts.fetch(3))
# print(parts.fetch())


inventory = hw.Inventory()
# # inventory.reset_database()
# inventory.add_inv("Bottled water", 24, "1.50")
# inventory.update_inv(1, 10, "1.99")
print(inventory.fetch_inv(1))
print(inventory.fetch_inv())
inventory.delete_inv(1)
print(inventory.fetch_inv())
