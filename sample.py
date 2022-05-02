

# # Open a text file named cities.txt in append mode.
# with open("cities.txt", "a") as cities_file:

#     # Print a city's name and information to the file.
#     print(city_name, file=cities_file)
#     print(f"{elevation}, {population}", file=cities_file)
#     print(f"{elevation}, {population}", file=cities_file)
#     print(f"{elevation}, {population}", file=cities_file)
first_name = input('First Name: ')
first_name_initial = first_name[0:2]
last_name = input('Last Name: ')
last_name_initial = last_name[0:2]


print(f'Initials: {first_name_initial}{last_name_initial}')