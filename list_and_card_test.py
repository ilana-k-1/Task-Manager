from list_and_card_def import List
from time import sleep

list = List('title')
print(list.title)
card = list.add('card')
print(list.cards)
print(card.text)
card.timer_start()
sleep(2)
print(card.elapsed_time())
print(card.status)
sleep(2)
card.timer_end()
print(card.log)
print(card.status)
print(card.elapsed_time())
