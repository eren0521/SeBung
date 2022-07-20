from flask import Flask, jsonify, request
from test import database
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)

api = Api(app, version='1.0', title='세붕이 API 문서', description='Swagger 문서', doc="/api-docs")

GET_api = api.namespace('GET', description='API')
POST_api = api.namespace('POST', description='API')

#insert
@POST_api.route("/insert", methods=['POST'])
class insert(Resource):
    def post():
        values = request.get_json()
        name = values['name']
        price = values['price']
        store = values['store']
        event = values['event']
        db_class = database.Database()
        sql = "INSERT INTO products(name, price, store, event) VALUES('%s', '%s', '%s', '%s')" % (name, price, store, event)
        db_class.execute(sql)
        db_class.commit()

        return jsonify(values)

#select store 매점별 검색 ex) CU, GS25
@GET_api.route("/select_store/<string:store>/<int:cnt>/<int:page>", methods=['GET'])
class select_store(Resource):
    def get(self, store, cnt, page):
        page = page - 1
        p = cnt * page
        db_class = database.Database()
        sql = "SELECT * FROM products WHERE store=('%s') limit %d offset %d" % (store, cnt, p)
        row = db_class.execute_all(sql)
        row = "" if not row else row

        return jsonify(row)

#select category 카테고리별 검색 ex) 바나나우유, 과자
@GET_api.route("/select_category/<string:category>/<int:cnt>/<int:page>", methods=['GET'])
class select_category(Resource):
    def get(self, category, cnt, page):
        page = page - 1
        p = cnt * page
        db_class = database.Database()
        sql = "SELECT * FROM products WHERE name LIKE ('%s') limit %d offset %d" % (category, cnt, p)
        row = db_class.execute_all(sql)
        row = "" if not row else row

        return jsonify(row)

#select event 이벤트 검색 ex) 1+1, 2+1
@GET_api.route("/select_event/<string:event>/<int:cnt>/<int:page>", methods=['GET'])
class select_event(Resource):
    def get(self, event, cnt, page):
        page = page - 1
        p = cnt * page
        db_class = database.Database()
        sql = "SELECT * FROM products WHERE event=('%s') limit %d offset %d" % (event, cnt, p)
        row = db_class.execute_all(sql)
        row = "" if not row else row

        return jsonify(row)

#select priceRange 가격 범위 검색 ex) 1000~1500
@GET_api.route("/select_priceRange/<int:minPrice>/<int:maxPrice>/<int:cnt>/<int:page>", methods=['GET'])
class select_priceRange(Resource):
    def get(self, minPrice, maxPrice, cnt, page):
        db_class = database.Database()
        page = page - 1
        p = cnt * page
        sql = "SELECT * FROM products WHERE price BETWEEN('%d') AND ('%d') limit %d offset %d" % (minPrice, maxPrice, cnt, p)
        row = db_class.execute_all(sql)
        row = "" if not row else row

        return jsonify(row)

#select priceRange 특정 가격 검색 ex) 1000
@GET_api.route("/select_price/<int:price>/<int:cnt>/<int:page>", methods=['GET'])
class select_price(Resource):
    def get(self, price, cnt, page):
        page = page - 1
        p = cnt * page
        db_class = database.Database()
        sql = "SELECT * FROM products WHERE price=('%d') limit %d offset %d" % (price, cnt, p)
        row = db_class.execute_all(sql)
        row = "" if not row else row

        return jsonify(row)