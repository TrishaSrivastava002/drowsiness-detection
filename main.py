import phonenumbers
from myphone import num
import opencage
# from phonenumbers import geocoder
import geocoder


check_number=phonenumbers.parse(num)
number_location=geocoder.description_for_number(check_number,"en")

print(number_location) 

# To find service provider
from phonenumbers import carrier
service_provider=phonenumbers.parse(num)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
key="18941f47572347bd9268bb66f78618d4"
geocoder=OpenCageGeocode(key)
query=str(number_location)
result=geocoder.geocode(query)


