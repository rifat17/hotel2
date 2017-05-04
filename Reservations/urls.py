from django.conf.urls import url
from Reservations import views
app_name = 'Reservations'
urlpatterns = [

    url(r'^book/(?P<hotelid>[0-9]+)/(?P<roomid>[0-9]+)$', views.bookRoom, name='bookroom'),
    url(r"^book/new/(?P<roomid>[0-9]+)/(?P<hotelid>[0-9]+)/(?P<checkin>(\d{4}-\d{2}-\d{2}))/(?P<checkout>(\d{4}-\d{2}-\d{2}))/(?P<totalcost>[0-9]+)$"
    , views.storeBooking, name='newbooking'),

]