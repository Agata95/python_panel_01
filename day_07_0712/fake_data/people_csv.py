from faker import Faker

# Poniżej możliwość generowania losowych danych, by stworzyć losową bazę danych

faker = Faker()

# print(faker.name())
# print(faker.address())

for _ in range(10):
    print(f"data: {faker.name()};\naddress: {faker.address()}\n")

# Można stosować język Polski

faker_pl = Faker("pl_PL")

for _ in range(10):
    print(f"data: {faker_pl.name()};\naddress: {faker_pl.address()};\ncredit card: {faker_pl.credit_card_full()}")

# inne

for _ in range(10):
    print(f'company name: {faker_pl.company()},\nregon: {faker_pl.regon()},\nregistration date: {faker_pl.date(pattern = "%d-%m-%Y")}\n')


