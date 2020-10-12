from .models import Location
LOCATIONS = [
    Location(1, "Uptown", "123 Main St N"),
    Location(2, "Midtown", "1 Main St"),
    Location(3, "Downtown", "321 Main St S")
]


def get_all_locations():
    all_locations = []
    for location in LOCATIONS:
        all_locations.append(location.__dict__)
    return all_locations

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location.id == id:
            requested_location = location.__dict__

    return requested_location

def create_location(new_location):
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1].id

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    new_location["id"] = new_id

    # Add the location dictionary to the list
    new_object = Location(new_id, new_location["name"], new_location["address"])
    LOCATIONS.append(new_object)

    # Return the dictionary with `id` property added
    return new_object.__dict__

def delete_location(id):
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the LOCATIONS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    # Iterate the LOCATIONS list, but use enumerate() so that
    # you can access the index value of each item.
    location_object = Location( id, new_location["name"], new_location["address"])
    for index, location in enumerate(LOCATIONS):
        if location.id == id:
            # Found the location. Update the value.
            LOCATIONS[index] = location_object
            break
