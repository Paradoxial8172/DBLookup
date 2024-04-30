
class NewUser():
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        
    def get_values(self):
        return (self.first_name, self.last_name, self.phone, self.email)
    