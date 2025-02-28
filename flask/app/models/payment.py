from app import db
from sqlalchemy_serializer import SerializerMixin

# Model สำหรับตารางข้อมูลการชำระเงิน
class Payment(db.Model, SerializerMixin):
    __tablename__ = "payments"

    payment_id = db.Column(db.Integer, primary_key=True)  # รหัสการชำระเงิน (Primary Key)
    table_id = db.Column(db.Integer, db.ForeignKey('Tables.table_id'), nullable=False)  # รหัสคำสั่งซื้อที่ชำระ (Foreign Key)
    payment_method = db.Column(db.String(50), nullable=False)  # วิธีการชำระเงิน (เงินสด, บัตรเครดิต, QR Payment)
    payment_time = db.Column(db.DateTime, nullable=False)  # เวลาที่ชำระ
    amount = db.Column(db.Float, nullable=False)  # ยอดชำระ
    status = db.Column(db.String, default="Enable")

    '''
    status : Enable, Disable
    '''

    def __init__(self, table_id, payment_method, payment_time, amount):
        self.table_id = table_id
        self.payment_method = payment_method
        self.payment_time = payment_time
        self.amount = amount

    def update(self, payment_method, payment_time, amount, table_id):
        self.payment_method = payment_method
        self.payment_time = payment_time
        self.amount = amount
        self.table_id = table_id

    def change_status(self, status):
        self.status = status
