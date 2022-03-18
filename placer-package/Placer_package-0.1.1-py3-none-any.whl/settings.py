import os

# sets the main
settings_file = 'settings.txt'
attributes = ["NAME", "AGE", "GENDER"]


if settings_file not in os.listdir():
    with open(settings_file, 'w') as file:
        file.write("This is the settings file" + 3 * "\n")
        for i in attributes:
            file.write(i + 3 * "\n")


def setting(setting, value):
    global settings_file
    current_settings = open(settings_file, 'r').readlines()
    setting += "\n"

    for lines in current_settings:

        if setting.lower() == lines.lower():
            current_settings[current_settings.index(lines) + 1] = value + "\n"

            open(settings_file, 'w').writelines(current_settings)

            break


# _0884
