class BillingModel(object):

    def __init__(self, id, date, bil_no, description, total, status):
        self.id = id
        self.date = date
        self.bil_no = bil_no
        self.description = description
        self.total = total
        self.status = status
