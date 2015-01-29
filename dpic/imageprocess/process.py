__author__ = 'yanshi'

import requests
from PIL import Image

from dpic import settings
from dpic.imageprocess.degree import Degree


class ImageProcess(object):
    pass


class ImageCutProcess(ImageProcess):
    def process(self, picPath):
        with Image.open(picPath) as img:
            print img.size, img.filename
            maxHeight = img.size[1] - 135
        files = {'picCode': open(picPath, 'rb'), 'method': 'transOri', 'maxWeight': str(img.size[0]),
                 'maxHeight': str(maxHeight)}
        r = requests.post(url=settings.IMAGE_PROCESS_CALL, files=files)
        if int(r.headers['content-length']) > 700:
            with open('/home/yanshi/dpic/test/t5.jpg', 'wb') as imageFile:
                imageFile.write(r.content)


class ImageDegreeProcess(ImageProcess):
    def process(self, picPath):
        for degree in Degree.get_degrees():
            files = {'picCode': open(picPath, 'rb'), 'method': degree.method, 'maxWeight': degree.width,
                     'maxHeight': degree.height}

            r = requests.post(url=settings.IMAGE_PROCESS_CALL, files=files)




if __name__ == '__main__':
    ImageDegreeProcess().process(picPath=None)
