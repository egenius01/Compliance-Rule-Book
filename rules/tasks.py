from celery import shared_task
from celery import Celery, app
from celery.schedules import crontab
from django.core.mail import send_mail
from django.utils import timezone
from datetime import date, timedelta
from django.db.models import F


app = Celery()

def update(MasterRuleBook):
    init_date = [f.initial_date_of_rendition for f in MasterRuleBook.objects.filter(with_returns=True)]
    lead_days = [timedelta(days=f.lead_days) for f in MasterRuleBook.objects.filter(with_returns=True)]
    next_rendition_date = [init_date[i] + (lead_days[i]) for i in range(len(init_date))]
    if next_rendition_date == timezone.now():
        MasterRuleBook.initial_date_of_rendition =  next_rendition_date
        MasterRuleBook.save()

@shared_task
def send_mail_task(sender):
    send_mail('Celery Task Worked',
              ' Just Posted a Rule Proof Kindly Authenticate',
              sender,
              ['reciever'])
    return None


@shared_task
def change_task(Upload,MRB):
       for Uploads in Upload:
           if Upload.approved == True:
                send_mail('Celery Task Worked',
                          ' Just Posted a Rule Proof Kindly Authenticate',
                          'sender',
                          ['upload.owner'])
                return None
@app.task
def alert_task(MasterRuleBook):
    init_date = [f.initial_date_of_rendition for f in MasterRuleBook.objects.filter(with_returns=True)]
    lead_days = [timedelta(days=f.lead_days) for f in MasterRuleBook.objects.filter(with_returns=True)]
    next_rendition_date = [init_date[i] + (lead_days[i]) for i in range(len(init_date))]
    n = [True for n in next_rendition_date if n <= timedelta(days=3) + timezone.now()]
    f = [c for c in n if c == MasterRuleBook.filter(next_rendition_date = c)]
    for a in n:
        if a==True:
            send_mail('ALERT',
                      ' Kindly be reminded that a rule is to be due in less than three days ',
                      'to',
                      ['reciever'])
            return None


#add "alert_tasks" to the beat schedule
app.conf.beat_schedule = {
    "alert mail Task" : {
        "task":"alert_task",
        "schedule":crontab(hour=13,minute=58)
    }
}



def alert_some(MasterRuleBook,Upload):
    init_date = [f.initial_date_of_rendition for f in MasterRuleBook.objects.filter(with_returns=True)]
    uploads1 = [f.returns.initial_date_of_rendition for f in Upload.objects.filter(approved=True)]
    print (uploads1)



# #add "alert_tasks" to the beat schedule
# app.conf.beat_schedule = {
#     "date change Task" : {
#         "task":"alert_some",
#         "schedule":crontab(hour=13,minute=58)
#     }
# }



#
# @app.task
# def send():
#     send_mail('Celery Task Worked',
#               ' Just Posted a Rule Proof Kindly Authenticate',
#               'sender',
#               ['reciever'])
#     return None
#
# app.conf.beat_schedule = {
#     "see-you-in-ten-seconds-task": {
#         "task": "rules.tasks.send",
#         "schedule": 10.0
#     }
# }

        #
        # elif b==True:
        #     send_mail('Celery Task Worked',
        #               ' This rule will be due in three days kindly comply before the third day ',
        #               'sender',
        #               ['reciever'])
        #     return None
        #
        #
        # elif c ==True:
        #     send_mail('Celery Task Worked',
        #               ' This rule will be due in three days kindly comply before the third day ',
        #               'sender',
        #               ['reciever'])
        #     return None
        #
        # #
        # else:
        #     return  None