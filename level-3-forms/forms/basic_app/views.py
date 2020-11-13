from django.shortcuts import render
from basic_app import forms
# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('VALIDATION SUCCESS!')
            print('Name: ', form.cleaned_data['name'])
            print('Email: ', form.cleaned_data['email'])
            print('Text: ', form.cleaned_data['text'])

    return render(request, 'basic_app/form_page.html', {'form': form})

def preorder_view(request):
    form = forms.PreorderForm()

    if request.method == 'POST':
        form = forms.PreorderForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'basic_app/index.html')


    return render(request, 'basic_app/preorder.html', {'form': form})
