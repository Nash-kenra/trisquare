import React, { useState, useEffect } from 'react';
import './Sectors.css';
import SectorImage from './Sector.png';

function Sectors() {
  const [sectors, setSectors] = useState([]);
  const [selectedSector, setSelectedSector] = useState(null);
  const [subsectors, setSubsectors] = useState([]);
  const [sectorMarketCap, setSectorMarketCap] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/sectors')
      .then((response) => response.json())
      .then((data) => setSectors(data))
      .catch((error) => console.error('Error fetching sectors:', error));
  }, []);

  const fetchSubsectors = (sector) => {
    fetch(`http://127.0.0.1:5000/sectors/subsectors?sector=${sector}`)
      .then((response) => response.json())
      .then((data) => setSubsectors(data))
      .catch((error) => console.error('Error fetching subsectors:', error));
  };

  const fetchSectorMarketCap = (sector) => {
    fetch(`http://127.0.0.1:5000/sectors/${sector}/marketcap`)
      .then((response) => response.json())
      .then((data) => setSectorMarketCap(data))
      .catch((error) => console.error('Error fetching sector market cap:', error));
  };

  const handleSectorClick = (sector) => {
    setSelectedSector(sector);
    fetchSubsectors(sector);
    fetchSectorMarketCap(sector);
  };

  return (
    <div>
      <h1>SP500 - Sectors</h1>
      <div className="sectors-container">
        <div className="sectors-text">
          <div>
            <div className="sector-buttons">
              {sectors.map((sector) => (
                <button
                  key={sector.sector}
                  onClick={() => handleSectorClick(sector.sector)}
                  className={selectedSector === sector.sector ? 'active' : ''}
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
