from django.shortcuts import render, redirect,get_object_or_404
from .models import Birthday
from .forms import BirthdayForm
from django.urls import reverse
# from django.contrib.sites.models import Site



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
            # current_site = Site.objects.get_current()
            # domainurl=current_site.domain
            data={
                'bdgifts':birthday,
                # 'domainurl':domainurl,
            }
            # data=data['giftid']
            # return redirect('thanks')
            # print(data['giftid'])
            # return redirect(reverse('thanks', args=[birthday_id]))
    
            # form.save()
            return render(request,'birthday/thanks.html',data)
            
        
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

# def thanks(request,data):
#     print(data)
#     gifts=Birthday.objects.get(data)
#     print(gifts)
#     datas = {'bdgifts': gifts}
#     return render(request,'birthday/thanks.html',datas)
