from faker import Faker
import random

fake = Faker("tr_TR")

with open("HastaVerisi.txt", "w", encoding="utf-8") as f:
    f.write("isim, soyisim, yas, il\n")
    for _ in range(499):
        isim = fake.first_name()
        soyisim = fake.last_name()
        yas = random.randint(1, 90)
        il = fake.city()
        f.write(f"{isim}, {soyisim}, {yas}, {il}\n")
