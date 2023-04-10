import cv2
import mediapipe as mp
import datetime

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from login.forms import *
from login.backend import *


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class LoginUserWithVideo(LoginView):
    form_class = LoginUserWithVideoForm
    template_name = 'users/loginWithVideo.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@csrf_exempt
def classification(request):
    print("!!!")
    mp_hands = mp.solutions.hands

    video = request.FILES['video']
    video_path = video.temporary_file_path()
    print(video_path)

    cap = cv2.VideoCapture(video_path)

    first_time = datetime.datetime.now()

    result = 'None'
    with mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

        if not cap.isOpened():
            print("File Cannot be Opened")

        length = int(cap.get(cv2.CAP_PROP_FPS))
        print(length)


        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break


            results = hands.process(image)
            image_height, image_width, _ = image.shape



            count_of_left_up =count_of_right_up = count_of_left_down = count_of_right_down = 0

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for ids, landmrk in enumerate(hand_landmarks.landmark):

                        cx, cy = landmrk.x * image_width, landmrk.y * image_height

                        if(cx>=image_width/2 and cy<=image_height/2):
                            count_of_left_up = count_of_left_up+1
                        if (cx >= image_width / 2 and cy >= image_height / 2):
                            count_of_left_down = count_of_left_down + 1
                        if (cx <= image_width / 2 and cy <= image_height / 2):
                            count_of_right_up = count_of_right_up + 1
                        if (cx <= image_width / 2 and cy >= image_height / 2):
                            count_of_right_down = count_of_right_down + 1

                if count_of_left_up > 17:
                    result = 'Левый верхний угол'
                if count_of_left_down > 17:
                    result = 'Левый нижний угол'
                if count_of_right_up > 17:
                    result = 'Правый верхний угол'
                if count_of_right_down > 17:
                    result = 'Правый нижний угол'


    later_time = datetime.datetime.now()
    difference = later_time - first_time
    print(difference)




    response = {
        'classification': result
    }
    return JsonResponse(response)


