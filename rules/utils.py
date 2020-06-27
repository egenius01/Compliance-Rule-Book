from datetime import datetime, timedelta, date
from .models import MasterRuleBook

def alertDays(MasterRuleBook):
    next = MasterRuleBook.next_rendition_date() - timedelta(days= 4)
