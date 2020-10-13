# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"

# What are the top 5 airports in terms of: Total freight by origin
class Top5AirportsFrtByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('origin_iata_code','origin_city_name') \
                                 .annotate(total_frt=Sum('freight')) \
                                 .order_by('-total_frt')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsFrtByDest(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_frt=Sum('freight')) \
                                 .order_by('-total_frt')[0:5]
    template_name="rankorder_list_destination.html"

# What are the top 5 airports in terms of: Total mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('origin_iata_code','origin_city_name') \
                                 .annotate(total_mail=Sum('mail')) \
                                 .order_by('-total_mail')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total mail by destination
class Top5AirportsMailByDest(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_mail=Sum('mail')) \
                                 .order_by('-total_mail')[0:5]
    template_name="rankorder_list_destination.html"

# What are the top 5 airports in terms of: Total distance by origin
class Top5AirportsDistanceByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('origin_iata_code','origin_city_name') \
                                 .annotate(total_dist=Sum('distance')) \
                                 .order_by('-total_dist')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total distance by destination
class Top5AirportsDistanceByDest(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_dist=Sum('distance')) \
                                 .order_by('-total_dist')[0:5]
    template_name="rankorder_list_destination.html"

# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"origin
    template_name="rankorder_list_origin_distance_month.html"

# Which airport reported the most passengers by month?
class TopPaxByMonth(ListView):
    context_object_name = "airport_list"origin
    template_name="rankorder_list_origin_passenger_month.html"

# Which airline reported the most freight carried?
class TopFreightByAirline(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_list_freight_airline.html"

# Which airline reported the most passengers carried?
class TopPaxByAirline(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_list_passenger_airline.html"

# Which airline reported the most mail carried?
class TopMailByAirline(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_list_mail_airline.html"

# Which airline reported the longest flight distance?
class TopDistanceByAirline(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_list_distance_airline.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

