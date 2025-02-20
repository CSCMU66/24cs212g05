import json
from flask import (jsonify, render_template,
                  request, url_for, flash, redirect)

from app import app
from app import db
from sqlalchemy.sql import text
import datetime

from app.models.table import Tables
from app.models.order import Order
from app.models.payment import Payment

@app.route('/payment/get_all_payment')
def payment_list():
    db_payment = Payment.query.all()
    payments = list(map(lambda x: x.to_dict(), db_payment))
    payments.sort(key=(lambda x: x['payment_id']))
    return jsonify(payments)


@app.route('/payment/create', methods=('GET', 'POST'))
def payment_create():
    app.logger.debug("Payment - CREATE")
    if request.method == 'POST':
        
        result = request.form.to_dict()

        validated = True
        valid_keys = ['order_id', 'payment_method', 'payment_time', 'amount']
        validated_dict = dict()
        for key in result:
            app.logger.debug(f"{key}: {result[key]}")
            # screen of unrelated inputs
            if key not in valid_keys:
                continue


            value = result[key].strip()
            if not value or value == 'undefined':
                validated = False
                break
            if key == 'is_employee' and result[key].lower() != "true":
                validated = False    
                break
            validated_dict[key] = value
            
        if validated:
            try:
                temp = Payment(**validated_dict)
                db.session.add(temp)
                
                db.session.commit()
                
            except Exception as ex:
                app.logger.error(f"Error create new order: {ex}")
                raise
            
    return payment_list()


@app.route('/payment/update', methods=('GET', 'POST'))
def payment_update():
    app.logger.debug("Payment - UPDATE")
    if request.method == 'POST':
        
        result = request.form.to_dict()

        validated = True
        valid_keys = ['payment_id', 'order_id', 'payment_method', 'payment_time', 'amount']
        validated_dict = dict()
        for key in result:
            app.logger.debug(f"{key}: {result[key]}")
            # screen of unrelated inputs
            if key not in valid_keys:
                continue


            value = result[key].strip()
            if not value or value == 'undefined':
                validated = False
                break
            if key == 'is_employee' and result[key].lower() != "true":
                validated = False    
                break
            validated_dict[key] = value
            
        if validated:
            try:
                payment = Payment.query.get(validated_dict['payment_id'])
                payment.update(
                    payment_method=validated_dict['payment_method'],
                    payment_time=validated_dict['payment_time'],
                    amount=validated_dict['amount']
                )
                db.session.commit()
                
            except Exception as ex:
                app.logger.error(f"Error create new order: {ex}")
                raise
            
    return payment_list()

@app.route('/payment/delete', methods=('GET', 'POST'))
def payment_delete():
    app.logger.debug("Payment - DELETE")
    if request.method == 'POST':
        
        result = request.form.to_dict()

        validated = True
        valid_keys = ['payment_id']
        validated_dict = dict()
        for key in result:
            app.logger.debug(f"{key}: {result[key]}")
            # screen of unrelated inputs
            if key not in valid_keys:
                continue


            value = result[key].strip()
            if not value or value == 'undefined':
                validated = False
                break
            if key == 'is_employee' and result[key].lower() != "true":
                validated = False    
                break
            validated_dict[key] = value
            
        if validated:
            try:
                payment = Payment.query.get(validated_dict['payment_id'])
                db.session.delete(payment)
                db.session.commit()
                
            except Exception as ex:
                app.logger.error(f"Error create new order: {ex}")
                raise
            
    return payment_list()