import pickle
import pandas as pd

from app.domain.responses import ResponsePrediction

class GetPovertyPrediction:
    
    def __init__(self, config):
        with open(config['MODEL_PATH'], 'rb') as f:
            import os
            model_data = pickle.load(f)
        self.model = model_data['model']
        # Encoder is a dict with a LabelBinarizer per column
        self.encoder = model_data['encoder']
        self.column_mapping = model_data['column_mapping']
        self.column_order = model_data['column_order']

    def preprocess(self, variables):
        allowed_variables = [
            "kjkrfgld", 
            "bpowgknt",
            "raksnhjf", 
            "vwpsxrgk", 
            "omtioxzz", 
            "yfmzwkru", 
            "tiwrsloh", 
            "weioazcf"
        ]
        data = pd.DataFrame(index=[0], columns=self.column_order, dtype=float)
        for allowed_variable in allowed_variables:
            if allowed_variable not in variables.keys():
                continue
            variable_name_mapped = self.column_mapping.get(allowed_variable)
            raw_value = variables.get(allowed_variable)
            if variable_name_mapped is None:
                continue
            if variable_name_mapped in self.encoder.keys():
                col_encoded = [col for col in self.column_order if variable_name_mapped in col]
                data[col_encoded] = 0
                variable_name_mapped = '%s_%s' % (variable_name_mapped, raw_value)
                data[variable_name_mapped] = 1
            else:
                data[variable_name_mapped] = raw_value
    
        return data

    def execute(self, variables):
        data = self.preprocess(variables)
        score = float(self.model.predict(data)[0])
        response = ResponsePrediction.create(score)
        return response