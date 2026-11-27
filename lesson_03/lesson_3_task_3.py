from address import Address
from mailing import Mailing

# Адрес отправителя
from_addr = Address("101000", "Москва", "Тверская", "7", "15")

# Адрес получателя
to_addr = Address("190000", "Санкт-Петербург", "Невский проспект", "42", "8")

# Отправление
parcel = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=345.50,
    track="RA123456789RU",
)

# Вывод строго по формату из задания
print(
    f"Отправление {parcel.track} "
    f"из {parcel.from_address.index}, {parcel.from_address.city}, "
    f"{parcel.from_address.street}, {parcel.from_address.house} - {parcel.from_address.apartment} "
    f"в {parcel.to_address.index}, {parcel.to_address.city}, "
    f"{parcel.to_address.street}, {parcel.to_address.house} -{parcel.to_address.apartment}. "
    f"Стоимость {parcel.cost} рублей."
)