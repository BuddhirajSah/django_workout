from ast import arg
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
#%%
#Dictionary mapping
monthly_challenges = {
    'january' : 'This is the first month of the year,make sure your habits are intact.',
    'february': 'Here is comes the month of lovers!!!',
    'march': 'march comes like a lion kya???',
    'april': 'Apun ka birthday aa re la hai bhai',
    'may' : 'May i come in sir ??',
    "june" : "Garmi ka mausam aaya -- Darmi Cool Ads",
    'july': 'Abhi to barish suru hui hai',
    'august' : 'Hmm August 15 will be a holiday dont worry!!',
    'september':'Four more months to go>>>',
    'october':'My love anniversary on Oct 11th',
    'november': 'Tor wife banbar lagi - e janbaby aasi gala!!',
    'december':'Christmas is coming on 25th.'
}
#%%
# Create your views here.
def index(request):
    list_items =""
    months =list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge",args=[month])
        list_items += f'<li><a href=\"{month_path}\">{capitalized_month}</li>'
    #new shits
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)




def monthly_challenges_by_number(request,month):
    month_list = list(monthly_challenges.keys())
    if month > len(month_list):
        return HttpResponseNotFound('Invalid Month')
    redirect_month = month_list[month-1]
    redirect_path = reverse('month-challenge',args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
#The original monthly challenges code is here >> 

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month] #f"<h1>{challenge_text}</h1>" 
        return render(request,"challenges/challenge.html",
                       {'text': challenge_text ,
                        'month_name' : month.capitalize()
                       }
                     )
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Make sure this is an appropriate month or in the list of months.</h1>")
    #return HttpResponse(response_text)







