import datetime

# store the next available id for all new notes

class Note:
    '''Represent a note in the notebook.Match aganinst
    a string in search and store tags for each note.'''
    def __init__(self,memo,tags=''):
        '''initialization a note with memo and optional 
        space-separated tags.Automatically set the notes 
        creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id 
        last_id += 1
        self.id = last_id

    def match(self,filter):
        '''Determine if this note matches the filter 
        text.Return true if it matches,False otherwise.
        Search is case sensative and matches both text and tags.'''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified and searched.'''
    def __init__(self):
        '''initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self,memo,tags=""):
        '''create a new note and add it to the list.'''
        self.notes.append(Note(memo,tags))

    def modify_memo(self,note_id, memo):
        '''Find the note and with the given id and change its 
        memo to the given value.'''
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self,note_id,tags):
        '''Find the note with the given id and change its 
        tags  to tee given value.'''
        for note in self.notes:
            if note in self.id == note_id:
                note.tags = tags
            break

    def search(self,filter):
        '''Find all notes that match the given filter
        string.'''
        return [note for note in self.notes if note.match(filter)]
