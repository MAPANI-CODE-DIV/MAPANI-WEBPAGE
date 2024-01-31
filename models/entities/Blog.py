class Blog():
    def __init__(self,id,title,content,image,username,date_of_creation,last_modification) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.image = image
        self.username = username
        self.date_of_creation = date_of_creation
        self.last_modification = last_modification

        return