import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/App.css';

const Sidebar = () => {
  return (
    <nav className="sidebar">
      
      <Link className="sidebar-link" to="/">Home</Link>
      <Link className="sidebar-link" to="/Domestic">Domestic</Link>
      <Link className="sidebar-link" to="/Import">Import</Link>
      <Link className="sidebar-link" to="/Export">Export</Link>
    </nav>
  );
};

export default Sidebar;
