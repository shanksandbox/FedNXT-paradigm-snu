from flask import Flask,request
from flask_restful import Resource, Api
import pickle
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
#
CORS(app)
# creating an API object
api = Api(app)


#prediction api call
class prediction(Resource):
    def get(self,budget):
        #budget = request.args.get('budget')
       # print(budget)
        # Let's load the package
        budget = [str(budget)]
        df = pd.DataFrame(budget, columns=['Marketing Budget (X) in Thousands'])
        filename='simple_linear_regression.pkl'
        loaded_model=pickle.load(open(filename,'rb'))
        pred_result=loaded_model.predict([[1,12,7758.83]])
        return list(pred_result)

#data api
class getData(Resource):
    def get(self):
            df = pd.read_excel('Dataset_Hackathon.xlsx')
            df =  df.rename({'Country': 'Destination', 'Frieght Cost (USD)': 'Estimated Cost'}, axis=1)  # rename columns
            #print(df.head())
            #out = {'key':str}
            res = df.to_json(orient='records')
            #print( res)
            return res

#
api.add_resource(getData, '/api')
api.add_resource(prediction, '/prediction/<int:budget>')

if __name__ == '__main__':
    app.run(debug=True)
