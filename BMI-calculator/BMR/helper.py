def subject_read():
    subject_file.add_section("Gender")
    subject_file.add_section("Units")
    subject_file.add_section("Conversion")
    subject_file.set("Gender","Male","Metric")
    subject_file.set("Gender", "Male", "Metric")
    subject_file.set("Unit", "Male", "Weight")
    subject_file.set("Unit", "Male", "Height")
    subject_file.set("Unit", "Male", "Age")
    subject_file.set("Unit", "Female", "Weight1")
    subject_file.set("Unit", "Female", "Height1")
    subject_file.set("Unit", "Female", "Age1")
    read_file = open("Config.ini", "r")

    '''with open("Config.ini") as subjectfileObj:
        subject_file.write(subjectfileObj)
        subjectfileObj.flush()
        subjectfileObj.close()
        print("subject file 'Config.ini' is created")'''

    read_file = open("Config.ini", "r")
    content = read_file.read()
    print("Content of the config file are:\n")
    print(content)
    read_file.flush()
    read_file.close()
    contents = read_file.read()
    config = eval(contents)
    Gender = config['Gender']
    Units = config['Units']
    Conversion = config['Conversion']
    print(Gender)
    print(Units)
    print(Conversion)
    return (Gender, Units, Conversion)
    print(Gender.keys())
    print(Units.keys())
    print(Conversion.keys())