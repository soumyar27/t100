# urls.py
from django.urls import path
from . views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    TopDistanceByMonth         


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('top5frtorigin/',  
        Top5AirportsFrtByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Origin Airport"}
        ), 
        name="top5frtorigin"),
    path('top5frtdestination/',  
        Top5AirportsFrtByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport"}
        ), 
        name="top5frtdestination"),
    path('top5mailorigin/',  
        Top5AirportsMailByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}
        ), 
        name="top5mailorigin"),
    path('top5maildestination/',  
        Top5AirportsMailByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport"}
        ), 
        name="top5maildestination"),
    path('top5distanceorigin/',  
        Top5AirportsDistanceByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Origin Airport"}
        ), 
        name="top5distanceorigin"),
    path('top5distancedestination/',  
        Top5AirportsDistanceByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport"}
        ), 
        name="top5distancedestination"),
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
    path('toppassengers_month/',  
        TopPassengersByMonth.as_view(
            extra_context={'title': "Top Passengers by Month"}
        ), 
        name="toppassengers_month"),
    path('topfreight_airline/',  
        TopFreightByAirline.as_view(
            extra_context={'title': "Top Freight by Airline"}
        ), 
        name="topfreight_airline"),
    path('toppassengers_airline/',  
        TopPassengersByAirline.as_view(
            extra_context={'title': "Top Passengers by Airline"}
        ), 
        name="toppassengers_airline")
    path('topmail_airline/',  
        TopMailByAirline.as_view(
            extra_context={'title': "Top Mail by Airline"}
        ), 
        name="topmail_airline"),
    path('topdistance_airline/',  
        TopDistanceByAirline.as_view(
            extra_context={'title': "Top Distance by Airline"}
        ), 
        name="topdistance_airline"),
]