# dogapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import requests
from django.contrib.auth.decorators import login_required

# View for handling user signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'dogapp/signup.html', {'form': form})

# View for showing a random dog image
@login_required  # Ensure only logged-in users can access this view
def random_dog(request):
    # Fetch a random dog image from the Dog API
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    image_url = data['message']  # Extract image URL from API response
    
    # Render the template and pass the image URL to it
    return render(request, 'dogapp/random_dog.html', {'image_url': image_url})
