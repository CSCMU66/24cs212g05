# from app.controllers import ctable_mange
from app.controllers import table_manage
from app.controllers import menu_manage
from app.controllers import employee_manage

from app.controllers import order_manage

from flask import (jsonify, render_template,
                   request, url_for, flash, redirect)
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from app import app