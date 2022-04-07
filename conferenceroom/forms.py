from django import forms
from .models import *

class RoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields= '__all__'
class RoomReservationForm(forms.ModelForm):
	class Meta:
		model = RoomReservation
		fields= '__all__'
class AddRoomForm(forms.ModelForm):
	class Meta:
		model = AddRoom
		fields= '__all__'
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields= '__all__'
class AdminForm(forms.ModelForm):
	class Meta:
		model = Admin
		fields= '__all__'