from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
import stripe

# Create your views here.

#make it secret later 
stripe.api_key = 'test_key_sanitized'
endpoint_secret = 'test_key_sanitized'
def home(request):
    return render(request,'home.html')

def logout(request):
    logout(request)
    return redirect("/user/me")

def event_checkout(request,slug):
    if request.user.is_authenticated==False:
        return render(request,'home.html')
    else:
        get_user = request.user
        try:
            get_event= Event.objects.get(id=slug)
            return render(request,'eventcheckout.html',{'event':get_event,'user':get_user})
        except ObjectDoesNotExist:
            return HttpResponse("404: No event found !")
def payment_gateway(request,slug):
    YOUR_DOMAIN = 'http://localhost:8000'
    get_user = request.user
    try:
        get_event= Event.objects.get(id=slug)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': get_event.stripe_prize_id,
                    'quantity': 1,
                },
            ],
            metadata={
                "event_id":get_event.id,
                "name":get_user.first_name,
                "email":get_user.email,
                "referral_code":''
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
    except Exception as e:
        return str(e)
    print(checkout_session)
    return redirect(checkout_session.url)
def success(request):
    return render(request,'success.html')
def cancel(request):
    return render(request,'cancel.html')

@csrf_exempt
def webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
        )
    except ValueError as e:

        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = stripe.checkout.Session.retrieve(
        event['data']['object']['id'],
        expand=['line_items'],
        )
        line_items = session.line_items
        event_id = session["metadata"]["event_id"]
        firstname = session["metadata"]["name"]
        email = session["metadata"]["email"]
        referral_code = session["metadata"]["referral_code"]
        get_event_details= Event.objects.get(id=event_id)
        print(line_items)
        if referral_code!='':
            print("activate campus ambassador")
        
        send_mail(
            subject='Your Advent ticket ',
            message=f'Your ticket is confirmed for the event : {get_event_details.event_name} ',
            recipient_list=email,
            from_email='mail'
        )
    return HttpResponse(status=200)

@api_view(['GET'])
def event_api(request,slug):
    get_events = Event.objects.filter(event_type=slug)
    response_bucket =[]
    for i in get_events:
        serializer  = EventSerializer(i)
        response_bucket.append(serializer.data)
    return Response({'data':response_bucket})