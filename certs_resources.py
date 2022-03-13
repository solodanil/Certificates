from flask import jsonify
from flask_restful import Resource, abort, reqparse

from data import db_session
from data.certs import Cert

parser = reqparse.RequestParser()
parser.add_argument('num', required=False)
parser.add_argument('order', required=False)
parser.add_argument('organisation', required=False)
parser.add_argument('product', required=False)
parser.add_argument('set', required=False)
parser.add_argument('drawing', required=False)
parser.add_argument('product_id', required=False)
parser.add_argument('conditions', required=False)


def abort_if_cert_not_found(cert_id):
    session = db_session.create_session()
    cert = session.query(Cert).get(cert_id)
    if not cert:
        abort(404, message=f"Cert {cert_id} not found")


class CertResource(Resource):
    def get(self, cert_id):
        abort_if_cert_not_found(cert_id)
        session = db_session.create_session()
        cert = session.query(Cert).get(cert_id)
        return jsonify({'cert': cert.to_dict()})

    def put(self, cert_id):
        args = parser.parse_args()
        session = db_session.create_session()
        cert = session.query(Cert).get(cert_id)
        if args.get('num'):
            cert.num = args.get('num')
        if args.get('order'):
            cert.order = args.get('order')
        if args.get('organisation'):
            cert.organisation = args.get('organisation')
        if args.get('product'):
            cert.product = args.get('product')
        if args.get('set'):
            cert.set = args.get('set')
        if args.get('drawing'):
            cert.drawing = args.get('drawing')
        if args.get('product_id'):
            cert.product_id = args.get('product_id')
        if args.get('conditions'):
            cert.conditions = args.get('conditions')
        session.commit()
        return jsonify({'success': 'OK', 'cert': cert.to_dict()})


class CertsListResource(Resource):
    def get(self):
        print(0)
        session = db_session.create_session()
        certs = session.query(Cert).all()
        return jsonify({'certs': [item.to_dict() for item in certs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        cert = Cert()
        if args.get('num'):
            cert.num = args.get('num')
        if args.get('order'):
            cert.order = args.get('order')
        if args.get('organisation'):
            cert.organisation = args.get('organisation')
        if args.get('product'):
            cert.product = args.get('product')
        if args.get('set'):
            cert.set = args.get('set')
        if args.get('drawing'):
            cert.drawing = args.get('drawing')
        if args.get('product_id'):
            cert.product_id = args.get('product_id')
        if args.get('conditions'):
            cert.conditions = args.get('conditions')
        session.add(cert)
        session.commit()
        return jsonify({'success': 'OK', 'cert': cert.to_dict()})
