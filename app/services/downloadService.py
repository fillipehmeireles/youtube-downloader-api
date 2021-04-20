import os

from pytube import YouTube

# custom responses
from ..custom import Responses

# tool to convert webm to mp3
from ..tools import ConvertToMp3

# rename file as unique on directory
from ..utils import RenameFile

custom = Responses()
utils = RenameFile()


class Downloader:
    def __init__(self):
        self.videoDownloadDir = 'tmp/video/'
        self.songDownloadDir = 'tmp/song/'

    def downloadVideo(self, videoUrl: str) -> custom:
        try:
            self.ytVideo = YouTube(videoUrl)
            self.originalVideoTitle = self.ytVideo.streams[0].title
            self.newVideoTitle: str = utils.rename(self.originalVideoTitle)
            self.ytVideo.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first().download(self.videoDownloadDir, filename=self.newVideoTitle)
        except Exception as error:
            return custom.send(400, str(error))
        return custom.send(202, 'Done!')

    def downloadMusic(self, videoUrl: str) -> custom:
        try:
            self.ytVideo = YouTube(videoUrl)
            self.originalSongTitle = self.ytVideo.streams[0].title
            self.newMusicTitle = utils.rename(self.originalSongTitle)
            self.ytVideo.streams.filter(only_audio=True, subtype='webm').order_by(
                'abr').first().download(self.songDownloadDir, filename=self.newMusicTitle)
            toMp3 = ConvertToMp3(
                {f'fileName': f'{self.songDownloadDir}/{self.newMusicTitle}.webm'})
            os.remove(f'{self.songDownloadDir}{self.newMusicTitle}.webm')

        except Exception as error:
            return custom.send(400, str(error))
        return custom.send(202, 'Done!')
