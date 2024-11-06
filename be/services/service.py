# be/services/service.py
import pandas as pd
import requests
from io import StringIO

class SaoKeService:
    def __init__(self, file_url="https://s.thuanle.me/chuyen_khoan.csv"):
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(file_url, headers=headers)
        
        if response.status_code == 200:
            csv_data = StringIO(response.text)
            self.data = pd.read_csv(csv_data)
        else:
            raise Exception(f"Lỗi khi tải dữ liệu. Mã lỗi: {response.status_code}")
    
    def search_by_credit(self, min_credit, max_credit):
        return self.data[(self.data['credit'] >= min_credit) & (self.data['credit'] <= max_credit)]

    def search_by_debit(self, min_debit, max_debit):
        return self.data[(self.data['debit'] >= min_debit) & (self.data['debit'] <= max_debit)]

    def search_by_detail(self, detail_content):
        return self.data[self.data['detail'].str.contains(detail_content, case=False, na=False)]
