import React from 'react';
import { BrowserRouter as Router,Routes, Route } from 'react-router-dom';
import Header from './Components/Header';
import Sidebar from './Components/Sidebar';
import MainContent from './Components/MainContent';
import Home from './pages/Home';
import Domestic from './pages/Domestic';
import Export from './pages/Export';
import Import from './pages/Import';


import './styles/App.css';

const App = () => {
  return (
    <Router>
      <div className="app">
        <Header />
        <Sidebar />
        </div>
      <div className='main-content'>
      <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Import" element={<Import />} />
            <Route path="/Export" element={<Export />} />
            <Route path="/Domestic" element={<Domestic />} />
      </Routes>
      </div>      
    </Router>
  );
};

export default App;
