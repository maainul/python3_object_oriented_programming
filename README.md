# Chaper 1

## Object-oriented?

```
An object is a collection of data and associated behaviors.
```
## what does it mean to be object-oriented?

```
Oriented simply means directed toward. So object-oriented simply means,
"functionally directed toward modeling objects".
```
## Object-oriented Analysis (OOA)

```
It is the process of looking at a problem, system, or
task that somebody wants to turn into an application
and identifying the objects and interactions between those objects.
Visitors to the website need to be able to (italic represents actions,
bold represents objects):
    • review our history
    • apply for jobs
    • browse, compare, and order our products
```
## Object-oriented Design (OOD)

```
The design stage is all about how things should be done.

It is the process of converting such requirements into an implementation specification.
 The designer must name the objects, define the
behaviors, and formally specify what objects can activate specific behaviors on
other objects.
```
## Object-oriented Programming (OOP)

```
OOP is the process of converting this perfectly
defined design into a working program that does exactly what the CEO
originally requested.
```
## Class

```
Classes describe objects
```
## Composition

```
Composition is the act of collecting together several objects to compose a new one.
Composition is usually a good choice when one object is part of another object.
We've already seen a first hint of composition in the mechanic example. A car is
composed of an engine, transmission, starter, headlights, and windshield, among
numerous other parts. The engine, in turn, is composed of pistons, a crank shaft, and
valves. In this example, composition is a good way to provide levels of abstraction.
```

## Inheritence

```
Inheritance is the most famous,
well-known, and over-used relationship in object-oriented programming.
Inheritance is sort of like a family tree. My grandfather's last name was Phillips and
my father inherited that name. I inherited it from him (along with blue eyes and a
penchant for writing). In object-oriented programming, instead of inheriting features
and behaviors from a person, one class can inherit attributes and methods from
another class.
```
# Chapter 2 (Objects in Python)

## Creating Python classes

```
class MyFirstclass:
    pass
```
## Class Name Rules:

```
    1.Must start with a letter or Underscore
    2.Can only be comprised of letters,underscores, on number
    3.Follow to CamelCase notation
```
## Adding attributes

```
    class Point():
        pass

    p1 = Point() #p1 is instance of class Point
    p2 = Point() #p2 is another instance of class Point()

    # <object>.<attribute> = <value>

    p1.x = 5
    p1.y = 4

    p2.x = 3
    p2.y = 6

    print(p1.x,p1.y)
    print(p2.x,p2.y)
```
## Make it Do Something

```
Add reset behavior into the class.So that the origin can be (0,0)

    class Point()
        def reset(self):
            self.x = 0
            self.y = 0

    p = Point()
    p.reset()
    print(p.x, p.y)
```

```
1. The one difference between methods and normal functions is that all methods
   have one required argument.
2. This argument is conventionally named self.
3. The self argument to a method is simply a reference to the object that the method
   is being invoked on.
2. Notice that when we call the p.reset() method, we do not have to pass the self
   argument into it. Python automatically takes care of this for us. It knows we're
   calling a method on the p object, so it automatically passes that object to the method.
```
## Add another arguments into function

```
    import math
    class point:
        def move(self,x,y):
            self.x = x
            self.y = y
        def reset(self):
            self.move(0,0)
        def calculate_distance(self,other_point):
            return math.sqrt(
                (self.x - other_point.x)**2 +
                (self.y - other_point.y)**2
                )

        # use it
        point1 = Point()
        point2 = Point()
        p1.reset()
        point2.move()
        point2.move(5,0)
        print(point2.calculate_distance(point1))
        assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))
        point1.move(3,4)
        print(point1.calculate_distance(point2))
```
## Explaining yourself

```
    import math
    class Point:
    'Represents a point in two-dimensional geometric coordinates'
        def __init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y
           coordinates can be specified. If they are not, the point
           defaults to the origin.'''
        self.move(x, y)
        def move(self, x, y):
        "Move the point to a new location in two-dimensional space."
            self.x = x
            self.y = y
        def reset(self):
        'Reset the point back to the geometric origin: 0, 0'
            self.move(0, 0)
        def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second point
            passed as a parameter.This function uses the Pythagorean Theorem
            to calculate the distance between the two points. The distance is returned
            as a float."""
            return math.sqrt(
                        (self.x - other_point.x)**2 +
                        (self.y – other_point.y)**2)

        # use it
        point1 = Point()
        point2 = Point()
        p1.reset()
        point2.move()
        point2.move(5,0)
        print(point2.calculate_distance(point1))
        assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))
        point1.move(3,4)
        print(point1.calculate_distance(point2))
```
## Case Study

