from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import MyModel

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# myapp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import MyModelForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def my_form_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with your success URL
    else:
        form = MyModelForm()

    return render(request, 'myapp/my_form.html', {'form': form})

def success_view(request):
    return render(request, 'myapp/success.html')

# def show_records(request):
#     records = MyModel.objects.all()
#     return render(request, 'myapp/show_records.html', {'records': records})

def show_records(request):
    role = request.GET.get('role', 'user')  # Default role is 'user' if not provided
    records = MyModel.objects.filter(role=role)
    return render(request, 'myapp/show_records.html', {'records': records, 'selected_role': role})

@require_POST
def delete_record(request, record_id):
    record = get_object_or_404(MyModel, pk=record_id)
    record.delete()
    return JsonResponse({'message': 'Record deleted successfully'})