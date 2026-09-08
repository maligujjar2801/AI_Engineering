def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("User Information:")
show_info(Name="Ali", age=17, city="Faisalabad", country="Pakistan")