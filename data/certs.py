import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


class Cert(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'certs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True)
    num = sqlalchemy.Column(sqlalchemy.String, index=True)
    order = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    organisation = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    product = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    set = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    drawing = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    product_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    conditions = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    status = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)
    is_editable = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # 0 — создан
    print_date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)

    # created_by
    # printed_by
    # shop

    def __repr__(self):
        return f'<Certificate {self.id} {self.num}>'
