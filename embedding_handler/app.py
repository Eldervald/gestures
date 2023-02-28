import json

from flask import Flask, request
import os
from settings import *
from src.video_utils import read_video
from src.handler import video2emb

app = Flask(__name__)


@app.route('/', methods=['POST'])
def video2vec():
    file = request.files['content']
    if not os.path.exists(TEMPORAL_VIDEO_FOLDER):
        os.mkdir(TEMPORAL_VIDEO_FOLDER)
    path = os.path.join(TEMPORAL_VIDEO_FOLDER, file.filename)
    file.save(path)
    video = read_video(path)
    emb = video2emb(video)

    return json.dumps({'embedding': list(emb)})


if __name__ == '__main__':
    app.run(debug=True)
