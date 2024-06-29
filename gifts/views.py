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
            form.save()
            return redirect('birthday_list')
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
