from flask import Flask, jsonify
from extract import extract_data
from transform import transform_data
from load import load_data
from export import export_to_csv

app = Flask(__name__)

@app.route('/api/extract', methods=['GET'])
def extract():
    data = extract_data()
    return jsonify(data)

@app.route('/api/transform', methods=['GET'])
def transform():
    data = extract_data()
    transformed_data = transform_data(data)
    return jsonify(transformed_data)

@app.route('/api/load', methods=['POST'])
def load():
    data = extract_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)
    return jsonify({"message": "Data loaded successfully into PostgreSQL"})

@app.route('/api/export', methods=['GET'])
def export():
    export_to_csv()
    return jsonify({"message": "CSV file generated successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
