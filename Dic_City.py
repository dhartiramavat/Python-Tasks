cities = ["Ahmedabad", "Surat", "Mumbai", "Delhi", "Pune"]

# Dictionary comprehension
city_length = {city: len(city) for city in cities}

print(city_length)