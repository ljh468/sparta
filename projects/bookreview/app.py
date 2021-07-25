from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    title_give = request.form['title_give']
    author_give = request.form['author_give']
    review_give = request.form['review_give']
    print(title_give)
    print(author_give)
    print(review_give)

    doc = {'title': title_give,
           'author': author_give,
           'review': review_give
    }

    db.bookreview.insert_one(doc)
    return jsonify({'msg': '저장완료료!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.bookreview.find({}, {'_id': False}))

    return jsonify({'all_reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)