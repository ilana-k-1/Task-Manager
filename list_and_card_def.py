import time #all time is handled in seconds since epoch!
import marshaller

class List:
    """docstring for List."""
    def __init__(self, title='new list'):
        self.title = title
        self.cards = []
        self.date_created = time.time() #gives us a float of secs since epoch

    def save(self):
        marshaller.save(self)
        return(0)

    def load(self, title):
        self.title = title
        data = marshaller.load(title)
        for dict in data:
            card = self.add(dict['text'], dict['due_date'], dict['status'], dict['date_created'])
            card.log = dict['log']

    def add(self,card_text='new card', due_date = None, status = 'inactive', date_created = time.time(), start_time = None):
        card_text = card_text.replace('|', '\174') #basic delimiter collision avoidance, this makes everything easier even if it feels a little blunt
        new_card = Card(card_text, due_date, status, date_created, start_time)
        self.cards.append(new_card)
        return(new_card)

    def total_time_elapsed(self):
        time= 0 #defaults to 0
        for card in self.cards:
            time = time + card.total_time_elapsed()
        return(time) #in seconds


class Card:
    """docstring for Card."""

    def __init__(self, text, due_date, status, date_created, start_time):
        self.text = text
        self.due_date = due_date
        self.status = status #status options are: active, inactive, complete
        self.log = [] #for some reason if we take as an argument it treats the default empty array presented in the argument as global as in all instances access the same one, so for marchalling we'll have to add this later
        self.start_time = start_time
        self.date_created = date_created

    def timer_start(self):
        self.start_time = time.time()
        self.status = 'active'
        return(self.start_time)

    def timer_end(self):
        tuple = None
        tuple = (self.start_time, self.elapsed_time())
        self.log.append(tuple)
        self.status = 'inactive'
        self.start_time = None
        return(tuple[1])

    def elapsed_time(self):
        if self.start_time:
            current_time=time.time()
            elapsed_time=current_time - self.start_time
            return(elapsed_time)
        else:
            return(None)#task hasn't been started

    def total_time_elapsed(self): #only counts logged time so does not include currently running timer
        total = 0 #defaults to 0
        for tuple in self.log:
            total = total + tuple[1]
        return(total)#returns a number of seconds
