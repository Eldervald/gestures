import base64
import hashlib
import json
import pickle

import requests
from urllib import request

from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    videoEmbedding = models.BinaryField()


    __original_video = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_video = self.video




    def save(self, *args, **kwargs):
        if self.video != self.__original_video:
           print(type(self.video))
           self.videoEmbedding = self.get_embedding()
        super(CustomUser, self).save(*args, **kwargs)


    def get_embedding(self):
        url = "http://127.0.0.1:5000"

        payload = {'name': 'branch'}
        files = [
            ('content', (
                'tmp.mp4',
                # open(path, 'rb'),
                self.video.open(mode='rb'),
                'application/octet-stream'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        list_bytes = pickle.dumps(json.loads(response.text)['embedding'])

        list_bytes64 = base64.b64encode(list_bytes)

        return list_bytes64





