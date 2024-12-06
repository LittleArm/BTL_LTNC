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

<<<<<<< HEAD
    # Áp dụng các bộ lọc nếu có tham số tương ứng
    if detail:
        results = sao_ke_service.search_by_detail(detail)
    if min_credit or max_credit < float('inf'):
        results = sao_ke_service.search_by_credit(min_credit, max_credit)
    if min_debit or max_debit < float('inf'):
        results = sao_ke_service.search_by_debit(min_debit, max_debit)

    if results.empty:
        return jsonify({"message": "Không tìm thấy kết quả nào."}), 404
    else:
        return jsonify(results.to_dict(orient="records"))

# @sao_ke_blueprint.route('/print_data', methods=['GET'])
# def print_data():
#     # In toàn bộ dữ liệu
#     data = sao_ke_service.data
#     return jsonify(data.to_dict(orient="records"))
=======
        # Kiểm tra kết quả
        if results.empty:
            return jsonify({"message": "Không tìm thấy kết quả nào."}), 404
        else:
            return jsonify(results.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"error": f"Lỗi trong quá trình xử lý: {str(e)}"}), 500
>>>>>>> 013c0e91cbb127e8ff3b30b6fc8f7392ecb00f4f
