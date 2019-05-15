class Note(object):
    title = ''
    description = ''
    tags = []

    def __init__(self, title='', description='', tags=[]):
        self.title = title
        self.description = description
        self.tags = tags

    def __str__(self):
        text = str(self.title) + ', ' + str(self.description)
        for tag in self.tags:
            text += ', ' + str(tag)
            
        return text

    def add_tags(self, new_tags=[]):
        self.tags = self.tags + new_tags

    def del_tags(self, del_tags=[]):
        for tag in del_tags:
            self.tags.remove(tag)