```
    import datetime

    # store the next available id for all new notes

    class Note:
        '''Represent a note in the notebook.Match against
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
            Search is case sensetive and matches both text and tags.'''
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
```
```
    import sys
    from notebook import Note,Notebook


    class Menu:
        '''Display a menu and respond to choices when run.'''
        def __init__(self):
            self.notebook = Notebook()
            self.choices = {
                "1": self.show_notes,
                "2": self.search_notes,
                "3": self.add_note,
                "4": self.modify_note,
                "5": self.quit
            }

        def display_menu(self):
            print("""
                Notebook Menu

                1. Show all notes
                2.Search Notes
                3.Add Notes
                4.Modify Notes
                5.Quit
                """)

        def run(self):
            '''Display the menu and respond to choices.'''
            while True:
                self.display_menu()
                choice = input("Enter an option:")
                action = self.choices.get(choice)
                if action:
                    action()
                else:
                    print("{0} is not a valid choice".format(choice))

        def show_notes(self,notes=None):
            if not notes:
                notes = self.notebook.notes
            for note in notes:
                print("{0}: {1}\n{2}".format(note.id,note.tags,note.memo))

        def search_notes(self):
            filter = input("search for:")
            notes = self.notebook.search(filter)
            self.show_notes(notes)

        def add_note(self):
            memo = input("Input a memo:")
            self.notebook.new_note(memo)
            print("Your note has been added.")

        def modify_note(self):
            id = input("Enter a note id :")
            memo = ("Enter a memo:")
            tags = input("Enter tags:")
            if memo:
                self.notebook.modify_memo(id,memo)
            if tags:
                self.notebook.modify_tags(id,tags)

        def quit(self):
            print("Thank you for using your notebook today.")
            sys.exit(0)

    if __name__ == "__main__":
        Menu().run()
```
# Chapter 3 (When Objects are Alike)

## Basic inheritance

```
1.every class we create uses inheritance.
2.All Python classes are subclasses of the special class named object .
3.This class provides very little in terms of data and
  behaviors (those behaviors it does provide are all double-underscore methods intended for internal use only)
4.A superclass, or parent class, is a class that is being inherited from.
5.A subclass is a class that is inheriting from a superclass.
```
```
    class Contact:
        all_contact = []
        def __init__(self,name,email):
            self.name = name
            self.email = email
            Contact.all_contact.append(self)
    class Supplier(Contact):
        def order(self,order):
            print("If this were a real system we would send " "{} order to {}".format(order,self.name))

>>> c = Contact("Some Body", "somebody@example.net")
>>> s = Supplier("Sup Plier", "supplier@example.net")
>>> print(c.name, c.email, s.name, s.email)
Some Body somebody@example.net Sup Plier supplier@example.net

```

```
class ContactList(list):
    def search(self, name):
    '''Return all contacts that contain the search value
    in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
class Contact:
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

Instead of instantiating a normal list as our class variable, we create a new
ContactList class that extends the built-in list . Then we instantiate this subclass
as our all_contacts list. We can test the new search functionality as follows:

>>> c1 = Contact("John A", "johna@example.net")
>>> c2 = Contact("John B", "johnb@example.net")
>>> c3 = Contact("Jenna C", "jennac@example.net")
>>> [c.name for c in Contact.all_contacts.search('John')]
['John A', 'John B']
```
## Overriding and Super

```
Overriding is altering or replacing a method of the superclass
with a new method (with the same name) in the subclass.
Let's create a class called Friend and override methods.
```
```
	class Friend(Contact):
		def __init__(self,name,email,phone):
			self.name = name
			self.email = email
			self.phone = phone

	class Contact:
	    all_contacts = ContactList()
	    def __init__(self, name, email):
		self.name = name
		self.email = email
		self.all_contacts.append(self)
```

```
Our Contact and Friendclasses have duplicate code to set up
the name and email properties; this can make maintenance complicated,
as we have to update the code in two or more places.
More alarmingly, our Friend class is neglect
```

```
class Friend(Contact):
	def __init__(self,name,email,phone):
		super().__init__(name,email)
		self.phone = phone
```
```
A super() call can be made inside any method, not just __init__ .
This means all methods can be modified via overriding and calls to super
```
## Multiple inheritance

```
a subclass that inherits from more than one parent class is
able to access functionality from both of them.
The simplest and most useful form of multiple inheritance is called a mixin.
A mixinis generally a superclass that is not meant to exist on its own,
but is meant to be inherited by some other class to provide extra functionality.
```
```
  class AddressHolder:
    def __init__(self,street,city,state,code):
      self.street = street
      self.city = city
      self.state=state
      self.code = code
```
# The Diamond Problem

```
  class Friend(Contact,AddressHolder):
    def __init__(self,name,email,phone,street,city,state,code):
      Contact.__init__(self,name,email)
      AddressHolder.__init__(self,street,city,state,code)
      self.phone = phone
      
```
# Convert Into superclass

```
  class Contact:
      all_contacts = []

      def __init__(self,name='',email='',**kwargs):
          super().__init__(**kwargs)
          self.name = email
          self.email = email
          self.all_contacts.append(self)

  class AddressHolder:
      def __init__(self,street='',city='',state='',code='',**kwargs):
          super().__init__(**kwargs)
          self.street = street
          self.city = city
          self.state = state
          self.code = code

  class Friend(Contact,AddressHolder):
      def __init__(self,phone='',**kwargs):
          super().__init__(**kwargs)
          self.phone = phone
  ```
