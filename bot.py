import os

from pygame import mixer
from flask import Flask


app = Flask(__name__)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)


@app.route("/upgrade")
def hello():
    mixer.init()
    mixer.music.load(os.path.join(ROOT_DIR, 'upgrade_complete.mp3'))
    mixer.music.set_volume(0.7)
    mixer.music.play()
    return "OK"

if __name__ == "__main__":
    app.run()
