from django.shortcuts import render, get_object_or_404, redirect
from .models import Suspicious
from .forms import Alert_comment_form
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required()
def alert_not_reacted_view(request):
    alert = Suspicious.objects.filter(status =' ').order_by('-creation_date', 'ACCOUNT_CLASS',)
    undefined = Suspicious.objects.filter(status='UNDEFINED')

    page = request.GET.get('page', 1)
    paginator = Paginator(alert, 50)
    alert = paginator.get_page(page)

    context = {'alerts':alert,
               'undefined':undefined,
               }
    template_name = 'alert_not_reacted_list.html'
    return render(request, template_name, context)

@login_required()
def alert_undefined_view(request):
    alert = Suspicious.objects.filter(status='UNDEFINED',).order_by('-edit_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(alert, 50)
    alert = paginator.get_page(page)

    context = {'alerts': alert}
    template_name = 'alert_undefined_list.html'
    return render(request, template_name, context)


@staff_member_required()
def alert_true_positive_view(request):
    alert = Suspicious.objects.filter(status='TRUE POSITIVE').order_by('-edit_date')
    undefined = Suspicious.objects.filter(status='UNDEFINED')

    page = request.GET.get('page', 1)
    paginator = Paginator(alert, 100)
    alert = paginator.get_page(page)

    context = {'alerts': alert, 'undefined':undefined}
    template_name = 'alert_positive_list.html'
    return render(request, template_name, context)

@staff_member_required()
def alert_false_positive_view(request):
    alert = Suspicious.objects.filter(status='FALSE POSITIVE').order_by('-edit_date')
    undefined = Suspicious.objects.filter(status='UNDEFINED')

    page = request.GET.get('page', 1)
    paginator = Paginator(alert, 100)
    alert = paginator.get_page(page)

    context = {'alerts': alert,
               'undefined':undefined}
    template_name = 'alert_false_list.html'
    return render(request, template_name, context)

@login_required()
def alert_detail(request, id):
    alerts = get_object_or_404(Suspicious, id=id)
    undefined = Suspicious.objects.filter(status='UNDEFINED')

    context = {'alerts': alerts,
               'undefined':undefined}
    template_name = 'alert_details.html'
    return render(request, template_name, context)

@login_required()
def update_alert(request, id):
    alerts = get_object_or_404(Suspicious, id=id)
    forms = Alert_comment_form(request.POST or None, instance=alerts)
    undefined = Suspicious.objects.filter(status='UNDEFINED')

    if forms.is_valid():
        alerts.user = request.user
        alerts.edit_date = datetime.datetime.now()
        forms.save()
        forms = Alert_comment_form()
        return redirect('not_reacted')

    template_name = 'forms.html'
    context = {'alerts': alerts,
               'forms': forms,
               'undefined':undefined}
    return render(request, template_name, context)




