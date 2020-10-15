from .models import Location
import sqlite3
import json

LOCATIONS = [
    Location(1, "Uptown", "123 Main St N"),
    Location(2, "Midtown", "1 Main St"),
    Location(3, "Downtown", "321 Main St S")
]


def get_all_locations():
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)

        # Initialize an empty list to hold all location representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Location class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

        # Use `json` package to properly serialize list as JSON
        return json.dumps(locations)

# Function with a single parameter
def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an location instance from the current row
        location = Location(data['name'], data['name'], data['address'])

        return json.dumps(location.__dict__)

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
