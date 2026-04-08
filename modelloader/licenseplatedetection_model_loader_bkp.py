# ===============================================================================================================#
# Copyright 2024 Infosys Ltd.                                                                                    #
# Use of this source code is governed by Apache License Version 2.0 that can be found in the LICENSE file or at  #
# http://www.apache.org/licenses/                                                                                #
# ===============================================================================================================#

import json
from modelloader.base_model_loader import BaseModelLoader
from keras.models import Model
import keras
import tensorflow as tf



class LicensePlateDetection(BaseModelLoader):
    def __init__(self, config, model_name):
        """
        Initialize the Detecto model loader.

        Args:
            config (dict): The configuration dictionary.
            model_name (str): The name of the modelloader.

        """
        from licenseplatedetectioninference import LicensePlateDetection    
        print(keras.__version__)
        print(tf.__version__)    
        wpod_net_json = config[model_name]['wpod_net']
        wpod_net_weight = config[model_name]['wpod_net_weight']
        MobileNets_character_recognition_json = config[model_name]['MobileNets_character_recognition']
        MobileNets_character_recognition_weight = config[model_name]['License_character_recognition_weight']
        license_character_classes = config[model_name]['license_character_classes']
        self.model_obj = LicensePlateDetection(wpod_net_json, wpod_net_weight,
                 MobileNets_character_recognition_json, MobileNets_character_recognition_weight,
                 license_character_classes)