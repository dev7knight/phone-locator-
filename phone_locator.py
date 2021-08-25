import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


while True:

    number = input("please enter phone number with country code ")

    ch_number = phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(ch_number, "en"))

    service_number = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_number, "en"))

    last = input("press enter to exit")
    
    if last == "":
        break 
    







