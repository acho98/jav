from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo
client = MongoClient('localhost', 27017)  # port number 27017
db = client.shop                          # create shop db

## HTML Link
@app.route('/')
def home():
    return render_template('myshop.html')

## API 
@app.route('/order', methods=['POST'])
def write_order():
    order_name = request.form['order_name']
    order_count = request.form['order_count']
    order_address = request.form['order_address']
    order_phone = request.form['order_phone']
	# 2. insert to db 
    order = {
        'name' : order_name, 
        'count' : order_count,
        'address' : order_address,
        'phone' : order_phone
    }
    db.order.insert_one(order)
	# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 입력되었습니다.'})
	


@app.route('/order', methods=['GET'])
def read_order():
    # 1. 모든 orders 를 가져온 후 list로 변환합니다.
    orders = list(db.order.find({},{'_id':0}))
    print(orders)
	# 2. 성공 메시지와 함께 주문을 보냅니다.
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)