from django.shortcuts import render, redirect
from .forms import PortfolioForm
from .models import Portfolio

def get_user_data(request):
    form = PortfolioForm()
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    content = {'form':form}
    return render(request, 'the_app/get_user_data.html', content)

def index(request):
    user = Portfolio.objects.all()
    p_user = user[len(user)-1]
    content = {'user': p_user}
    return render(request, 'the_app/index.html', content)