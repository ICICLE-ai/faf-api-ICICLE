import React from 'react';
import '../styles/App.css';

const Home = () => {
  return (
    <div className="home-container">
      <section className="section-box">
        <div>
        <h2>About</h2>
        <h5 style={{ color: 'red' }}> (Need to re-write this section based on the API's)</h5>
        <p>The Freight Analysis Framework (FAF) creates a comprehensive picture of freight movement among states and major metropolitan areas by all modes of transportation. This application </p>
      </div>
        </section>

      <section className="section-box">
        <h2>Data</h2>
        <p>FAF provides a regional database of tonnage and value by origin-destination pair, commodity type, and mode. It also includes a state database with similar metrics.</p>
      </section>
      
      <section className="section-box">
        <h2>Types of Data</h2>
        <p>The DTT allows users to select specific categories of data to create customized subsets of FAF5 data. The three types of FAF5 data are:</p>
        <ul>
          <li><strong>Total Flows:</strong> Includes both domestic and foreign shipments. Mode of transportation is used within and between domestic regions or states.</li>
          <li><strong>Domestic Flows:</strong> Only includes shipments associated with domestic freight. Domestic movements of foreign trade flows are not included.</li>
          <li><strong>Foreign Trade Flows:</strong> Includes import and export flows with specific geographies and modes of transportation:
            <ul>
              <li><strong>Import Flows:</strong> Data from foreign origins to domestic destinations, with both foreign and domestic modes of transportation.</li>
              <li><strong>Export Flows:</strong> Data from domestic origins to foreign destinations, with both domestic and foreign modes of transportation.</li>
            </ul>
          </li>
        </ul>
      </section>
    </div>
  );
};

export default Home;
