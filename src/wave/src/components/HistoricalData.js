import React, { useState, useEffect } from 'react';

function HistoricalData() {
  const [sectorData, setSectorData] = useState([]);
  const [selectedSector, setSelectedSector] = useState('');

  useEffect(() => {
    // Fetch the dummy data from the public directory
    fetch('/dummy_data.json') // Assuming the JSON file is in the public directory
      .then((response) => response.json())
      .then((data) => {
        // Set the sector data from the JSON
        setSectorData(data.historicalSectors);
      })
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  const handleSectorClick = (sector) => {
    // Set the selected sector
    setSelectedSector(sector);
  };

  // Render the component with sector buttons and data
  return (
    <div>
      <h1>Historical Data</h1>
      <div className="sector-buttons">
        {sectorData.map((sectorInfo) => (
          <button
            key={sectorInfo.sector}
            onClick={() => handleSectorClick(sectorInfo.sector)}
          >
            {sectorInfo.sector}
          </button>
        ))}
      </div>
      {selectedSector && (
        <div>
          <h2>{selectedSector}</h2>
          <ul>
            {/* Render historical data for the selected sector */}
            {sectorData
              .find((sectorInfo) => sectorInfo.sector === selectedSector)
              .historical.map((entry) => (
                <li key={entry.date}>
                  Date: {entry.date}, Volume: {entry.volume}, Market Cap: ${entry.marketcap}
                </li>
              ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default HistoricalData;
