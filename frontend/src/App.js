import React from 'react';
import KPICards from './components/KPICards';
import TopProducts from './components/TopProducts';

function App() {
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1 style={{ textAlign: 'center' }}>Sales Analytics Dashboard</h1>
      <KPICards />
      <TopProducts />
    </div>
  );
}

export default App;