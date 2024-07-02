from models import BIT_TYPE_DICT


class Config:

    def __init__(self, quant_method='minmax'):
        '''
        '''
        self.BIT_TYPE_W = BIT_TYPE_DICT['int8']
        self.BIT_TYPE_A = BIT_TYPE_DICT['uint8']

        self.OBSERVER_W = 'minmax'
        self.OBSERVER_A = quant_method

        self.QUANTIZER_W = 'uniform'
        self.QUANTIZER_A = 'uniform'

        self.CALIBRATION_MODE_W = 'channel_wise'
        self.CALIBRATION_MODE_A = 'layer_wise'
