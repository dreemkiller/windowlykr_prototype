from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
#from django.template import RequestContext, loader

from .models import User, Object, Customer, Video, UserAction

def index(request):
    user_list = User.objects.order_by('user_id')
    customer_list = Customer.objects.order_by('customer_id')
    video_list = Video.objects.order_by('video_id')
    object_list = Object.objects.order_by('object_id')
    context = {'user_list': user_list,
               'customer_list':customer_list,
               'video_list':video_list,
               'object_list':object_list}
    return render(request, 'lyker_dashboard/index.html', context)
def user(request, user_id):
    this_user = get_object_or_404(User, pk=user_id)
    useraction_list = UserAction.objects.filter(user=this_user)
    object_list = Object.objects.order_by('object_id')
    print("useraction_list:" + str(useraction_list))
    return render(request, 'lyker_dashboard/user.html',
                  {'this_user':this_user,
                   'useraction_list':useraction_list,
                   'object_list':object_list,
                  })

def object(request, object_id):
    this_object = get_object_or_404(Object, pk=object_id)
    return render(request, 'lyker_dashboard/object.html', {'this_object': this_object})

def customer(request, customer_id):
    this_customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'lyker_dashboard/customer.html', {'this_customer':this_customer})

def video(request, video_id):
    this_video = get_object_or_404(Video, pk=video_id)
    return render(request, 'lyker_dashboard/video.html', {'this_video':this_video})

def useraction(request):
    object_id = request.POST['object']
    action_type = request.POST['type']
    image_path = request.POST['image_path']
    #user_id = request.POST['user_id']
    return render(request, 'lyker_dashboard/useraction.html',
                           {'object_id':object_id,
                            'action_type':action_type,
                            'image_path':image_path})

# Create your views here.
