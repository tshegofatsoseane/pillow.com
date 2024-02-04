from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Accommodation
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    # Get the search query from the URL parameters
    query = request.GET.get('q')
    
    # Fetch all accommodations from the database
    accommodations_list = Accommodation.objects.all()

    # If there's a search query, filter the accommodations list
    if query:
        accommodations_list = accommodations_list.filter(
            Q(residence_name__icontains=query) |
            Q(street_address__icontains=query) |
            Q(email__icontains=query) |
            Q(nearest_campus__icontains=query)
        )

    # Paginate the filtered accommodations list, showing 3 accommodations per page
    paginator = Paginator(accommodations_list, 3)
    
    # Get the page number from the URL parameters
    page_number = request.GET.get('page')
    
    try:
        # Try to fetch the requested page of accommodations
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # If the page parameter is out of range, show the last page
        page_obj = paginator.page(paginator.num_pages)

    # If it's a regular request, render HTML template
    return render(request, 'accommodations/index.html', {'page_obj': page_obj, 'query': query})
