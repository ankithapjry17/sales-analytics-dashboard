import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

function TopProducts() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/top-products')
      .then(res => setData(res.data));
  }, []);

  return (
    <div style={{ margin: '30px auto', maxWidth: '800px' }}>
      <h2 style={{ textAlign: 'center' }}>Top 5 Products by Revenue</h2>
      <ResponsiveContainer width="100%" height={350}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="product" tick={{ fontSize: 10 }} />
          <YAxis />
          <Tooltip />
          <Bar dataKey="revenue" fill="#4CAF50" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default TopProducts;