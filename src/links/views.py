from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Link
from .forms import AddLinkForm
from django.views.generic import DeleteView
import smtplib 
import time
# Create your views here.

def home_view(request):
    no_discounted = 0
    error = None
    
    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Uopa...ne mogu dohvatit ime ili cijenu"
        except:
            error = "Uopa...nesto je poslo po krivu"

    form = AddLinkForm()

    qs = Link.objects.all()
    items_no = qs.count()

    if items_no > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)

    if discount_list != []:
            send_mail()

    context = {
        'qs' : qs,
        'items_no' : items_no,
        'no_discounted' : no_discounted,
        'form' : form,
        'error' : error,
    }

    return render(request, 'links/main.html', context)

class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'links/confirm_del.html'
    success_url = reverse_lazy('home')

def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')


def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('karlozeko@gmail.com', 'oxwlrqyfhqjiftpy')

        subject = 'Cijena se promijenila'
        body = 'Provjeri amazon stranicu'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'karlozeko@gmail.com',

            'k_zeko@hotmail.com',
            msg


        )

        server.quit()








