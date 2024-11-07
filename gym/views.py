from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index1.html')

def user(request):
    


    return render(request,'user.html')



# from django.shortcuts import render
# import pyrebase
# config={
#      'apiKey': "AIzaSyD-rD8buMeyKJMVBU3Izxx9OG_NL8GufCs",
#  ' authDomain': "authdemo-14bdc.firebaseapp.com",
#   'projectId': "authdemo-14bdc",
#   'storageBucket': "authdemo-14bdc.appspot.com",
#   'messagingSenderId': "1099509624771",
#   'appId': "1:1099509624771:web:ebf3730a962ef6c8e65776",
#   'measurementId': "G-XD10J88L4L"
# }
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()

