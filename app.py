from flask import Flask, jsonify, request

app = Flask(__name__)

# Data roti contoh
breads = [
    {"id": 1, "name": "Sourdough", "price": 30000, "stock": 20},
    {"id": 2, "name": "Croissant", "price": 20000, "stock": 15},
    {"id": 3, "name": "Baguette", "price": 25000, "stock": 10}
]

# Endpoint: Mendapatkan daftar semua roti
@app.route('/api/breads', methods=['GET'])
def get_breads():
    return jsonify(breads), 200

# Endpoint: Mendapatkan detail roti berdasarkan ID
@app.route('/api/breads/<int:bread_id>', methods=['GET'])
def get_bread(bread_id):
    bread = next((bread for bread in breads if bread["id"] == bread_id), None)
    if bread is None:
        return jsonify({"error": "Bread not found"}), 404
    return jsonify(bread), 200

# Endpoint: Menambahkan roti baru
@app.route('/api/breads', methods=['POST'])
def add_bread():
    new_bread = request.get_json()
    new_bread["id"] = len(breads) + 1  # ID otomatis
    breads.append(new_bread)
    return jsonify(new_bread), 201

# Endpoint: Memperbarui stok roti berdasarkan ID
@app.route('/api/breads/<int:bread_id>', methods=['PUT'])
def update_bread(bread_id):
    bread = next((bread for bread in breads if bread["id"] == bread_id), None)
    if bread is None:
        return jsonify({"error": "Bread not found"}), 404
    
    data = request.get_json()
    bread.update(data)
    return jsonify(bread), 200

# Endpoint: Menghapus roti berdasarkan ID
@app.route('/api/breads/<int:bread_id>', methods=['DELETE'])
def delete_bread(bread_id):
    bread = next((bread for bread in breads if bread["id"] == bread_id), None)
    if bread is None:
        return jsonify({"error": "Bread not found"}), 404
    
    breads.remove(bread)
    return jsonify({"message": "Bread deleted"}), 200

# Menjalankan server
if __name__ == '__main__':
    app.run(debug=True)
