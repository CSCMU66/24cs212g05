from flask import (jsonify, render_template,
                  request, url_for, flash, redirect)
from flask_login import login_required
from app.controllers.role_controller import roles_required
from app import app

@app.route('/waiter')
@login_required
@roles_required('Admin', 'Waiter')
def waiter():
    return render_template('waiter_page/base.html')