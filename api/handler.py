import pickle
import pandas as pd
import os

from flask             import Flask, request, Response
from rossmann.Rossmann import Rossmann

print('teste1')

# loading model 
model = pickle.load( open( 'C:/Users/leona/repos/DataScience_Em_Producao/model/model_rossmann.pkl', 'rb' ) )

print('teste2')


# initialize API
app = Flask( __name__ )

print('teste3')


@app.route( '/rossmann/predict', methods=['POST'] )
def rossmann_predict():
    print('teste4') 	
    test_json = request.get_json()
    print('teste5')
           
    if test_json: # there is data        
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0])
        
        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
           
        # Instantiate Rossman Class 
        pipeline = Rossmann()           
           
        # data cleaning 
        df1 = pipeline.data_cleaning( test_raw )
           
        # feature engineering
        df2 = pipeline.feature_engineering( df1 )
           
        # data preparation
        df3 = pipeline.data_preparation( df2 ) 
           
        # prediction 
        df_response = pipeline.get_prediction( model, test_raw, df3 )
        
        return df_response
           
    else:
           return Response( '{}', status=200, mimetype='application/json' )
           
           
if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000)
    app.run( host='0.0.0.0', port=port )