from .models.animal import Animal
import sqlite3
import json

ANIMALS = [
    Animal(1, "Snickers", "Dog", "Admitted", 1, 4),
    Animal(2, "Gypsy", "Dog", "Admitted", 1, 2),
    Animal(3, "Blue", "Cat", "Admitted", 2, 1)
]


def get_all_animals():
    # Open a connection to the database
    
    with sqlite3.connect("./kennels.db") as conn:
        print(conn)
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)



# Function with a single parameter
def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['name'], data['breed'], data['status'],
                        data['location_id'], data['customer_id'],
                        data['id'])

        return json.dumps(animal.__dict__)

def get_animals_by_location(location):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
          SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.location_id = ?
        """, ( location, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)

def get_animals_by_status(status):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
          SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.status = ?
        """, ( status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


def create_animal(new_animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1].id

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    new_animal["id"] = new_id

    # Add the animal dictionary to the list
    new_object = Animal(new_id, new_animal["name"], new_animal["species"], new_animal["status"], new_animal["location"], new_animal["customer"])
    ANIMALS.append(new_object)

    # Return the dictionary with `id` property added
    return new_object.__dict__

def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)

def update_animal(id, new_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    animal_object = Animal(new_animal["id"], new_animal["name"], new_animal["species"], new_animal["status"], new_animal["location_id"], new_animal["customer_id"])
    print(id, new_animal)
    for index, animal in enumerate(ANIMALS):
        print(animal.id)
        if animal.id == id:
            # Found the animal. Update the value.
            ANIMALS[index] = animal_object
            break
