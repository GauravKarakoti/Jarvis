import webbrowser
import geocoder
from Speak2 import Speak
def system_locater():
    Speak("Fetching System location")
    def get_system_location():
        
        system_location = geocoder.osm('me')
        return system_location

    def open_location_in_browser(location):
        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={location.latlng[0]},{location.latlng[1]}"
        webbrowser.open(google_maps_url)

    def main():
        system_location = get_system_location()
        Speak("Your location is")
        open_location_in_browser(system_location)
        Speak(f"Latitude: {system_location.latlng[0]}, Longitude: {system_location.latlng[1]}")

    if __name__ == "__main__":
        main()




def asked_location():
    import webbrowser
    Speak("which Location do you want to find ")
    def get_user_location():
        location = input("Enter the location : ")
        Speak("Fetching")
        return location
        

    def open_location_in_browser(location):
        google_maps_url = f"https://www.google.com/maps/search/{location}"
        webbrowser.open(google_maps_url)

    def main():
        user_location = get_user_location()
        Speak("sir please see what i found ")
        open_location_in_browser(user_location)

    if __name__ == "__main__":
        main()