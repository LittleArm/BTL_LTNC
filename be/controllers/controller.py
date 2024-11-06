# be/controllers/controller.py
from flask import Blueprint, jsonify, request
from services.service import SaoKeService

sao_ke_blueprint = Blueprint('sao_ke', __name__)
sao_ke_service = SaoKeService()

@sao_ke_blueprint.route('/search', methods=['GET'])
def search():
    # Lấy các tham số từ yêu cầu
    min_credit = float(request.args.get('min_credit', 0))
    max_credit = float(request.args.get('max_credit', float('inf')))
    min_debit = float(request.args.get('min_debit', 0))
    max_debit = float(request.args.get('max_debit', float('inf')))
    detail = request.args.get('detail', '')

    # Khởi tạo kết quả là toàn bộ dữ liệu
    results = sao_ke_service.data

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
