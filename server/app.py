# Using flask to make an api
# import necessary libraries and functions
from flask import Flask
from flask_restful import Api

from server.business_search import *
from server.business_settings import *
from server.queue_management import *
from server.statistics import *
from server.MyQueue import *
from server.user import *
from server.my_workers import *
from server.measures import *
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class EMPTY(Resource):

    def get(self):
        return "<h1>hello world</h1>"


# adding the defined resources along with their corresponding urls
api.add_resource(RegisterBusiness, '/RegisterBusiness')
api.add_resource(RegisterWorker, '/RegistrationWorker')
api.add_resource(Registration, '/Registration')
api.add_resource(Login, '/Login')
api.add_resource(AvailableQueues, '/AvailableQueues')
api.add_resource(GetQueue, '/GetQueue')
api.add_resource(GetMyQueue, '/GetMyQueue')
api.add_resource(EMPTY, '/')
api.add_resource(updateSettings, '/businessSettings')
api.add_resource(getBusinesses, '/getBusinesses')
api.add_resource(LetsUserIntoBusiness, '/LetsUserIntoBusiness')
api.add_resource(LetsUserOutBusiness, '/LetsUserOutBusiness')
api.add_resource(deleteAppointment, '/deleteAppointment')
api.add_resource(currentAmountAtBusiness, '/currentAmount')
api.add_resource(generateCodeForSpontaneousAppointment, '/SpontaneousAppointment')
api.add_resource(GetMyWorkers, '/GetMyWorkers')
api.add_resource(RemoveMyWorkers, '/RemoveWorkers')
api.add_resource(getAmountOfCostumersForDayAndHour, '/AmountForDayAndHour')
api.add_resource(UpdateMyMessage, '/UpdateMyMessage')
api.add_resource(GetBusinessMessage, '/GetBusinessMessage')
api.add_resource(getPreciseAmountOfCostumers, '/PreciseAmount')
api.add_resource(MeasureUrlsResponse, '/MeasureUrlsResponse')
# api.add_resource(MeasureUrlsResponseTime, '/MeasureUrlsResponseTime')
api.add_resource(avgStatisticsPerHour, '/avgStats')





# driver function

if __name__ == '__main__':
    app.run(debug=True)
