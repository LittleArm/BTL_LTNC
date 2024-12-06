# be/services/service.py
import pandas as pd
import requests
from io import StringIO

class SaoKeService:
    def __init__(self, file_url="https://s.thuanle.me/chuyen_khoan.csv"):
        self.file_url = file_url
        self.data = self.load_data()

    def load_data(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(self.file_url, headers=headers)
        if response.status_code == 200:
            csv_data = StringIO(response.text)
            return pd.read_csv(csv_data)
        else:
            raise Exception(f"Lỗi khi tải dữ liệu từ {self.file_url}. Mã lỗi: {response.status_code}")

    def filter_data(self, min_credit=0, max_credit=float('inf'), min_debit=0, max_debit=float('inf'), detail=''):
        filtered_data = self.data
        if detail:
            filtered_data = filtered_data[filtered_data['detail'].str.contains(detail, case=False, na=False)]
        if min_credit or max_credit < float('inf'):
            filtered_data = filtered_data[(filtered_data['credit'] >= min_credit) & (filtered_data['credit'] <= max_credit)]
        if min_debit or max_debit < float('inf'):
            filtered_data = filtered_data[(filtered_data['debit'] >= min_debit) & (filtered_data['debit'] <= max_debit)]
        return filtered_data
