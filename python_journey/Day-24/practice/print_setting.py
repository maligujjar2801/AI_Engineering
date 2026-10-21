def print_setting(**settings):
    for name, setting in settings.items():
        print(f"{name} : {setting}")

print_setting(theme = "dark", font = "Ariel" )