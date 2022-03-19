from flask import Flask, jsonify, render_template
from sqlite_db import live_ticker_db
import read_json

app = Flask(__name__)

@app.route('/get_values', methods = ['GET'])
def stuff():
    SYMBOLS = read_json.get_json_value(file='C:\\Users\\lauri\\Documents\\GitHub\\Projekt_Tradingbot\\parameter.json', parameter="ticker_list")
    db = live_ticker_db('technical_indicator_values_ft')
    result = []

    for table in db.get_all_tables():
        for symbol in SYMBOLS:
            result.append(db.get_table_entry(table, symbol))
    return jsonify(result=result)


@app.route('/')
def index():
    return render_template('home.html')

    
if __name__ == '__main__':
    app.run()