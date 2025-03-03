from flask_login import login_required
from app.controllers.role_controller import roles_required
from flask import (jsonify, render_template,
                  request, url_for, flash, redirect)
from app import app

@app.route('/review')
def review():
    return render_template('review_page.html')