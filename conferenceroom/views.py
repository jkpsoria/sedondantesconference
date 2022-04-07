from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Count
from django.db.models import Max
# Create your views here.
class IndexView(View):
	def get(self, request):
		return render(request,'index.html',{})
class AccomodationView(View): 
	def get(self, request):
		room = Room.objects.values('roomtype').annotate(count=Count('roomtype')).latest('count')
		count_date = Room.objects.values('dateofuse').annotate(count=Count('dateofuse'))
		context = {
			'room':room,
			'count_date':count_date
			}
		return render(request,'accomodation.html',{})
class SignInView(View): 
	def get(self, request):
		return render(request, 'signin.html',{})
	def post(self, request):
		if request.method == 'POST':
			username= request.POST.get("username")
			password = request.POST.get("password")
			check_user = User.objects.filter(username=username,password=password)
			check_admin = Admin.objects.filter(username='admin',password='admin')
			if check_user:
				request.session['usern'] = username
				if User.objects.filter(username=username).count()>0:
					return redirect('/conferenceroom/indexwuser')
				else:
					return redirect('/conferenceroom/signin.html')
			if check_admin:
				request.session['admin'] = username
				if Admin.objects.filter(username=username).count()>0:
					return redirect('/conferenceroom/admin')
		else:	
			return render(request,"signup.html", context)
class RegistrationView(View): 
	def get(self, request):
		user = User.objects.all()
		context = {
			'user':user,
		}
		return render(request,'registration.html',context)
	def post(self, request):		
		form = UserForm(request.POST)		
		if form.is_valid():
			username = request.POST.get("username")
			password = request.POST.get("password")
			emailadd = request.POST.get("emailadd")
			fname = request.POST.get("fname")
			lname = request.POST.get("lname")
			address = request.POST.get("address")
			contactNum = request.POST.get("contactNum")

			form = User(username=username,password=password,emailadd=emailadd,fname=fname,lname=lname,address=address,contactNum=contactNum)
			form.save()	
			return redirect('/conferenceroom/signin')
		else:
			print(form.errors)
			return HttpResponse('not valid')
class AboutUsView(View):
	def get(self, request):
		return render(request, 'about.html',{})
		
class ContactView(View):
	def get(self, request):
		return render(request, 'contact.html',{})
class RoomView(View):
	def get(self, request):
		if 'usern' in request.session:
			current_user = request.session['usern']
			addroom = AddRoom.objects.all()
			userdetails = User.objects.filter(username=current_user)
			context = {
				'userdetails':userdetails,
				'addroom':addroom,
		}
		return render(request,'room.html',context)
	def post(self, request):		
		form = RoomForm(request.POST)		
		if form.is_valid():
			slot = request.POST.get("slot")
			roomtype = request.POST.get("roomtype")
			dateofuse = request.POST.get("dateofuse")
			username = request.POST.get("username")
			form = Room(slot=slot,roomtype = roomtype, dateofuse = dateofuse, username_id=username)
			form.save()	
			return redirect('/conferenceroom/roomdashboard')
		else:
			print(form.errors)
			return HttpResponse('not valid')
class RoomDashboardView(View):
	def get(self, request):
		if 'usern' in request.session:
			current_user = request.session['usern']
			room = Room.objects.filter(username=current_user)
			#count_date = Room.objects.values('dateofuse').order_by('dateofuse').annotate(count=Count('dateofuse'))
			userdetails = User.objects.filter(username=current_user)
			context = {
				'userdetails':userdetails,
				'room':room,
			#	'count_date':count_date,
		}
		return render(request,'roomdashboard.html',context)
	def post(self, request):
			if 'BtnUpdate_user'in request.POST:
				username = request.POST.get("username") 
				password = request.POST.get("password")
				emailadd = request.POST.get("emailadd")
				fname = request.POST.get("fname")
				lname = request.POST.get("lname")
				address = request.POST.get("address")
				contactNum = request.POST.get("contactNum")
				print(username)		
				update_user = User.objects.filter(username = username).update(password=password,emailadd=emailadd,fname=fname,lname=lname,address=address,contactNum=contactNum)
				print(update_user)
				print('User Updated')
				return redirect('/conferenceroom/roomdashboard')
			elif 'BtnDelete_user' in request.POST:
				iddn = request.POST.get("id") 
				iddn= User.objects.filter(id = iddn).delete()
				print('deleted')
				return redirect('/conferenceroom/roomdashboard')
			elif 'BtnUpdate_room'in request.POST:
				username = request.POST.get("username") 
				slot = request.POST.get("slot") 
				dateofuse = request.POST.get("dateofuse")
				roomtype = request.POST.get("roomtype")	
				update_room = Room.objects.filter(username = username).update(slot=slot,dateofuse=dateofuse,roomtype=roomtype)
				print('Room Updated')
				return redirect('/conferenceroom/roomdashboard')
			elif 'BtnDelete_room' in request.POST:
				iddn = request.POST.get("id") 
				iddn= Room.objects.filter(id = iddn).delete()
				print('deleted')
				return redirect('/conferenceroom/roomdashboard')
			
class AddRoomView(View):
	def get(self, request):
		return render(request, 'addroom.html',{})
	def post(self, request):
		form = AddRoomForm(request.POST)
		if form.is_valid():
			roomnumber = request.POST.get("roomnumber")
			roomtype = request.POST.get("roomtype")
			form = AddRoom(roomnumber=roomnumber,roomtype = roomtype)
			form.save()	
			return redirect('/conferenceroom/roomdashboard')
		else:
			print(form.errors)
			return HttpResponse('not valid')


