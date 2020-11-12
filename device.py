class MyRouter(object):
    """ This is my first class
    """
    def __init__(self, routername, model, serialNo, ios, manufact_date):
        self.routername = routername
        self.model = model
        self.serialNo = serialNo
        self.ios = ios
        self.manufact_date = manufact_date
        
    def print_router(self, manufact_date):
        print(f" The router name is: {self.routername}.")
        print(f" The router model is: {self.model}.")
        print(f" The router serial number is: {self.serialNo}.")
        print(f" The router IOS version is: {self.ios}.")
        print(f" The router model and date combined: {self.ios} + {self.manufact_date}.")
        
#create MyRouter Object and test
AbujaRouter = MyRouter('Cisco', 'c1500', 888444, 13.5, '20/10/2020')
print(AbujaRouter.print_router(2013))