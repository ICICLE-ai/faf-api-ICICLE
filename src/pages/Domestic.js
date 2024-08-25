import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/Domestic.css';
import axios from 'axios';

const Domestic = () => {
  const [selectedCommodity, setSelectedCommodity] = useState('');
  const [selectedOrigin, setSelectedOrigin] = useState('');
  const [selectedDestination, setSelectedDestination] = useState('');
  const [selectedTimeframe, setSelectedTimeframe] = useState('');
  const [dataEndpoint1, setDataEndpoint1] = useState(null);
  const [dataEndpoint2, setDataEndpoint2] = useState(null);
  const [blobUrl, setBlobUrl] = useState(null);
  const [error, setError] = useState(null);

  // Fetch data for both endpoints on page load - Useful for fetching data to populate dropdown - State, Commodity, Origin, Destinaiton, etc
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Need to replace with actual endpoints
        //      try {
          //       // Constructing request payload
          //       const payload = {
          //         table,
          //         timeframe
          //       };
          
          //       // Making API request
          //       const response = await axios.post('http://127.0.0.1:8000/api/schema/swagger-ui/#/get_table_data/', payload, {
          //         responseType: 'blob' 
          //       });
          
          //       // Create a blob from the CSV data
          //       const blob = new Blob([response.data], { type: 'text/csv' });
          //       const url = URL.createObjectURL(blob);
          //       setCsvUrl(url);
          
          //     } catch (err) {
          //       setError('An error occurred while fetching data');
          //     }
        const response1 = await fetch('api/endpoint1', {
          method: 'GET',
          headers: { 'Content-Type': 'application/json' },
        });
        const data1 = await response1.json();
        setDataEndpoint1(data1);
      } catch (error) {
        console.error('Error fetching initial data:', error);
      }
    };

    fetchData();
  }, []);

  // Handle form submission for Endpoint 1
  const handleSubmitEndpoint1 = async () => {
    try {
      // Constructing request payload
      const payload = {
        commodity: selectedCommodity,
        origin: selectedOrigin,
        destination: selectedDestination,
        timeframe: selectedTimeframe
      };
  
      // Making API request
      const response = await axios.post('http://127.0.0.1:8000/api/schema/swagger-ui/#/get_table_data/', payload, {
        headers: { 'Content-Type': 'application/json' },
        responseType: 'blob' 
      });
  
      // Create a blob from the response data
      const blob = new Blob([response.data], { type: response.headers['content-type'] });
      const url = URL.createObjectURL(blob);
  
      setBlobUrl(url);
    } catch (error) {
      console.error('Error fetching data for Endpoint 1:', error);
      setError('An error occurred while fetching data'); 
    }
  };

  // Handle form submission for Endpoint 2
  const handleSubmitEndpoint2 = async () => {
    try {
      const response = await fetch('api/endpoint2', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          commodity: selectedCommodity,
          origin: selectedOrigin,
          destination: selectedDestination,
          timeframe: selectedTimeframe
        })
      });
      const data = await response.json();
      setDataEndpoint2(data);
    } catch (error) {
      console.error('Error fetching data for Endpoint 2:', error);
    }
  };

  return (
    <div className="domestic container">

      <div className="endpoints">
        <div className="endpoint-section mb-4 p-3 border rounded">
          <h2>Get Table Data</h2>
          <p>This endpoint queries the FAF database and retrieves one of six fully populated tables: faf0, faf1, faf2, faf3, state0, state1, state2, or state3 based on the timeframe given. Subsequently, the server generates a query to join these smaller tables with the main data tables and processes this query. The resulting data is stored in a Pandas DataFrame, converted to a CSV file, and provided to the user as a downloadable file. The file is named according to the selected table. If the user inputs incorrect information, an error message is returned detailing the issue.
          </p>
          <button
              className="btn btn-custom btn-primary mt-2"
              onClick={handleSubmitEndpoint1}
            >
              Get Data
            </button>
        </div>

        <div className="endpoint-section mb-4 p-3 border rounded">
          <h2>Point to Point</h2>
          <p>This endpoint takes in a specific commodity, or writing "all" gives all the commodities traded between two areas. This endpoint works for the FAF and state databases and will return the value and quantity per ton of the resource traded between the origin and destination based on year or timeframe if given two years. This endpoint also returns the method of transportation, and if either the origin or destination is foreign, it returns the foreign transit and any other states the commodity moved to before the final destination.</p>
          <div className="endpoint-dropdowns">
            <div className="form-group">
              <label htmlFor="commoditySelect2">Commodity:</label>
              <select
                id="commoditySelect2"
                className="form-control"
                value={selectedCommodity}
                onChange={(e) => setSelectedCommodity(e.target.value)}
              >
                {/* Need to fetch these values dynamically by making API call to retrieve list of commodities, origin, destination states*/}
                <option value="">Select Commodity</option>
                <option value="commodity1">Pharmaceuticals</option>
                <option value="commodity2">Animal Feed</option>
                <option value="commodity3">Coal</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="originSelect2">Origin:</label>
              <select
                id="originSelect2"
                className="form-control"
                value={selectedOrigin}
                onChange={(e) => setSelectedOrigin(e.target.value)}
              >
                <option value="">Select Origin</option>
                <option value="origin1">CA</option>
                <option value="origin2">IN</option>
                <option value="origin2">IL</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="destinationSelect2">Destination:</label>
              <select
                id="destinationSelect2"
                className="form-control"
                value={selectedDestination}
                onChange={(e) => setSelectedDestination(e.target.value)}
              >
                <option value="">Select Destination</option>
                <option value="destination1">CA</option>
                <option value="destination2">IN</option>
                <option value="destination2">IL</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="timeframeSelect2">Timeframe:</label>
              <select
                id="timeframeSelect2"
                className="form-control"
                value={selectedTimeframe}
                onChange={(e) => setSelectedTimeframe(e.target.value)}
              >
                {/* Need to modify from - to */}
                <option value="">Select Timeframe</option>
                <option value="timeframe1">2022</option>
                <option value="timeframe2">2024</option>
              </select>
            </div>
            <button
              className="btn btn-custom btn-primary mt-2"
              onClick={handleSubmitEndpoint1}
            >
              Get Data
            </button>
          </div>
        </div>

        <div className="endpoint-section mb-4 p-3 border rounded">
          <h2>Domestic Imports</h2>
          <p>This endpoint takes in a region or state with a year or year frame and returns all exported commodities from that area. This only applies to domestic-based trade. The endpoint returns the commodity type, the transportation type, the area the commodity was sent to, and the year's ton and value.</p>
          <div className="endpoint-dropdowns">
            <div className="form-group">
              <label htmlFor="commoditySelect2">Commodity:</label>
              <select
                id="commoditySelect2"
                className="form-control"
                value={selectedCommodity}
                onChange={(e) => setSelectedCommodity(e.target.value)}
              >
                <option value="">Select Commodity</option>
                <option value="commodity1">Pharmaceuticals</option>
                <option value="commodity2">Animal Feed</option>
                <option value="commodity3">Coal</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="originSelect2">Origin:</label>
              <select
                id="originSelect2"
                className="form-control"
                value={selectedOrigin}
                onChange={(e) => setSelectedOrigin(e.target.value)}
              >
                <option value="">Select Origin</option>
                <option value="origin1">CA</option>
                <option value="origin2">IN</option>
                <option value="origin2">IL</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="destinationSelect2">Destination:</label>
              <select
                id="destinationSelect2"
                className="form-control"
                value={selectedDestination}
                onChange={(e) => setSelectedDestination(e.target.value)}
              >
                <option value="">Select Destination</option>
                <option value="destination1">CA</option>
                <option value="destination2">IN</option>
                <option value="destination2">IL</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="timeframeSelect2">Timeframe:</label>
              <select
                id="timeframeSelect2"
                className="form-control"
                value={selectedTimeframe}
                onChange={(e) => setSelectedTimeframe(e.target.value)}
              >
                <option value="">Select Timeframe</option>
                <option value="timeframe1">2022</option>
                <option value="timeframe2">2024</option>
              </select>
            </div>
            <button
              className="btn btn-custom btn-primary mt-2"
              onClick={handleSubmitEndpoint2}
            >
              Get Data
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Domestic;