######################views with user######################################################################################
class AboutUsViewWUser(View):
	def get(self, request):
		if 'usern' in request.session:
			current_user = request.session['usern']
			userdetails = User.objects.filter(username=current_user)
			context = {
			'userdetails':userdetails,
			}
		return render(request,'aboutwuser.html', context)
class AccomodationViewWUser(View):
	def get(self, request):
		if 'usern' in request.session:
			current_user = request.session['admin']
			userdetails = Admin.objects.filter(username=current_user)
			room = Room.objects.values('roomtype').annotate(count=Count('roomtype')).latest('count')
			#order_by().annotate(count=Count('roomtype'))
			#room = Room.objects.aggregate(max=Max('roomtype'))
			count_date = Room.objects.values('dateofuse').annotate(count=Count('dateofuse'))
			
			context = {
			'userdetails':userdetails,
			'room':room,
			'count_date':count_date
			}
		return render(request,'accomodationwuser.html', context)
class IndexViewWUser(View):
	def get(self, request):
		if 'usern' in request.session:
			current_user = request.session['usern']
			userdetails = User.objects.filter(username=current_user)
			context = {
			'userdetails':userdetails,
			}
		return render(request,'indexwuser.html', context)
class ContactViewWUser(View):
	def get(self, request):
		if 'usern' in request.session:
			current_user = request.session['usern']
			userdetails = User.objects.filter(username=current_user)
			context = {
			'userdetails':userdetails,
			}
		return render(request,'contactwuser.html', context)
	
####################################admin views ####################
class AdminView(View):
	def get(self, request):
		if 'admin' in request.session:
			current_user = request.session['admin']
			userdetails = Admin.objects.filter(username=current_user)
			room = Room.objects.values('roomtype').annotate(count=Count('roomtype')).latest('count')
			#order_by().annotate(count=Count('roomtype'))
			#room = Room.objects.aggregate(max=Max('roomtype'))
			count_date = Room.objects.values('dateofuse').annotate(count=Count('dateofuse'))
			context = {
			'userdetails':userdetails,
			'room':room,
			'count_date':count_date
			}
		return render(request,'admin.html', context)
class AdminAboutView(View):
	def get(self, request):
		if 'admin' in request.session:
			current_user = request.session['admin']
			userdetails = Admin.objects.filter(username=current_user)
			#room = Room.objects.values('roomtype').order_by().annotate(count=Count('roomtype'))
			#room = Room.objects.aggregate(max=Max('roomtype'))
			room = Room.objects.values('roomtype').annotate(count=Count('roomtype'))
			count_date = Room.objects.values('dateofuse').annotate(count=Count('dateofuse'))
			context = {
			'userdetails':userdetails,
			'room':room,
			'count_date':count_date,
			}
		return render(request,'adminabout.html', context)
class AdminContactView(View):
	def get(self, request):
		if 'admin' in request.session:
			current_user = request.session['admin']
			userdetails = Admin.objects.filter(username=current_user)
			room = Room.objects.values('roomtype').order_by().annotate(count=Count('roomtype'))
			#room = Room.objects.aggregate(max=Max('roomtype'))
			count_date = Room.objects.values('dateofuse').annotate(count=Count('dateofuse'))
			context = {
			'userdetails':userdetails,
			'room':room,
			'count_date':count_date
			}
		return render(request,'admincontact.html', context)
class AdminIndexView(View):
	def get(self, request):
		if 'admin' in request.session:
			current_user = request.session['admin']
			userdetails = Admin.objects.filter(username=current_user)
			room = Room.objects.values('roomtype').order_by().annotate(count=Count('roomtype'))
			#room = Room.objects.aggregate(max=Max('roomtype'))
			count_date = Room.objects.values('dateofuse').annotate(count=Count('dateofuse'))
			context = {
			'userdetails':userdetails,
			'room':room,
			'count_date':count_date
			}
		return render(request,'adminindex.html', context)
class AdminRegistrationView(View): 
	def get(self, request):
		user = Admin.objects.all()
		context = {
			'user':user,
		}
		return render(request,'adminregistration.html',context)
	def post(self, request):		
		form = UserForm(request.POST)		
		if form.is_valid():
			username = request.POST.get("username")
			password = request.POST.get("password")
			emailadd = request.POST.get("emailadd")
			fname = request.POST.get("fname")
			lname = request.POST.get("lname")
			address = request.POST.get("address")
			contactNum = request.POST.get("contactNum")

			form = Admin(username=username,password=password,emailadd=emailadd,fname=fname,lname=lname,address=address,contactNum=contactNum)
			form.save()	
			return redirect('/conferenceroom/signin')
		else:
			print(form.errors)
			return HttpResponse('not valid')
class AdminDashboardView(View):
	def get(self, request):
		if 'admin' in request.session:
			current_user = request.session['admin']
			userdetails = Admin.objects.filter(username=current_user)
			count_date = Room.objects.values('dateofuse').order_by('dateofuse').annotate(count=Count('dateofuse'))
			#room = Room.objects.values('roomtype').annotate(count=Count('roomtype'))
			#room_max = room.aggregate(Max('roomtype')
			context = {
			'userdetails':userdetails,
			'count_date':count_date
			}
		return render(request,'admindashboard.html', context)