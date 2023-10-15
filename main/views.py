from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, serializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth import authenticate
from .serializers import UserSerializer, UserInfoSerializer, UserMoodSerializer, MemoriesSerializer, MedicationsSerializer, MedicationsRecordSerializer, AppointmentSerializer, LocationSerializer
from django.contrib.auth.hashers import make_password
from . import models
from django.utils import timezone
import json

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response({"message": "Hello, world!"})

@api_view(['POST'])
def singup(request):
    postdata = json.loads(request.body)
    email = postdata.get('email')
    password = postdata.get('password')
    first_name = postdata.get('name')
    try:
        user = User.objects.filter(Q(username=email) | Q(email=email)).count()
    except:
        user = None
    if not user:
        user = User.objects.create(username=email,password=make_password(password),email=postdata['email'],first_name=first_name)
        return Response({"user": UserSerializer(user).data}	)
    else:
        return Response({"message": "Email already Exists."}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login(request):
    print(request.body)
    postdata = json.loads(request.body)
    email = postdata.get('email')
    password = postdata.get('password')
    try:
        user = User.objects.get(username=postdata['email'])
    except:
        user = None
    if user and email and password:
        user = authenticate(username=email, password=password)
        if user:
            return Response({"user": UserSerializer(user).data})
        else:
            return Response({"message": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "user not found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_info(request):
    postdata = json.loads(request.body)
    weight = postdata.get('weight')
    height = postdata.get('height')
    user = postdata.get('user_id')
    if weight and height and user:
        models.UserInfo.objects.create(user_id=user,weight=weight,height=height)
        return Response({"message": "User Info Added"})
    else:
        return Response({"message": "User Info Not Added"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST','GET'])
def user_mood(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            user_mood = models.UserMood.objects.filter(user_id=user_id).order_by('-date')
            serializer = UserMoodSerializer(user_mood, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        postdata = json.loads(request.body)
        mood = postdata.get('mood')
        user = postdata.get('user_id')
        if mood and user:
            models.UserMood.objects.create(user_id=user,mood=mood,date=timezone.now().date())
            return Response({"message": "User Mood Added"})
        else:
            return Response({"message": "User Mood Not Added"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def user_data(request):
    user_id = request.GET.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        user_info = models.UserInfo.objects.get(user_id=user_id)
        user_mood = models.UserMood.objects.filter(user_id=user_id).order_by('-date')
        return Response({
                "user": UserSerializer(user).data,
                "user_info":UserInfoSerializer(user_info).data,
                "user_mood":UserMoodSerializer(user_mood, many=True).data
            })
    else:
        return Response({"message": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def meds_data(request):
    json_file_path = 'output.json'

    # Read the JSON data from the file
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
        
    serialized_data = json_data[0::1000]

    # Return the JSON data as a response
    return JsonResponse(serialized_data, safe=False)

@api_view(['POST','GET'])
def memories(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            memories = models.Memories.objects.filter(author_id=user_id).order_by('-date_posted')
            serializer = MemoriesSerializer(memories, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        postdata = request.POST
        user = postdata.get('user_id')
        content = postdata.get('content')
        image = request.FILES.get('image')
        alt_text = postdata.get('alt_text')
        if user and content:
            # url: str = "https://qwrranvmkfmxcmjilkam.supabase.co"
            # key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF3cnJhbnZta2ZteGNtamlsa2FtIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NzI2NDI3MywiZXhwIjoyMDEyODQwMjczfQ.O2suIZCGyNwbPV7PC8EyK8jrvyrF3iTv31cdKwsVD4M"
            # supabase: Client = create_client(url, key)
            # print(image.name,image.content_type)
            # try:
            #     name = image.name.split('.')[0]
            #     file_type = image.content_type
            #     image_content = image.read()
            #     supabase.storage.from_("images").upload(file=image_content,path=name, file_options={"content-type": file_type})
            #     url = supabase.storage.from_('images').get_public_url(name)
            #     print(url)
            #     print(type(url))
            # except Exception as e:
            #     return Response({"message": "Memory Not Added"}, status=status.HTTP_400_BAD_REQUEST)
            models.Memories.objects.create(author_id=user,content=content,image=image,alt_text=alt_text)
            return Response({"message": "Memory Added"})
        else:
            return Response({"message": "Memory Not Added"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','GET'])   
def medications(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            meds = models.Medications.objects.filter(user_id=user_id)
            serializer = MedicationsSerializer(meds, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        postdata = json.loads(request.body)
        user = postdata.get('user_id')
        name = postdata.get('name')
        time_of_day = postdata.get('time_of_day')
        if user and name and time_of_day:
            models.Medications.objects.create(user_id=user,name=name,time_of_day=time_of_day)
            return Response({"message": "Medication Added"})
        else:
            return Response({"message": "Medication Not Added"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','POST'])
def medications_record(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            meds = models.Medications.objects.filter(user_id=user_id)
            for m in meds:
                try:
                    obj = models.MedicationsRecord.objects.get(user_id=user_id, medicine_id=m.id, date=timezone.now().date())
                except:
                    obj = None
                if not obj:
                    obj = models.MedicationsRecord.objects.create(user_id=user_id, medicine_id=m.id, date=timezone.now().date())
                
            meds_record = models.MedicationsRecord.objects.filter(user_id=user_id, date=timezone.now().date())
            serializer = MedicationsRecordSerializer(meds_record, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        postdata = json.loads(request.body)
        user = postdata.get('user_id')
        medicine = postdata.get('medicine')
        taken = postdata.get('taken')
        if user and medicine and taken:
            try:
                obj = models.MedicationsRecord.objects.get(user_id=user, medicine_id=medicine, date=timezone.now().date(), taken=False)
            except:
                obj = models.MedicationsRecord.objects.create(user_id=user, medicine_id=medicine, date=timezone.now().date())
            if obj:
                obj.taken = True
                obj.save()
                return Response({"message": "Medication Record Added"})
        else:
            return Response({"message": "Medication Record Not Added"}, status=status.HTTP_400_BAD_REQUEST)\
                    
# @api_view(['POST'])     
# def get_appointments(request):
#     user_id = request.GET.get('user_id')
#     if user_id:
#         appointments = models.Appointment.objects.filter(user_id=user_id)
#         serializer = AppointmentSerializer(appointments, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({"message": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)                         
                         
     
@api_view(['POST'])
def appointment(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            appointments = models.Appointment.objects.filter(user_id=user_id)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        postdata = json.loads(request.body)
        user = postdata.get('user_id')
        doctor = postdata.get('doctor')
        date = postdata.get('date')
        time = postdata.get('time')
        location = postdata.get('location')
        reason = postdata.get('reason')
        notes = postdata.get('notes')
        if user and doctor and date and time and location and reason and notes:
            models.Appointment.objects.create(user_id=user,doctor=doctor,date=date,time=time,location=location,reason=reason,notes=notes)
            return Response({"message": "Appointment Added"})
        else:
            return Response({"message": "Appointment Not Added"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST','GET'])
def location(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            locations = models.Location.objects.filter(user_id=user_id)[0]
            serializer = LocationSerializer(locations)
            return Response(serializer.data)
        else:
            return Response({"message": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        postdata = json.loads(request.body)
        print(postdata)
        user = postdata.get('user_id')
        lat = postdata.get('lat')
        lon = postdata.get('lon')
        if user and lat and lon:
            models.Location.objects.create(user_id=user,lat=lat,lon=lon,date_time=timezone.now())
            return Response({"message": "Location Added"})
        else:
            return Response({"message": "Location Not Added"}, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET'])
def nearby_doctors(request):
    with open('docs.json', 'r') as file:
            data = json.load(file)
    return JsonResponse({'data': data}, status=200)


# views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
