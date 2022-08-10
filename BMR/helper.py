import configparser

subject_file = configparser.ConfigParser()

subject_file.add_section("Male")
subject_file.set("Male", "Constant_For_Male", "88.362")
subject_file.set("Male", "Weight_Constant_For_Male", "13.397")
subject_file.set("Male", "Height_Constant_For_Male", "4.799")
subject_file.set("Male", "Age_Constant_For_Male", "5.677")

subject_file.add_section("Female")
subject_file.set("Female", "Constant_For_Female", "447.593")
subject_file.set("Female", "Weight_Constant_For_Female", "9.247")
subject_file.set("Female", "Height_Constant_For_Female", "3.098")
subject_file.set("Female", "Age_Constant_For_Female", "4.33")

subject_file["Conversion"]={"Pound":"2.204","foot" : "3.28"}

with open(r"Config.ini", 'w') as configfile:
    subject_file.write(configfile)