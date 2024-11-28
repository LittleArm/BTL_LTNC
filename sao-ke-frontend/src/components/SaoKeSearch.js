import React, { useState } from 'react';
import logo from '../assets/image 329 (1).png';
import axios from 'axios';

const SaoKeSearch = () => {
  const [searchParams, setSearchParams] = useState({
    min_credit: '',
    max_credit: '',
    min_debit: '',
    max_debit: '',
    detail: ''
  });

  const [results, setResults] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setSearchParams(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const queryParams = new URLSearchParams();
      
      Object.entries(searchParams).forEach(([key, value]) => {
        if (value !== '') {
          queryParams.append(key, value);
        }
      });

      const response = await axios.get(`http://localhost:5000/api/search?${queryParams}`);
      setResults(response.data);
    } catch (err) {
      setError(err.response?.data?.message || 'Có lỗi xảy ra');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {/* Header Mặt trận Tổ quốc Việt Nam */}
      <header className="bg-red-700 text-white py-4 shadow-lg">
        <div className="container mx-auto flex items-center justify-center">
          <img 
            src={logo} 
            alt="Logo Mặt trận Tổ quốc" 
            className="mr-4 rounded-full w-16 h-16"
          />
          <div className="text-center">
            <h1 className="text-3xl font-bold uppercase">
              Mặt Trận Tổ Quốc Việt Nam
            </h1>
            <p className="text-sm mt-1">
              Đoàn kết - Dân chủ - Hợp tác - Phát triển
            </p>
          </div>
        </div>
      </header>

      <div className="container mx-auto p-4">
        <div className="bg-gray-100 p-6 rounded-lg shadow-md">
          <h2 className="text-2xl font-bold mb-4 text-center text-red-700">
            Tra Cứu Sao Kê
          </h2>
          
          <form onSubmit={handleSearch} className="mb-4 grid grid-cols-2 gap-4">
            <div>
              <label className="block mb-2">Số tiền ghi có (Credit)</label>
              <div className="flex gap-2">
                <input 
                  type="number" 
                  name="min_credit" 
                  placeholder="Từ" 
                  value={searchParams.min_credit}
                  onChange={handleInputChange}
                  className="w-full p-2 border rounded"
                />
                <input 
                  type="number" 
                  name="max_credit" 
                  placeholder="Đến" 
                  value={searchParams.max_credit}
                  onChange={handleInputChange}
                  className="w-full p-2 border rounded"
                />
              </div>
            </div>

            <div>
              <label className="block mb-2">Số tiền ghi nợ (Debit)</label>
              <div className="flex gap-2">
                <input 
                  type="number" 
                  name="min_debit" 
                  placeholder="Từ" 
                  value={searchParams.min_debit}
                  onChange={handleInputChange}
                  className="w-full p-2 border rounded"
                />
                <input 
                  type="number" 
                  name="max_debit" 
                  placeholder="Đến" 
                  value={searchParams.max_debit}
                  onChange={handleInputChange}
                  className="w-full p-2 border rounded"
                />
              </div>
            </div>

            <div className="col-span-2">
              <label className="block mb-2">Chi tiết giao dịch (Nội dung & Tên)</label>
              <input 
                type="text" 
                name="detail" 
                placeholder="Nhập tên người gửi hoặc nội dung" 
                value={searchParams.detail}
                onChange={handleInputChange}
                className="w-full p-2 border rounded"
              />
            </div>

            <div className="col-span-2">
              <button 
                type="submit" 
                disabled={loading}
                className="w-full p-2 bg-red-600 text-white rounded hover:bg-red-700 disabled:bg-gray-400"
              >
                {loading ? 'Đang tìm kiếm...' : 'Tìm kiếm'}
              </button>
            </div>
          </form>

          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
              {error}
            </div>
          )}

          {results.length > 0 && (
            <div>
              <h2 className="text-xl font-semibold mb-2">Kết quả: {results.length} giao dịch</h2>
              <div className="overflow-x-auto">
                <table className="w-full border-collapse border">
                  <thead>
                    <tr className="bg-gray-200">
                      {Object.keys(results[0]).map(header => (
                        <th key={header} className="border p-2">{header}</th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {results.map((row, index) => (
                      <tr key={index} className="hover:bg-gray-100">
                        {Object.values(row).map((value, cellIndex) => (
                          <td key={cellIndex} className="border p-2">{value}</td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default SaoKeSearch;