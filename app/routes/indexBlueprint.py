from flask import Blueprint

indexBlueprint = Blueprint('index',__name__)

@indexBlueprint.route('/')
def index() -> str:
    return 'Youtube Video and Music Downloader Api v1.0'