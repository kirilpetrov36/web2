from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from .models import Note, User
from django.urls import reverse
from django.utils import timezone 

from django.urls import reverse

def login_page(request):
	return render(request, 'web2app/login_template.html')

def check_login(request):
	user = User.objects.filter(username = request.POST['username'], password = request.POST['password'])
	if(len(user) != 0):
		response = {'bool': True}
		return render(request, 'web2app/form.html', {'user': user[0]})		
	else:
		response = {'bool': False}
		return JsonResponse(response)

def login(request):
	user = User.objects.filter(username = request.POST['username'], password = request.POST['password'])
	if(len(user) != 0):
		user_temp = user[0]
		user_notes = user_temp.note_set.all()
		return render(request, 'web2app/main_page.html', {'user_notes': user_notes, 'user': user_temp})			
		

def registration_page(request):
	return render(request, 'web2app/registration_template.html', {'bool': -1})


def registration(request):
	username = request.POST['Username1']
	password = request.POST['Password1']
	confirm_password = request.POST['Confirm_password1']
	mod = request.POST['mod']
	if (mod == 'Admin'):
		admin = True
	else:
		admin = False

	if (password == confirm_password):
		user = User(username=username, password=password, admin = admin)
		user.save()
		user_notes = []
		return render(request, 'web2app/main_page.html', {'user_notes': user_notes, 'user': user})
	else:
		return render(request, 'web2app/registration_template.html', {'bool': 0})

def note_page(request, username):
	return render(request, 'web2app/note_template.html', {'username': username, 'bool_create': 1})

def save_note(request, username):
	theme = request.POST['theme']
	text = request.POST['text']
	date = timezone.now()
	last_edit = date
	last_user = User.objects.get(username=username)
	note = Note(theme=theme, text=text, date=date, last_edit=last_edit, last_user=last_user)
	note.save()
	user_notes=last_user.note_set.all()
	last_user.note_amount = len(user_notes)
	last_user.save()	
	return render(request, 'web2app/main_page.html', {'user_notes': user_notes, 'user': last_user})

def open_note(request, username, theme):
	user = User.objects.get(username = username)
	note = user.note_set.all().get(theme=theme)
	return render(request, 'web2app/note_template.html', {'note': note,'username': username, 'bool_create': 0})

def delete_note(request, username, theme):
	user = User.objects.get(username = username)
	note = user.note_set.all().get(theme=theme)
	user.save()
	note.delete()
	user_notes=user.note_set.all()
	user.note_amount = len(user_notes)
	user.save()
	return render(request, 'web2app/main_page.html', {'user_notes': user_notes, 'user': user})

def edit_note(request, username, theme):
	user = User.objects.get(username = username)
	note = user.note_set.all().get(theme=theme)
	note.theme = request.POST['theme']
	note.text = request.POST['text']
	note.save()
	user_notes=user.note_set.all()
	return render(request, 'web2app/main_page.html', {'user_notes': user_notes, 'user': user})

def get_users(request, username):
	users = User.objects.all()
	user = User.objects.get(username = username)
	return render(request, 'web2app/users_template.html', {'users': users, 'user_x': user} )

def make_admin(request, username):
	user = User.objects.get(username = username)
	user.admin = True;
	user.save()
	return HttpResponseRedirect( reverse('web2app:get_users', args = (username,)))

def delete_user(request, username):
	user = User.objects.get(username = username)
	user.delete()
	return HttpResponseRedirect( reverse('web2app:get_users', args = (username,)))

def main_menu(request, username):
	user = User.objects.get(username = username)
	user_notes=user.note_set.all()
	return render(request, 'web2app/main_page.html', {'user_notes': user_notes, 'user': user})