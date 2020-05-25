from django.urls import path

from . import views

app_name = 'web2app'

urlpatterns = [
	path('', views.login_page, name = 'login_page'),
	path('login', views.login, name = 'login'),
	path('check_login', views.check_login, name = 'check_login'),

	path('note_page/<str:username>', views.note_page, name = 'note_page'),
	path('open_note/<str:username>/<str:theme>', views.open_note, name = 'open_note'),
	path('save_note/<str:username>', views.save_note, name = 'save_note'),
	path('delete_note/<str:username>/<str:theme>', views.delete_note, name = 'delete_note'),
	path('edit_note/<str:username>/<str:theme>', views.edit_note, name = 'edit_note'),

	path('get_users/<str:username>', views.get_users, name = 'get_users'),		
	path('registration_page', views.registration_page, name = 'registration_page'),
	path('registration', views.registration, name = 'registration'),
	path('make_admin/<str:username>', views.make_admin, name = 'make_admin'),
	path('delete_user/<str:username>', views.delete_user, name = 'delete_user'),
	path('main_menu/<str:username>', views.main_menu, name = 'main_menu'),

]