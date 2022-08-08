import configparser

subject_file = configparser.ConfigParser()

subject_file.add_section("Male")
subject_file.set("Male", "a", "88.362")
subject_file.set("Male", "b", "13.397")
subject_file.set("Male", "c", "4.799")
subject_file.set("Male", "d", "5.677")

subject_file.add_section("Female")
subject_file.set("Female", "w", "447.593")
subject_file.set("Female", "x", "9.247")
subject_file.set("Female", "y", "3.098")
subject_file.set("Female", "z", "4.33")

subject_file["Conversion"]={
        "Pound":"2.2",
        "Inch" : "33.397"
        }
with open(r"Config.ini", 'w') as configfile:
    subject_file.write(configfile)