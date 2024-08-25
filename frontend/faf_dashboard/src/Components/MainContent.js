// src/components/MainContent.js
import React from 'react';
import {Routes, Route} from "react-router-dom";
import Home from '../pages/Home';
import Mode from '../pages/Mode';

const MainContent = () => {
  return (
    <main className="main-content">
      <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Mode" element={<Mode />} />
      </Routes>
    </main>
  );
};

export default MainContent;
