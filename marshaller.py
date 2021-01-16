def save(list):
    string = ''
    cards_array = list.cards
    for card in cards_array:
        meta_line = "%s|%s|%s|%s" %(card.text, card.due_date, card.status, card.date_created)
        log_line = ''
        for tuple in card.log:
            log_entry = '%s,%s' %(tuple[0],tuple[1])
            log_line = log_line + ';' + log_entry
        string = string + '\n%s|%s' %(meta_line, log_line[1:])
    file = open("storage/lists/%s.txt" %list.title, 'w')
    file.write(string[1:])
    file.close()
    return(0)

def load(title): #this feels pretty inelegant and we'll probably find something better later
    file_path = "storage/lists/%s.txt" %title
    file = open(file_path,'r').readlines()
    card_data = []
    for line in file:
        data = line.split('|') #data is stored as: text|due_date|status|date_created|log
        pairs = data[4].split(';')
        log = []
        for pair in pairs:
            pair = pair.split(',')
            pair = (float(pair[0]), float(pair[1])) #makesure seconds is loaded as a number and not a string!
            log.append(pair)

        if data[1] == 'None':
            due_date = None
        else:
            due_date = float(data[1])

        card_data.append({'text' : data[0], 'due_date' : due_date, 'status' : data[2], 'date_created' : float(data[3]), 'log' : log})
    return(card_data)

def datetimeify(string):
    return(0)

def timedeltaify(string):
    return(0)
