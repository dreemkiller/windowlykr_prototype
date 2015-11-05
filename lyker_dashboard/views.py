from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from .models import User, Object, Customer, Video

def index(request):
    user_list = User.objects.order_by('user_id')
    template = loader.get_template('lyker_dashboard/index.html')
    context = RequestContext(request, {'user_list': user_list,})
    return HttpResponse(template.render(context))
def user(request, user_id):
    try:
        this_user = User.objects.get(user_id = user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return HttpResponse("User name:" + this_user.name)

def object(request, object_id):
    try:
        this_object = Object.objects.get(object_id = object_id)
    except Object.DoesNotExist:
        raise Http404("Object does not exist");
    return HttpResponse("Object name:" + this_object.object_name)

def customer(request, customer_id):
    try:
        this_customer = Customer.objects.get(customer_id = customer_id)
    except Customer.DoesNotExist:
        raise Http404("Customer does not exist")
    return HttpResponse("customer name:" + this_customer.name)

def video(request, video_id):
    try:
        this_video = Video.objects.get(video_id = video_id)
    except Video.DoesNotExist:
        raise Http404("Video does not exist")
    return HttpResponse("video name:" + this_video.name)

# Create your views here.
