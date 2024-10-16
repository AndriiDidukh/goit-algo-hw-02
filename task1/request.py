class Request:
    _id_counter = 0

    def __init__(self, name, description):
        Request._id_counter += 1
        self.id = Request._id_counter
        self.name = name
        self.description = description
