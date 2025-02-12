import json
from sqlalchemy.sql import text
from app import app
from app import db
from flask import (jsonify, render_template,
                  request, url_for, flash, redirect)
from datetime import datetime, timedelta
from app.models.payment import Payment

@app.route('/revenue')
def revenue():
    return render_template('Admin_page/Revenue.html')