from apis.Api import Api
from apis.response.BillingModel import BillingModel


class BillingApi(Api):
    fake_data = [
        BillingModel(1, "2020/2/3", 5004, 'Doug fees', 2300, 'Completed'),
        BillingModel(1, "2020/10/3", 5004, 'Lab fees', 200, 'Pending'),
        BillingModel(1, "2020/2/5", 5004, 'Doug fees', 2700, 'Completed'),
        BillingModel(1, "2020/3/4", 5004, 'Doug fees', 500, 'Close'),
        BillingModel(1, "2020/2/9", 5004, 'Doug fees', 9500, 'Completed'),
    ]

    def find_all(self):
        return self.fake_data

    def find_by_id(self, id):
        for model in self.fake_data:
            if model.id == id:
                return model

    def search(self, query):
        pass
