from flask import Flask, render_template, request
from MessagingService import push_notifications

app = Flask(__name__)


@app.route('/')
def launcher():
    response = push_notifications()
    return response


# Run the app
if __name__ == '__main__':
    print ("***************server called***************")
    app.run(
        host="0.0.0.0",
        port=int("5000"),
        debug=True,
        use_reloader = False
    )
