import phonenumbers
from phonenumbers import geocoder
phone_number1= phonenumbers.parse("+919883921876")
phone_number2= phonenumbers.parse("+919883910434")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number))