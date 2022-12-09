from faker import Faker

dane = Faker("pl_PL")

print(dane.name())
print(dane.address())

for _ in range(10):
    # print(f"dane: {dane.name()}; adres: {dane.credit_card_full()}")
    print(f'{dane.name()}; {dane.street_prefix_short()}; {dane.street_name()}; {dane.building_number()}; '
          f'{dane.postcode()}; {dane.city()}; {dane.administrative_unit()}')