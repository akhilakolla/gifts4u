from django.shortcuts import render
from django.http import HttpResponse
from appsd.models import Category,Gifts,Giftmapping

def index(request):
    return HttpResponse("haiiii first app")
def homes(request):
    r = render(request,'appsd/homes.html')
    return HttpResponse(r)       
def occs(request,pn):
    if pn == 'R':
       idgs = Gifts.objects.get(occasion_type = 'ramzan')
       idg = Gift.objects.get(occid = idgs.id)
def hyperl(request,pn):
    if pn == '1':
       idg = Gifts.objects.get(id = 5)
    ren = render(request, 'appsd/wdhpl.html',{'pren': idg})
    return HttpResponse(ren)   
def odiwali(request,pageno):
    if pageno == '1':
        id_c = Category.objects.get(category_type = 'Flowers')
        id_gm = Giftmapping.objects.get(catid = id_c.id)
        id_g = Gifts.objects.get(id = id_gm.id )
    rendered = render(request, 'appsd/odiwali.html', {'pp':id_g})
    return HttpResponse(rendered)
    
   
