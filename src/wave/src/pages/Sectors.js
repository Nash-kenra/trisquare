import React, { useState, useEffect } from 'react';
import './Sectors.css';

import SectorImage from './Sector.png';
import { Link } from 'react-router-dom';
import { pangea } from '../context/apiContext.js';


function Sectors() {
  const [sectors, setSectors] = useState([]);
  const [selectedSector, setSelectedSector] = useState(null);
  const [subsectors, setSubsectors] = useState([]);
  const [sectorMarketCap, setSectorMarketCap] = useState(null);


  useEffect(() => {
    pangea("/sectors", setSectors);
  }, []);

  const fetchSubsectors = (sector) => {
    pangea(`/sectors/subsectors?sector=${sector}`, setSubsectors);
  };

  const fetchSectorMarketCap = (sector) => {
    pangea(`/sectors/${sector}/marketcap`, setSectorMarketCap);
  };

  const handleSectorClick = (sector) => {
    setSelectedSector(sector);
    fetchSubsectors(sector);
    fetchSectorMarketCap(sector);
  };

  return (
    <div>
      <Link to="/" className="home-link">Home</Link>
      <h1>SP500 - Sectors</h1>
      <div className="sectors-container">
        <div className="sectors-text">
          <div>
            <div className="sector-buttons">
              {sectors.map((sector) => (
                <button
                  key={sector.sector}
                  onClick={() => handleSectorClick(sector.sector)}
                  className={selectedSector === sector.sector ? 'selected-button' : ''}
                >
                  {sector.sector}
                </button>
              ))}
            </div>
            {selectedSector && (
              <div>
                <h2>Subsectors for {selectedSector}</h2>
                <ul>
                  {subsectors.map((subsector) => (
                    <li key={subsector.subSector}>{subsector.subSector}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
        <div className="sector-image-container">
          <img src={SectorImage} />
        </div>
      </div>
      {selectedSector && (
        <div>
          <h2>Market Capitalization for {selectedSector}</h2>
          <p>Market Cap: {sectorMarketCap && sectorMarketCap.total_marketcap}</p>
        </div>
      )}
    </div>
  );
}

export default Sectors;
