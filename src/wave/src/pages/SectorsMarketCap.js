import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { pangea } from '../context/apiContext.js';

function SectorsMarketCap() {
  const [sectorMarketCaps, setSectorMarketCaps] = useState([]);

  useEffect(() => {
    pangea("/sectors/marketcap", transformData);
  }, []);

  const transformData = (data) => {
    // Transform the API response into an array of objects with formatted market caps
    const transformedData = Object.entries(data).map(([sector, marketcap]) => ({
      sector,
      marketcap,
      formattedMarketCap: formatMarketCap(marketcap),
    }));
    setSectorMarketCaps(transformedData);
  }

  // Function to format market cap values
  const formatMarketCap = (marketcap) => {
    const numericValue = parseFloat(marketcap.replace(/[^0-9.]/g, ''));
    if (numericValue >= 10 ** 12) {
      return `${marketcap} (${(numericValue / 10 ** 12).toFixed(1)} Trillion)`;
    } else if (numericValue >= 10 ** 9) {
      return `${marketcap} (${(numericValue / 10 ** 9).toFixed(1)} Billion)`;
    } else {
      return marketcap;
    }
  };

  return (
    <div>
      <Link to="/" className="home-link">Home</Link>
      <h1>Sectors Market Cap</h1>
      <ul>
        {sectorMarketCaps.map((sector) => (
          <li key={sector.sector}>
            {sector.sector} - {sector.formattedMarketCap}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SectorsMarketCap;
