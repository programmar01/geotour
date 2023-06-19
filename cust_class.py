class Customer:
    def __init__(self, first, last, mail, phone):
        self.first = first
        self.last = last
        self.mail = mail
        self.phone = phone

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}')".format(self.first, self.last, self.mail, self.phone)