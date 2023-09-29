import React from 'react';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Home from './components/Home';
import Sectors from './components/Sectors';
import SectorsMarketCap from './components/SectorsMarketCap';
import HistoricalData from './components/HistoricalData';
import CompareMarketCap from './components/CompareMarketCap';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/sectors" element={<Sectors />} />
        <Route path="/sectors-marketcap" element={<SectorsMarketCap />} />
        <Route path="/historical-marketcap" element={<HistoricalData />} />
        <Route path="/compare-marketcap" element={<CompareMarketCap />} />
      </Routes>
    </Router>
  );
}


export default App;
