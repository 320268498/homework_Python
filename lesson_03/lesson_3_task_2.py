from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79123456701"),
    Smartphone("Samsung", "Galaxy S24", "+79123456702"),
    Smartphone("Xiaomi", "13T", "+79123456703"),
    Smartphone("Google", "Pixel 8", "+79123456704"),
    Smartphone("OnePlus", "12", "+79123456705"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")