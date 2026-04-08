from modelloader.base_model_loader import BaseModelLoader


class LicensePlateDetection(BaseModelLoader):
    def __init__(self, config, model_name):
        from licenseplatedetectioninference import LicensePlateDetection as LicensePlateDetectionInference
        wpod_net_json                           = config[model_name]['wpod_net']
        wpod_net_weight                         = config[model_name]['wpod_net_weight']
        MobileNets_character_recognition_json   = config[model_name]['MobileNets_character_recognition']
        MobileNets_character_recognition_weight = config[model_name]['License_character_recognition_weight']
        license_character_classes               = config[model_name]['license_character_classes']

        self.model_obj = LicensePlateDetectionInference(
            wpod_net_json,
            wpod_net_weight,
            MobileNets_character_recognition_json,
            MobileNets_character_recognition_weight,
            license_character_classes
        )

    def predict(self, Base_64, Cs, req_data=None):
        if req_data is None:
            req_data = {}
        return self.model_obj.executeModel(Base_64, Cs, req_data)

    def predict_request(self, req_data):
        Base_64 = req_data.get("Base_64", "")
        Cs = req_data.get("C_threshold", 0.3)
        result = self.predict(Base_64, Cs, req_data)

        # Merge original request fields into result
        for key in ["Tid", "Did", "Fid", "Ffp", "Lfp", "Ltsize", "Ts", "Ts_ntp", "Inf_ver", "Msg_ver", "Ad", "Mtp"]:
            if key in req_data:
                result[key] = req_data[key]

        # Map RC -> Rc and RM -> Rm (ModelResult schema uses lowercase c/m)
        result["Rc"] = result.pop("RC", "500")
        result["Rm"] = result.pop("RM", "")

        # ModelResult requires Fs — use Objects if Fs not present
        if "Fs" not in result:
            result["Fs"] = result.pop("Objects", [])

        # Add missing required response fields with defaults
        result.setdefault("Obase_64", [])
        result.setdefault("Img_url", [])

        return result