import datetime

class List:
    """docstring for List."""
    def __init__(self, title='new list', cards=[]):
        self.title = title
        self.cards = cards

    def add(self,card_text='new card', due_date=None):
        new_card = Card(card_text, due_date)
        self.cards.append(new_card)
        return(new_card)

    def total_time_elapsed(self):
        time= datetime.timedelta() #defaults to 0
        for card in self.cards:
            time = time + card.total_time_elapsed()
        return(time)


class Card:
    """docstring for Card."""

    def __init__(self, text, due_date=None):
        self.text = text
        self.due_date = due_date
        self.status = 'inactive' #status options are: active, inactive, complete
        self.log = []
        self.start_time = None

    def timer_start(self):
        self.start_time = datetime.datetime.now()
        self.status = 'active'
        return(self.start_time)

    def timer_end(self):
        tuple = (self.start_time, self.elapsed_time())
        self.log.append(tuple)
        self.status = 'inactive'
        self.start_time = None
        return(tuple[1])

    def elapsed_time(self):
        if self.start_time:
            current_time=datetime.datetime.now()
            elapsed_time=current_time - self.start_time #this gives a timedelta object not a number
            return(elapsed_time)
        else:
            return(None)#task hasn't been started

    def total_time_elapsed(self):
        total = datetime.timedelta() #defaults to 0
        for tuple in self.log:
            total = total + tuple[1]
        return(total)#returns a timedelta object
