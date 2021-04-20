from pydub import AudioSegment

class ConvertToMp3:
    def __new__(cls,fileInfo):
        try:
            cls.webmFile = AudioSegment.from_file(fileInfo['fileName'], format = 'webm')
            cls.webmFile.export(f"{fileInfo['fileName'].replace('.webm','mp3')}", format = 'mp3')
        except Exception as error:
            return str(error)
        return True