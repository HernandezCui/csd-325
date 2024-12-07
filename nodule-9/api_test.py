import requests

# Ask user for a Pokémon name or ID
pokemon_id_or_name = input("Enter the Pokémon name or ID: ").lower()

# Make the API request
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name}/')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()

    # Print formatted Pokémon data
    print(f"Name: {data['name'].capitalize()}")
    print(f"ID: {data['id']}")
    print(f"Height: {data['height']} decimeters")
    print(f"Weight: {data['weight']} hectograms")
    
    # Print Pokémon types
    print("Types:", end=" ")
    for t in data['types']:
        print(t['type']['name'], end=" ")
    print()
    
    # Print Pokémon abilities
    print("Abilities:", end=" ")
    for ability in data['abilities']:
        print(ability['ability']['name'], end=" ")
    print()

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")