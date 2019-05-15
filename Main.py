from Note import Note
from Board import Board

board = Board('Kanban1')

board.add_note('Title 1', 'Description 1')
board.add_note('To be deleted')
board.add_note('Title 3', note_tags=['tag1', 'tag2'])
board.add_note('To be deleted again')

board.notes[2].add_tags(['tag3', 'tag4'])
board.notes[2].del_tags(['tag1', 'tag3'])

board.del_notes_index(board.index_notes_titled('deleted'))

print(board)