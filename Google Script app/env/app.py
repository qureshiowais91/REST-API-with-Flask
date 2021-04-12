from flask import Flask, jsonify
from flask_restful import Api, Resource
import os

app = Flask(__name__)
api = Api(app)

class runFiles(Resource):
    def get(self, file_name):
        # checkFileName(file_name)
        file_dir = os.path.dirname(__file__)
        if True == os.path.exists(file_dir):
            file_full_path = os.path.join(file_dir, file_name)
            file = open(file_full_path)
            exec(file.read())
        else:
            print("Error Path Does't Exist")
        # return jsonify({'data': getvalues['total']})
        return None
class getValues(Resource):
    def post(self,jsonObj):
        return jsonObj

# def checkFileName(file_name):
#         whiteListFiles=['test.py','runMe2.py']
#         numberofFile = len(whiteListFiles)
#         for index in whiteListFiles:
#             if whiteListFiles[index] != file_name:
#                 --numberofFile
#                 if index == len(whiteListFiles) & numberofFile == False:
#                     return None

api.add_resource(runFiles, "/runFiles/<string:file_name>")
api.add_resource(getValues,"/getValues/<json:jsonObj>")

if __name__ == '__main__':
    app.run()
