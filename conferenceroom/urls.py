from django.urls import path
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'conferenceroom'
urlpatterns= [
#URLS for myapp1 app
     #dashboard
     path('index',views.IndexView.as_view(), name="my_index_view"),
     path('accomodation',views.AccomodationView.as_view(), name="my_accomodation_view"),     
     path('registration',views.RegistrationView.as_view(), name="my_registration_view"),
     path('signin',views.SignInView.as_view(), name="my_signin_view"),          
     path('about',views.AboutUsView.as_view(), name="my_aboutus_view"),
     path('contact',views.ContactView.as_view(), name="my_contact_view"),
     path('room',views.RoomView.as_view(), name="my_room_view"),
     path('addroom',views.AddRoomView.as_view(), name="my_addroom_view"),
     #urls after signing in
     path('roomdashboard',views.RoomDashboardView.as_view(), name="my_roomdashboard_view"),
     path('aboutwuser',views.AboutUsViewWUser.as_view(), name="my_aboutuswuser_view"),
     path('accomodationwuser',views.AccomodationViewWUser.as_view(), name="my_accomodationwuser_view"),
     path('indexwuser',views.IndexViewWUser.as_view(), name="my_indexwuser_view"),
     path('contactwuser',views.ContactViewWUser.as_view(), name="my_contactwuser_view"),
     #######admin#######
     path('admin',views.AdminView.as_view(), name="my_admin_view"),
     path('adminabout',views.AdminAboutView.as_view(), name="my_admin_about_view"),
     path('admincontact',views.AdminContactView.as_view(), name="my_admin_contact_view"),
     path('adminindex',views.AdminIndexView.as_view(), name="my_admin_index_view"),
     path('admindashboard',views.AdminDashboardView.as_view(), name="my_admin_dashboard_view"),
     path('adminregistration',views.AdminRegistrationView.as_view(), name="my_admin_registration_view"),
     ]