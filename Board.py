from Note import Note

class Board(object):
    name = ''
    notes = []

    def __init__(self, name=''): 
        self.name = name

    def add_note(self, note_name='', note_description='', note_tags=[]):
        note = Note(note_name, note_description, note_tags)
        self.notes.append(note)

    def del_notes_index(self, index):
        index.sort(reverse=True) #deleting backwards to preserve original index
        for i in index:
            self.notes.pop(i)

    def __str__(self):
        text = self.name
        for note in self.notes:
            text = text + '\n' + str(note)

        return text

    def notes_titled(self, substring):
        list_notes = []
        for note in self.notes:
            if substring in note.title:
                list_notes.append(note)

        return list_notes

    def index_notes_titled(self, substring):
        index_notes = []
        for i in range(len(self.notes)):
            if substring in self.notes[i].title:
                index_notes.append(i)

        return index_notes

    def index_notes_tagged(self, substring):
        index_notes = []
        for i_note in range(len(self.notes)):
            for i_tag in range(len(self.notes[i_note].tags)):
                if substring in self.notes[i_note].tags[i_tag]:
                    index_notes.append(i_note)
                    break

        return index_notes