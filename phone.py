import webbrowser
import phonenumbers
from my_phone import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

my_number = number()
p_num = phonenumbers.parse(my_number)



# Get the location description
loco = geocoder.description_for_number(p_num, "en")
print(loco)

# Get the service provider information
service_prov = phonenumbers.parse(my_number)
print(carrier.name_for_number(service_prov, "en"))

# Set up OpenCageGeocode
key = "304a62f3f7474a63875b2478be56953a"
geocoder_ocg = OpenCageGeocode(key)

# Use the original phone number for geocoding
query =my_number
result = geocoder_ocg.geocode(query)

# Check if the result is not empty before accessing its elements
if result:
    lat = result[0]["geometry"]["lat"]
    lng = result[0]["geometry"]["lng"]
    print(lat, lng)

    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
    webbrowser.open(google_maps_url)
else:
    print("Geocoding failed. No location found for the given query.")