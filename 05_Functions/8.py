# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
# Function with **kwargs

#def print_kwargs(name, power):
    # print("Name: ", name, "Power: ", power)

# print_kwargs(name="Alice", power=5)  # Output: Name: Alice Power: 5
# print_kwargs(power=10, name="Bob")  # Output: Name: Bob Power: 10 

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(Pokemon = "Pikachu", Type = "Electric", Level = 25)  # Output: Pokemon: Pikachu, Type: Electric, Level: 25
print_kwargs(Name = "Ash", Age = 10, Region = "Kanto")  # Output: Name: Ash, Age: 10, Region: Kanto
print_kwargs(Country = "Japan", City = "Tokyo", Population = 13929286)  # Output: Country: Japan, City: Tokyo, Population: 13929286