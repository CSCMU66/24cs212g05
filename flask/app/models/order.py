from app import db
from app import app
from sqlalchemy_serializer import SerializerMixin
import datetime
from app.models.menu import Menu

# # Model สำหรับตารางข้อมูลคำสั่งซื้อ
class Order(db.Model, SerializerMixin):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)  # รหัสคำสั่งซื้อ (Primary Key)
    table_id = db.Column(db.Integer, db.ForeignKey('Tables.table_id'), nullable=False)  # รหัสโต๊ะที่สั่ง (Foreign Key)
    order_time = db.Column(db.DateTime, nullable=False)  # เวลาที่สั่ง
    status = db.Column(db.String(20), nullable=False, default="Preparing")  # สถานะคำสั่งซื้อ
    
    '''
    สถานะคำสั่งซื้อ (Preparing, Ready, Served, Paid)
    '''
    menu_list = db.Column(db.JSON, nullable=False)
    '''Menu_list = {menu_id : amount}'''
    total_price = db.Column(db.Float, nullable=False, default=0.0)  # ยอดรวมคำสั่งซื้อ

    
    
    def __init__(self, table_id, time, menu_list, status="Preparing"):
        self.table_id = table_id
        self.order_time = time
        self.status = status
        self.menu_list = menu_list


    def update_status(self, status):
        self.status = status

    def change_price(self, price):
        self.total_price = price