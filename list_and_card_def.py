import datetime

class List:
    """docstring for List."""
    def __init__(self, title='newlist', cards=[]):
        self.title = title
        self.cards = cards

    def add(self,card_text, due_date=None):
        new_card = Card(card_text, due_date)
        self.cards.append(new_card)
        return(new_card)


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
            elapsed_time=current_time - self.start_time
            return(elapsed_time)
        else:
            return(None)#task hasn't been started
