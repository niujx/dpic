# -*- coding: utf-8 -*-
__author__ = 'yanshi'
import StringIO
import requests
import json
from PIL import Image
from dpic import settings

TRANS_SMALL = 'transSmall'
TRANS_MID = 'transMid'


class Degree(object):
    def __init__(self, value, width=None, height=None, method=None):
        self.value = value
        self.width = width
        self.height = height
        self.method = method

    @staticmethod
    def get_degrees():
        return [
            Degree(-1),
            Degree(0),
            Degree(1, 52, 52, TRANS_SMALL),
            Degree(2, 75, 75, TRANS_SMALL),
            Degree(3, 81, 71, TRANS_SMALL),
            Degree(4, 122, 108, TRANS_SMALL),
            Degree(5, 240, 320, TRANS_MID),
            Degree(6, 320, 240, TRANS_MID),
            Degree(7, 320, 480, TRANS_MID),
            Degree(8, 480, 800, TRANS_MID),
            Degree(9, 150, 150, TRANS_SMALL),
            Degree(10, 162, 142, TRANS_SMALL),
        ]


class ImageDegreeProcess(object):
    def process(self, pic_path):
        b_image = self._cut_image_process(pic_path)
        if not b_image:
            return
        for degree in Degree.get_degrees():
            if degree.value != 0 and degree.value != -1:
                r = self._call_image_service(call_url=settings.IMAGE_PROCESS_CALL, method=degree.method,
                                             image_file=b_image, weight=degree.width, height=degree.height)
                params = {'fs': r.content}
            else:
                params = {'fs': b_image}
            upload_image = requests.post(url=settings.IMAGE_UPLOAD, files=params)
            image_info = json.loads(upload_image.text)
            yield degree.value, image_info['result']


    @staticmethod
    def _cut_image_process(pic_path):
        with Image.open(pic_path) as img:
            del_head, del_tail = 40, 75
            out_data = StringIO.StringIO()
            w, h = img.size
            if (h - del_head - del_tail) < 100:
                return

            if w > 400 or h > 400:
                img = img.crop((0, del_head, w, h - del_tail))
            out_data.seek(0)
            img.save(out_data, "JPEG", quality=50)
            out_data.seek(0)
            return out_data.getvalue()

    @staticmethod
    def _call_image_service(call_url, method, image_file, weight=None, height=None):

        params = {'picCode': image_file, 'method': method, 'maxWeight': str(weight),
                  'maxHeight': str(height)}
        r = requests.post(call_url, files=params)
        if r.status_code == 200:
            return r

