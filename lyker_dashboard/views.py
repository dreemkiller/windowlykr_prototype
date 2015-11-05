from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
#from django.template import RequestContext, loader

from .models import User, Object, Customer, Video

def index(request):
    user_list = User.objects.order_by('user_id')
    #template = loader.get_template('lyker_dashboard/index.html')
    context = {'user_list': user_list,}
    return render(request, 'lyker_dashboard/index.html', context)
def user(request, user_id):
    this_user = get_object_or_404(User, pk=user_id)
    return render(request, 'lyker_dashboard/user.html', {'this_user':this_user})

def object(request, object_id):
    this_object = get_object_or_404(Object, pk=object_id)
    return render(request, 'lyker_dashboard/object.html', {'this_object': this_object})

def customer(request, customer_id):
    this_customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'lyker_dashboard/customer.html', {'this_customer':this_customer})

def video(request, video_id):
    this_video = get_object_or_404(Video, pk=video_id)
    return render(request, 'lyker_dashboard/video.html', {'this_video':this_video})

# Create your views here.
