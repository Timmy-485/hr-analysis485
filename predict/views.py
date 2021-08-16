from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from .forms import PredictCreateForm
from .models import PredictionResults
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
import pickle


# Create your views here.
#login view
def login_view(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      # Add your code below:
      login(request, user)
      return redirect("dashboard")
    else:
      return HttpResponse("invalid credentials")
  return render(request, "registration/login.html", context)

# signup view
class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

#logout view
def logout_view(request):
  logout(request)
  return redirect("home")

#Homepage view (prediction page)
def homepage(request):
  form = PredictCreateForm()

  context = {'result': ""}
  # grab inputs from form
  if request.method =='POST':
    training_hours = int(request.POST.get('training_hours'))
    city_dev_index = float(request.POST.get('city_dev_index'))
    experience = int(request.POST.get('experience'))
    last_new_job = int(request.POST.get('last_new_job'))
    company_size = request.POST.get('company_size')
    edu_level = request.POST.get('edu_level')
    major = request.POST.get('major')
    company_type = request.POST.get('company_type')
    relevant_experience = request.POST.get('relevant_experience')

    # encode categorical input
    # load saved encoders
    rel_exp = pickle.load(open("predict/relevent_experience_le.pkl", "rb"))
    edu_lvl = pickle.load(open("predict/education_level_le.pkl", "rb"))
    major_disc = pickle.load(open("predict/major_discipline_le.pkl", "rb"))
    comp_size = pickle.load(open("predict/company_size_le.pkl", "rb"))
    comp_type = pickle.load(open("predict/company_type_le.pkl", "rb"))

    # encode values
    rel_exp_val = rel_exp.transform([relevant_experience])
    edu_lvl_val = edu_lvl.transform([edu_level])
    major_disc_val = major_disc.transform([major])
    comp_size_val = comp_size.transform([company_size])
    comp_type_val = comp_type.transform([company_type])


    # load machine learning module
    model_var = pickle.load(open("predict/model.sav", "rb"))
    prediction_result = model_var.predict([[
      city_dev_index, 
      rel_exp_val, 
      edu_lvl_val, 
      major_disc_val, 
      experience, 
      comp_size_val, 
      comp_type_val, 
      last_new_job, 
      training_hours
      ]])
    

    p = PredictionResults(
      training_hours=training_hours, 
      city_dev_index=city_dev_index,
      experience=experience,
      last_new_job=last_new_job,
      company_size=company_size,
      edu_level=edu_level,
      major=major,
      company_type=company_type,
      relevant_experience=relevant_experience,
      prediction_result=prediction_result 
      )
    p.save()

    if prediction_result == 0:
      context = 'Employee likely to leave'
    elif prediction_result == 1:
      context = 'Employee likely to stay'
    return render(request, 'predict/predict.html', {'form': form, 'result': context})


  return render(request, 'predict/predict.html', {'form': form})


#database display view
class dashboard(LoginRequiredMixin, ListView):
  model = PredictionResults
  template_name = 'predict/dashboard.html'
  
