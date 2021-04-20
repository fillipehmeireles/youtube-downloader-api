from flask import (
    Blueprint,
    jsonify
)

# Download controller
from ..controllers import DownloadController

downloadBlueprint = Blueprint('downloadBlueprint', __name__)

@downloadBlueprint.route('/download-video', methods = ['POST'])
def downloadVideo() -> str:
    response = DownloadController().download('video')
    return jsonify(response['message']), response['statusCode']

@downloadBlueprint.route('/download-music', methods = ['POST'])
def downloadMusic() -> str:
    response = DownloadController().download('music')
    return jsonify(response['message']), response['statusCode']