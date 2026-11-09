def school_profile(**profile):
    print("name: ", profile["name"])
    print("location: ", profile["location"])
    print("students: ", profile["students"])
    print("teachers: ", profile["teachers"])
    if "establishment" in profile:
        print("establishment: ", profile["establishment"])
    else:
        print()

school_profile(name="Acadex International School", students=500, location="Makurdi", teachers="30")
school_profile(name="Future Leaders Academy", establishment=2015, location="Lagos", teachers=45, students=800)
