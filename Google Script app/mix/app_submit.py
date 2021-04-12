from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class sumUp(Resource):
    def get(self,arg_one,arg_two):
        total = 0
        total =  float(arg_one)+float(arg_two)
        return float(total)

api.add_resource(sumUp,"/sumUp/<string:arg_one>/<string:arg_two>")

if __name__ == '__main__':
   app.run()