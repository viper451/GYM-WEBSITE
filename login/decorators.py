from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

def auth_or_not(flag):
	def auth_or_not_d(view_func):
		def wrapper_func(request, *args, **kwargs):
			if ((request.user.is_authenticated and flag == 1) or (request.user.is_authenticated == False and flag == 0)):
				return view_func(request, *args, **kwargs)
			elif flag == 1:
				return redirect('register')
			else:
				return redirect('login')
		return wrapper_func
	return auth_or_not_d