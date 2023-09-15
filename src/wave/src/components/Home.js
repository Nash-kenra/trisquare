import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css'; // Import your CSS file

function Home() {
  return (
    <div className="home-container">
      <h1 className="home-title">TriSquare</h1>
      <div className="home-links">
        <Link to="/sectors" className="home-link">Sectors Subsectors</Link>
        <Link to="/sectors-marketcap" className="home-link">Sectors Market Cap</Link>
      </div>
    </div>
  );
}

export default Home;
