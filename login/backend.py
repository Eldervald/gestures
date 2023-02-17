import base64
import pickle
import requests
import os
import json
from urllib import request
from django.contrib.auth import login, get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pathlib import Path
from gestures import settings
from login.models import CustomUser
from login import models


class MultiPasswordModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, video=None):
        try:
            user = CustomUser.objects.get(username=username)
            if password is None and video is not None:
                embedding_video_from_site = self.getEmbeddingFromVideo(video)
                embedding_original_video = self.getEmbeddingFromDataBase(username)
                if(embedding_original_video==embedding_video_from_site):
                    return user
                #item_video = CustomUser.objects.filter(username=username).first().video
            elif user.check_password(password) and self.user_can_authenticate(user):
                return user
        except CustomUser.DoesNotExist:
            pass



    def getEmbeddingFromDataBase(self, username):
        item_video_Embedding = CustomUser.objects.filter(username=username).first().videoEmbedding
        list_bytes = base64.b64decode(item_video_Embedding)
        list = pickle.loads(list_bytes)
        return list


    def getEmbeddingFromVideo(self, video):
        BASE_DIR = Path(__file__).resolve().parent.parent
        path = os.path.join(BASE_DIR, 'media', video.name)
        url = "http://127.0.0.1:5000"

        payload = {'name': 'branch'}
        files = [
            ('content', (
                'tmp.mp4',
                # open(path, 'rb'),
                video.open(mode='rb'),
                'application/octet-stream'))
        ]
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        return json.loads(response.text)['embedding']
