from requests import get

from apis.Api import Api
from apis.response.LabReportModel import LabReportModel


class LabReportApi(Api):
    fake_data = [
        LabReportModel(1, "V"),
        LabReportModel(2, "D"),
        LabReportModel(3, "D"),
        LabReportModel(4, "D"),
        LabReportModel(5, "F"),
    ]

    def find_all(self):
        return self.fake_data

    def find_by_id(self, id):
        for model in self.fake_data:
            if model.id == id:
                return model

    def search(self, query):
        pass
