from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices,sorting_choices

import math as m
from .models import Listing
# Create your views here.


def for_lab1(request):
    if 'val1' in request.GET:
        try:
            x = float(request.GET['val1'])
            result = ((5 * x**3) + 1)/(m.e**x + m.sin(m.cos(m.tan(x))))
            result = float(round(result, 3))
            context = {
                'result': result,
                'values': request.GET
            }
            return render(request, 'listings/new.html', context)
        except:
            print('here')
            return render(request, 'listings/new.html')

    if 'osn1' and 'osn2' and 'stor1' and 'stor2' in request.GET:
        try:
            osn1 = float(request.GET['osn1'])
            osn2 = float(request.GET['osn2'])
            stor1 = float(request.GET['stor1'])
            stor2 = float(request.GET['stor2'])
            height = 5
            sqr = ((osn1 + osn2)/2) * height
            context = {
                'resul': sqr,
                'values': request.GET
            }
            return render(request, 'listings/new.html', context)
        except:
            return render(request, 'listings/new.html')

    else:
        return render(request, 'listings/new.html')


def for_lab3(request):
    if 'size' in request.GET:
        try:
            x = float(request.GET['size'])
            x1 = float(request.GET['size1'])
            x2 = float(request.GET['size2'])
            s = x**2 - (x1*x2)*4
            if s < 0:
                s = 0
            context = {
                'result': s,
                'values': request.GET
            }
            return render(request, 'listings/lab3.html', context)
        except:
            return render(request, 'listings/lab3.html')

    if 'mas1' and 'mas2' in request.GET:
        try:
            m1 = str(request.GET['mas1'])
            m2 = str(request.GET['mas2'])
            m1 = m1.split()[:7]
            m2 = m2.split()[:7]
            c1 = []
            c2 = []
            for x in m1:
                if int(x) > 0:
                    c1.append(x)
            for x in m2:
                if int(x) > 0:
                    c2.append(x)
            if len(c1) > len(c2):
                result = len(c2)
            else:
                result = len(c1)

            context = {
                'resul': result,
                'values': request.GET
            }
            return render(request, 'listings/lab3.html', context)
        except:
            return render(request, 'listings/lab3.html')

    else:
        return render(request, 'listings/lab3.html')


def for_lab2(request):
    if 'str' in request.GET:
        try:
            s = str(request.GET['str'])
            result = s.split()
            result.sort()
            result = " ".join(result)
            context = {
                'result': result,
                'values': request.GET
            }
            return render(request, 'listings/lab2.html', context)
        except:
            return render(request, 'listings/lab2.html')

    elif 'str1' in request.GET:
        try:
            s = str(request.GET['str1'])
            result = s.split('. ')
            ls = []
            for x in result:
                for i in x:
                    if x.count(i) == 4:
                        ls.append(i)

            result = " ".join(set(ls))
            context = {
                'resul': result,
                'values': request.GET
            }
            return render(request, 'listings/lab2.html', context)
        except:
            return render(request, 'listings/lab2.html')

    elif 'str2' in request.GET:
        try:
            s = str(request.GET['str2'])
            s = s.replace('&', '@')
            context = {
                'result1': s,
                'values': request.GET
            }
            return render(request, 'listings/lab2.html', context)
        except:
            return render(request, 'listings/lab2.html')

    else:
        return render(request, 'listings/lab2.html')


def for_lab4(request):
    if 'num' in request.GET:
        try:
            s = str(request.GET['num'])
            result = []
            for x in s:
                result.append(x)
            leng = len(result)
            sum = 0
            for x in result:
                sum += int(x)
            status = 'Ne vhodit'
            if '3' in result:
                status = 'Vhodit'
            context = {
                'result': {
                    'sum': str(sum),
                    'vhod': status,
                    'len': str(leng)
                },
                'values': request.GET
            }
            return render(request, 'listings/lab4.html', context)
        except:
            return render(request, 'listings/lab4.html')

    if 'mas1' in request.GET:
        try:
            m1 = str(request.GET['mas1'])
            m1 = m1.split()
            c1 = []

            for x in range(len(m1)-1):
                c1.append(int(m1[x]) + int(m1[x+1]))

            minx = min(c1)

            context = {
                'resul': str(minx),
                'values': request.GET
            }
            return render(request, 'listings/lab4.html', context)
        except:
            return render(request, 'listings/lab4.html')

    if 'mas2' in request.GET:
        # try:
            m1 = str(request.GET['mas2'])
            m1 = m1.split()
            c1 = []

            for x in range(len(m1)):
                if int(m1[x]) != 0:
                    c1.append(str(x))

            context = {
                'result1': ' '.join(c1),
                'values': request.GET
            }
            return render(request, 'listings/lab4.html', context)
        # except:
        #     return render(request, 'listings/lab4.html')

    else:
        return render(request, 'listings/lab4.html')

def index(request):
    listings = Listing.objects.order_by('-price').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'listings': paged_listings,
        'sorting_choices': sorting_choices
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('list_date')

    if 'sorting' in request.GET:
        sort = request.GET['sorting']
        if sort == 'price_by_raising':
            queryset_list = Listing.objects.order_by('price')

        if sort == 'price_by_down':
            queryset_list = Listing.objects.order_by('-price')

        if sort == 'older_first':
            queryset_list = Listing.objects.order_by('list_date')

        if sort == 'new_first':
            queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
            
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
            
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices, 
        'listings': queryset_list,
        'sorting_choices': sorting_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)