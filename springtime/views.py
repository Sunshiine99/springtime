from django.shortcuts import render
from springtime.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    #This should change to return the index page
    return render(request, 'springtime/main.html')

def register(request):
	# Boolean value tells template whether registration was successful. 
	# Set to false initially.
	registered = False

	# If HTTP POST, process form data.
	if request.method == 'POST':
		# Grab information from raw form information. 
		user_form = UserForm(data=request.POST)

		#If form is valid...
		if user_form.is_valid():
			#Saves user's form data to database.
			user = user_form.save()

			# Hash password with set_password method.
			user.set_password(user.password)
			user.save()

			# Update variable to indicate that template registration was success.
			registered = True

		else:
			# Invalid form, print problems to terminal.
			print(user_form.errors)
	else:
		# Not a HTTP POST, so render form using ModelForm instance.
		user_form = UserForm()

	# Render the template depending on the context.
	return render(request, 'springtime/register.html', 
		{'user_form': user_form,
		 'registered': registered})

def user_login(request):
	# If request is HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather usernamd and password provided by user in login form.
		username = request.POST.get('username')
		password = request.POST.get('password')

		# See if username/password combination is valid.
		user = authenticate(username=username, password=password)

		# If we have User object, the details are correct.
		# If None, no user with matching credentials.
		if user:
			if user.is_active():
				# If account is valid and active, log the user in.
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				# An inactive account was used - no logging in.
				return HttpResponse("Your Springtime account is disabled.")

		else:
			# Bad login details provided, can't log user in.
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

		# The request is not a HTTP POST, so display the login form.
	else:
		return render(request, 'springtime/login.html', {})


