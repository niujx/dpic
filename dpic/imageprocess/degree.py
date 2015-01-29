__author__ = 'yanshi'

'''
	ORIG		(0,		480,	800,	TRANS_ORIG),
	ID_52X52	(1,		52,		52,		TRANS_SMALL),
	ID_75X75	(2, 	75,		75,		TRANS_SMALL),
	ID_81X71	(3, 	81,		71,		TRANS_SMALL),
	ID_122X108	(4, 	122,	108,	TRANS_SMALL),
	ID_240X320	(5, 	240,	320,	TRANS_MID),
	ID_320X240	(6, 	320,	240,	TRANS_MID),
	ID_320X480	(7, 	320,	480,	TRANS_MID),
	ID_480X800	(8, 	480,	800,	TRANS_MID),
	ID_150X150	(9, 	150,	150,	TRANS_SMALL),
	ID_162X142	(10,	162,	142,	TRANS_SMALL),
	ID_122X108_2(36, 	122,	108,	TRANS_SMALL);
'''

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
            # Degree(-1),
            # Degree(0),
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
