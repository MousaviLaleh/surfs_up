
# import flask dependency
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask

# craete a new flask app instance
app = Flask(__name__)

# create a flask route
@app.route('/')

# create a function
def hello_world():
    return 'You Did It'

