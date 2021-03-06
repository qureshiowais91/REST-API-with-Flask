from flask import Flask, jsonify
from flask_restful import Api, Resource
import os

app = Flask(__name__)
api = Api(app)


class callApi(Resource):
    def get(self, file_name):
        checkFileName(file_name)
        my_dir = os.path.dirname(__file__)
        file_path = os.path.join(my_dir, file_name)
        file = open(file_path)
        getvalues = {}
        exec(file.read(), getvalues)
        return jsonify({'data': getvalues['total']})


def checkFileName(file_name):
        whiteListFiles=['test.py','runMe2.py']
        numberofFile = len(whiteListFiles)
        for index in whiteListFiles:
            if whiteListFiles[index] != file_name:
                --numberofFile
                if index == len(whiteListFiles) & numberofFile == False:
                    return None

api.add_resource(callApi, "/callApi/<string:file_name>")

if __name__ == '__main__':
    app.run()
