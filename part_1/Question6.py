'''Your name left justified 15 spaces'''
name = "suraj"
space_name = f"{name:<15}"
print(f"'{space_name}'")


name = "Ashish"
space_name = name.ljust(15)
print(f"'{space_name}'")