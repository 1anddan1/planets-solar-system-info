# Define a dictionary to hold planet data
planets = {
    "Mercury": {
        "mass": "3.30 × 10^23 kg",
        "distance_from_sun": "57.9 million km",
        "moons": [],
    },
    "Venus": {
        "mass": "4.87 × 10^24 kg",
        "distance_from_sun": "108.2 million km",
        "moons": [],
    },
    "Earth": {
        "mass": "5.97 × 10^24 kg",
        "distance_from_sun": "149.6 million km",
        "moons": ["Moon"],
    },
    "Mars": {
        "mass": "6.42 × 10^23 kg",
        "distance_from_sun": "227.9 million km",
        "moons": ["Phobos", "Deimos"],
    },
    "Jupiter": {
        "mass": "1.90 × 10^27 kg",
        "distance_from_sun": "778.5 million km",
        "moons": ["Io", "Europa", "Ganymede", "Callisto"],
    },
    "Saturn": {
        "mass": "5.68 × 10^26 kg",
        "distance_from_sun": "1.43 billion km",
        "moons": ["Titan", "Enceladus", "Rhea", "Iapetus"],
    },
    "Uranus": {
        "mass": "8.68 × 10^25 kg",
        "distance_from_sun": "2.87 billion km",
        "moons": ["Titania", "Oberon", "Umbriel", "Ariel"],
    },
    "Neptune": {
        "mass": "1.02 × 10^26 kg",
        "distance_from_sun": "4.50 billion km",
        "moons": ["Triton", "Proteus", "Nereid"],
    },
}


# Function to handle queries
def query_planets(question):
    if "pluto" in question:
        return "Pluto is not in the list of planets."

    display_attributes = []
    display_planet = ""

    question = question.strip().lower()
    for planet, info in planets.items():
        if planet.lower() in question:
            display_planet = planet
            if "everything" in question:
                display_attributes = ["mass", "distance_from_sun", "moons"]
            elif "mass" in question:
                display_attributes = ["mass"]
            elif "distance" in question:
                display_attributes = ["distance_from_sun"]
            elif "moons" in question:
                display_attributes = ["moons"]
            else:
                return "Sorry, I couldn't understand the question."
            break

    if display_planet == "":
        return "planet not found"

    display_attributes_string = "\n".join(
        [
            f"{attribute}: {planets[display_planet][attribute]}"
            for attribute in display_attributes
        ]
    )
    return f"Planet: {display_planet}:\n{display_attributes_string}"


question = input("Enter a question: ")
print(query_planets(question))
# Example queries
# print(query_planets("Tell me everything about Saturn?"))
# print(query_planets("How massive is Neptune?"))
# print(query_planets("Is Pluto in the list of planets?"))
# print(query_planets("How many monns oes the Earth have"))
