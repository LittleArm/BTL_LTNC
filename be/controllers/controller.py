# be/controllers/controller.py
from flask import Blueprint, jsonify, request
from services.service import SaoKeService
from flask_cors import CORS

sao_ke_blueprint = Blueprint('sao_ke', __name__)
CORS(sao_ke_blueprint, origins=["http://localhost:8000", "http://localhost:3000"])  # Thêm localhost:3000 cho React
sao_ke_service = SaoKeService()

@sao_ke_blueprint.route('/search', methods=['GET'])
def search():
    try:
        # Lấy các tham số từ yêu cầu
        min_credit = float(request.args.get('min_credit', 0))
        max_credit = float(request.args.get('max_credit', float('inf')))
        min_debit = float(request.args.get('min_debit', 0))
        max_debit = float(request.args.get('max_debit', float('inf')))
        detail = request.args.get('detail', '')

        # Áp dụng bộ lọc
        results = sao_ke_service.filter_data(min_credit, max_credit, min_debit, max_debit, detail)

        # Kiểm tra kết quả
        if results.empty:
            return jsonify({"message": "Không tìm thấy kết quả nào."}), 404
        else:
            return jsonify(results.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"error": f"Lỗi trong quá trình xử lý: {str(e)}"}), 500
