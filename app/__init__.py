from flask import Flask
import sketch
import api

app = Flask(__name__)
app.register_blueprint(sketch.bp)
app.register_blueprint(api.bp)

@app.route('/')
def hello():
    return 'Please goto /sketch or /api'

#######################################
######you will start this app here#####
#######Write Flask start code here#####
#######################################