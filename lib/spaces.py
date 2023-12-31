class Spaces:
    def __init__(self, id, title, description, email_address, price_per_night, user_id):
        self.id = id
        self.title = title
        self.description = description
        self.email_address = email_address
        self.price_per_night = price_per_night
        self.user_id = user_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.title}, {self.description}, {self.email_address}, {self.price_per_night})"