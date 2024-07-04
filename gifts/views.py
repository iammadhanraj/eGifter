from django.shortcuts import render, redirect,get_object_or_404
from .models import Birthday
from .forms import BirthdayForm

def birthday_list(request):
    birthdays = Birthday.objects.all()
    return render(request, 'birthday/birthday_list.html', {'birthdays': birthdays})

def birthday_detail(request, pk):
    birthday = Birthday.objects.get(pk=pk)
    return render(request, 'birthday/birthday_detail.html', {'birthday': birthday})

def birthday_create(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST, request.FILES)
        if form.is_valid():
            birthday_instance = form.save()  # Save the form data to create a new instance
            birthday_id = birthday_instance.id  # Access the ID of the newly created instance
            birthday=Birthday.objects.get(pk=birthday_id)
            data={
                'bdgifts':birthday,
            }
            return redirect("thanks", str(birthday.id))
            
        
    else:
        form = BirthdayForm()
    return render(request, 'birthday/birthday_form.html', {'form': form})

def birthday_delete(request, pk):
    birthday = get_object_or_404(Birthday, pk=pk)
    if request.method == 'POST':
        birthday.delete()
        return redirect('birthday_list')
    return render(request, 'birthday/birthday_confirm_delete.html', {'birthday': birthday})


def normalview(request,pk):
    birthday=Birthday.objects.get(pk=pk)
    data={
        'bdgifts':birthday,
    }
    return render(request,'designs/ButtterflyCatcher.html',data)

def thanks(request,data):
    gifts=Birthday.objects.get(id=data)
    datas = {'bdgifts': gifts}
    return render(request,'birthday/thanks.html',datas)
