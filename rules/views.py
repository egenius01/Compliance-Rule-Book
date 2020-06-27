from django.shortcuts import render, get_object_or_404,redirect
from .models import MasterRuleBook, Upload
from .forms import UploadForm, AuthenticateForm
from .filters import RuleFilter, RuleBookFilter,  AuthenticateFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date, timedelta
from .tasks import send_mail_task, change_task,alert_task, alert_some,update
from django.core.mail import send_mail
from django.contrib import messages

"""
this is the views where the templates are being rendered dynamically. 

"""

# Create your views here.

@login_required
def rule_list(request):
    rule_list = MasterRuleBook.objects.filter( with_returns = True ) # Import the returns list and filter with if returns are true.
    upload = Upload.objects.order_by('-published_date').last() # import the uploads and make the ordering the latest published return
    rule_filter = RuleFilter(request.GET, queryset=rule_list) #this renders the rule filter imported above from the filters.py
    update(MasterRuleBook)
    return render(request, "rule_list.html", {'filter' : rule_filter,
                                              'upload' : upload
                                              })
@login_required
def upload_list(request):
    M = MasterRuleBook.objects.all()
    upload = Upload.objects.order_by('-published_date').filter(approved=True) # import the uploads and make the ordering the latest published return and also filter by the approved uploads
    uploads = Upload.objects.order_by('-published_date').filter(approved=False)  # import the uploads and make the ordering the latest published return and also filter by the unapproved uploads
    upload_filter = AuthenticateFilter(request.GET, queryset= upload) #this renders the rule filter imported above from the filters.py
    alert_some(MasterRuleBook, Upload) #an alert function i created in tasks.py

    paginator = Paginator(uploads,2)
    page=request.GET.get('page',1)#this tells how the paginator works
    try:
        load = paginator.page(page)
    except PageNotAnInteger:
        load = paginator.page(1)#this is if the page requested is not an integer
    except EmptyPage:
        load = paginator.page(paginator.num_pages) #this checks if the page request is empty and it returns the max page_number i.e the amount of pages will be the max page number

    #return renders the html page template.
    return render(request, 'upload_list.html',{
        'uploads': load,
        'filter' : upload_filter,
    })




@login_required
def upload(request):
    #this renders and saves the form on submit
    if request.method =="POST":
        form = UploadForm(request.POST, request.FILES)#get the post or request files
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.posted_by = request.user
            # article.owner = Upload.objects.values("returns")
            article.save()
            send_mail_task(article.posted_by)

            # messages.success(request, f"Upload has been created for Approval: {username}")

            return redirect('upload_list')
    else:
        form = UploadForm()

    return render(request, 'upload.html', {
        'form' : form
    })

@login_required
def rulebook(request):
    #renders the rules without returns. #anywhere there's a rulebook in this app, it means rules without returns
    rule_list = MasterRuleBook.objects.filter(with_returns = False)
    rule_filter = RuleBookFilter(request.GET, queryset=rule_list)
    return render(request, "rulebook.html", {'filter': rule_filter})



@login_required
def rulebook_detail(request,pk):#this gets the id of the particular rule clicked on
    rule_list = get_object_or_404(MasterRuleBook, pk=pk)
    return render(request, 'rulebook_detail.html', {'rule_list':rule_list
                                                    })


@login_required
def rule_detail(request,pk):
    init_date = [f.initial_date_of_rendition for f in MasterRuleBook.objects.filter(with_returns = True,pk=pk)]
    lead_days = [timedelta(days=f.lead_days) for f in MasterRuleBook.objects.filter(with_returns=True, pk=pk)]
    next_rendition_date = [init_date[i] + (lead_days[i]) for i in range(len(init_date))]
    rule_list = get_object_or_404(MasterRuleBook, pk=pk)
    # officer = [f.Responsible_Officer for f in MasterRuleBook.objects.filter(with_returns=True,pk=pk)]
    alert_task(MasterRuleBook)
    return render(request, 'rule_detail.html', {'rule_list':rule_list,
                                                    'next':next_rendition_date
                                                    })

@login_required
#the function below is for the alert page a page that is for assertion if the functionality still works.
def alert(request):
    init_date = [f.initial_date_of_rendition for f in MasterRuleBook.objects.filter(with_returns=True)]
    lead_days = [timedelta(days=f.lead_days) for f in MasterRuleBook.objects.filter(with_returns=True)]
    next_rendition_date = [init_date[i] + (lead_days[i]) for i in range(len(init_date))]
    n = [n for n in next_rendition_date if n <= timedelta(days=3) + timezone.now()]
    d = [f for f in MasterRuleBook.objects.filter(with_returns=True) if f.initial_date_of_rendition == n]
    return render(request, 'alerts.html',{
        'date':n
                                          })
