import pymongo 
import backend
from backend.connect_data import database
from datetime import datetime

#defines variable for 'History' collection
history = database['History']

class History():
    @staticmethod
    def make_list():
        history_list = []
        for event in history.find():
            history_list.append(event)
        return history_list

    @staticmethod
    def add(event_type, group, debtor, creditor, amount, description):
        now = datetime.now()
        now_str = now.strftime('%d/%m/%Y %H:%M')
        new_event = {'type': event_type, 'group': group, 'debtor': debtor, 'creditor': creditor,
        'description': description, 'amount': amount, 'time': now_str}
        try:
            history.insert(new_event)
            return True
        except:
            return False
   
    @staticmethod
    def show(event):
        if event['type'] == 'expense':
            result = ('%s- %s gave %s %d$ for %s in %s group' %(event['time'], event['creditor'], event['debtor'], event['amount'], event['description'], event['group']))
        elif event['type'] == 'settle_up':
            if event['amount'] < 0:
                result = ('%s- %s and %s settled up (%s payed %d$)' %(event['time'], event['creditor'], event['debtor'], event['debtor'], -event['amount']))
            else:
                result = ('%s- %s and %s settled up (%s payed %d$)' %(event['time'], event['creditor'], event['debtor'], event['creditor'], event['amount']))
        else:
            return 'invalid event type'
        return result