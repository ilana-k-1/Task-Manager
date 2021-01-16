
from list_and_card_def import List

list=List('test')
first_card = list.add()
second_card = list.add()
first_card.log = [(1610761985.0728917, 5),(1610761995.0728917, 4),(1610762010.0728917, 7)]
second_card.log = [(1610762015.0728917, 4), (1610762020.0728917, 2)]
list.save()
loaded_list = List('reloaded test')
print('LOADED LIST CARDS (before loading): \n%s' %loaded_list.cards)
loaded_list.load('test')
loaded_list.save()
print('LOADED LIST CARDS: \n%s' %loaded_list.cards)
