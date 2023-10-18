from faker import Faker
# pip freeze > requirements.txt

fake = Faker()

name = fake.name()
email = fake.email()

print(name, email)