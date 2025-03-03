from flask_login import login_required
from app.controllers.role_controller import roles_required
from flask import (jsonify, render_template,
                  request, url_for, flash, redirect)

import jwt
from manage import SECRET_KEY

from app.models.table import Tables
from app import app

@app.route('/menu/table/<token>', methods=['GET', 'POST'])
def menu(token):
    table_number, count = decode_jwt(token)
    db_allTable = Tables.query.get(table_number)
    table = db_allTable.to_dict()
    app.logger.debug(count)
    if table['count'] != count:
        return render_template('test.html', table_id='Something wrong with your QRcode')
    
    app.logger.debug(not table_number)
    if not table_number:
        return "Invalid or expired token", 400

    if request.method == 'GET':
        # selected_items = request.form.getlist('item')  # List of selected items' ids
        # return render_template('order_summary.html', table_number=table_number, selected_items=selected_items, menu_items=menu_items)
        return render_template('order_page/index.html', table_id=table_number, count=count)

    # return render_template('menu.html', menu_items=menu_items, table_number=table_number)
    return render_template('test.html', table_id='Something wrong with your QRcode')

def decode_jwt(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded['table_number'], decoded['count']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None