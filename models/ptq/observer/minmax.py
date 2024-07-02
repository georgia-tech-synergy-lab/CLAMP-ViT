# Adapted from MEGVII Inc.
# https://github.com/megvii-research/FQ-ViT/tree/main
import torch

from .base import BaseObserver


class MinmaxObserver(BaseObserver):

    def __init__(self, module_type, bit_type, calibration_mode):
        super(MinmaxObserver, self).__init__(module_type, bit_type,
                                             calibration_mode)
        self.symmetric = self.bit_type.signed

    def update(self, v):
        v = self.reshape_tensor(v)
        cur_max = v.max(axis=1).values
        if self.max_val is None:
            self.max_val = cur_max
        else:
            self.max_val = torch.max(cur_max, self.max_val)
        cur_min = v.min(axis=1).values
        if self.min_val is None:
            self.min_val = cur_min
        else:
            self.min_val = torch.min(cur_min, self.min_val)

        if self.calibration_mode == 'layer_wise':
            self.max_val = self.max_val.max()
            self.min_val = self.min_val.min()

    def get_quantization_params(self, *args, **kwargs):
        max_val = self.max_val
        min_val = self.min_val

        qmax = self.bit_type.upper_bound
        qmin = self.bit_type.lower_bound

        scale = torch.ones_like(max_val, dtype=torch.float32)
        zero_point = torch.zeros_like(max_val, dtype=torch.int64)

        if self.symmetric:
            max_val = torch.max(-min_val, max_val)
            scale = max_val / (float(qmax - qmin) / 2)
            scale.clamp_(self.eps)
            zero_point = torch.zeros_like(max_val, dtype=torch.int64)
        else:
            scale = (max_val - min_val) / float(qmax - qmin)
            scale.clamp_(self.eps)
            zero_point = qmin - torch.round(min_val / scale)
            zero_point.clamp_(qmin, qmax)
        return scale, zero_point
