from requests import get

from apis.Api import Api
from apis.response.LabReportModel import LabReportModel


class DrugApi(Api):
    fake_data = [
        LabReportModel(1, "Pandoll"),
        LabReportModel(2, "Vitermin c"),
        LabReportModel(3, "Glimin"),
        LabReportModel(4, "MDR"),
        LabReportModel(5, "Sep"),
    ]

    def find_all(self):
        return self.fake_data

    def find_by_id(self, id):
        for model in self.fake_data:
            if model.id == id:
                return model

    def search(self, query):
        pass
