from django.shortcuts import render ,redirect
from .models import Employee , User 
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home_page(request):
    user = request.user
    full_name = get_user_full_name(user)  # Replace with your logic to get the full name

    context = {
        'full_name': full_name,
        # Add other context variables as needed
    }

    return render(request, 'home.html', context)

def get_user_full_name(user):
    # Replace this with your logic to get the full name
    # For example, if you have a UserProfile model with a full_name field:
    # return user.profile.full_name
    return f"{user.first_name} {user.last_name}"




def about_page(request):
  return render(request , 'about.html')

def services_page(request):
  
  return render(request , 'services.html')


def register_page(request):
   if request.method == "POST":
      full_name = request.POST.get('full_name')
      email_id = request.POST.get('email_id')
      office_id = request.POST.get('office_id')
   

      user = User.objects.filter(office_id = office_id)

      if user.exists():
         messages.info(request, 'Username already exists')
         return redirect('/register/')


      user = User.objects.create(
         full_name = full_name,
         email_id = email_id,
         office_id = office_id,
           )

      
      user.save()

      messages.info(request, 'Account created successfully!')

      return redirect('home')


   return render(request, 'register.html')





   return render(request , 'register.html')

def login_page(request):
   if request.method == "POST":
    email_id = request.POST.get('email_id')
    office_id = request.POST.get('office_id')
   

    user = User.objects.filter(office_id = office_id)

    if user.exists():
         messages.info(request, 'Username already exists')
         return redirect('/register/')


    user = User.objects.create(
        
         email_id = email_id,
         office_id = office_id,
           )

      
    user.save()

    messages.info(request, 'Logged in successfully!')

    return redirect('home')








   return render(request , "login.html")


