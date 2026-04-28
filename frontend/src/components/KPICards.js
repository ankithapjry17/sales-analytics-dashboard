import React, { useEffect, useState } from 'react';
import axios from 'axios';

function KPICards() {
  const [revenue, setRevenue] = useState(null);
  const [orders, setOrders] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/revenue')
      .then(res => setRevenue(res.data.total_revenue));

    axios.get('http://127.0.0.1:8000/orders')
      .then(res => setOrders(res.data.total_orders));
  }, []);

  const cardStyle = {
    background: '#4CAF50',
    color: 'white',
    padding: '20px',
    borderRadius: '10px',
    textAlign: 'center',
    width: '200px'
  };

  return (
    <div style={{ display: 'flex', gap: '20px', justifyContent: 'center', margin: '20px' }}>
      <div style={cardStyle}>
        <h3>Total Revenue</h3>
        <h2>${revenue ? revenue.toFixed(2) : 'Loading...'}</h2>
      </div>
      <div style={{ ...cardStyle, background: '#2196F3' }}>
        <h3>Total Orders</h3>
        <h2>{orders ? orders : 'Loading...'}</h2>
      </div>
    </div>
  );
}

export default KPICards;