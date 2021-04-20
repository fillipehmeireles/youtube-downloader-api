from flask import request

# download service
from ..services import Downloader

# responses
from ..custom import Responses

custom = Responses()

class DownloadController:
    def __init__(self):
        self.url: str
        self.downloader = Downloader()
        self.downloadType = {
            'music': self.downloader.downloadMusic,
            'video': self.downloader.downloadVideo
        }

    def download(self, downloadType: str):
        try:
            self.url = request.json['video-url']
        except KeyError as error:
            return custom.send(400,'Nonexistent URL')
        result = self.downloadType[downloadType](videoUrl=self.url)
        return result
    