import faker

fake = faker.Faker()

def generate_random_name():
    return fake.name()
