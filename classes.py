import datetime


class User:
    """A MEMBER OF FRIENDFACE. FOR NOW WE ARE ONLY STORING THEIR NAME
    AND WE WILL STOR AN UN CONFORTABLE
    AMOUNT OF USER INFORMATION"""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        # EXTRACT FIRST AND LAST NAMES
        name_pieces = full_name.split(' ')
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """RETURN THE AGE OF THE USER IN YEARS."""
        today = datetime.date(2020, 8, 22)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)  # date of birth
        age_in_days = (today - dob).days
        age_in_year = age_in_days / 365
        return int(age_in_year), age_in_days


user = User(input('ENTER YOUR NAME: '), str(input('ENTER DATE OF BIRTH: EXAMPLE"YYYY, MM, DD": ')))
print(user.name, user.age())
help(User)