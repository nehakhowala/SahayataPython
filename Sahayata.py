from flask import Flask, render_template, request
from MessagingService import push_notifications
from AreaClassifierService import takeLatLongReturnCrimeNumbers, classifyArea

app = Flask(__name__)

from werkzeug.routing import FloatConverter as BaseFloatConverter

class FloatConverter(BaseFloatConverter):
    regex = r'-?\d+(\.\d+)?'

app.url_map.converters['float'] = FloatConverter

@app.route('/')
def launcher():
    response = push_notifications()
    return response

@app.route('/spitCrimeNumber/<float:lat>/<float:longi>')
def getCrimes(lat,longi):

	z = takeLatLongReturnCrimeNumbers(lat,longi)
    	return str(z)


# Run the app
if __name__ == '__main__':
    print ("***************server called***************")
    app.run(
        host="0.0.0.0",
        port=int("5000"),
        debug=True,
        use_reloader = False
    )
