import React, { useEffect, useState } from 'react';
import * as echarts from 'echarts';
import './CompareMarketCap.css'; 
import { Link } from 'react-router-dom';

const CompareMarketCap = () => {
  // State to store the fetched data
  const [data, setData] = useState([]);
  
  // State to track the selected comparison type
  const [selectedComparison, setSelectedComparison] = useState('previous');
  
  // State to track whether data has been fetched
  const [dataFetched, setDataFetched] = useState(false);

  // Function to fetch data from the API
  const fetchData = () => {
    // Define the API URL
    const apiUrl = 'http://127.0.0.1:5000/sectors/periodic_marketcap_data';

    // Make the API request
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => {
        // Update the component's state with the fetched data
        setData(data);
        setDataFetched(true); // Set dataFetched to true
      })
      .catch((error) => {
        console.error('Error fetching data from the API:', error);
      });
  };

  // Fetch data from the API when the component mounts
  useEffect(() => {
    // Check if data has already been fetched
    if (!dataFetched) {
      fetchData(); // Fetch data only if it hasn't been fetched yet
    }
  }, [dataFetched]);


  // Function to format market capitalization values
  function formatMarketCap(value) {
    if (value >= 1e12) {
      return '$'+ (value / 1e12).toFixed(2) + 'T';
    } else if (value >= 1e9) {
      return '$'+ (value / 1e12).toFixed(2) + 'T';
    } else {
      return '$'+ value.toFixed(2);
    }
  }
  function sortDataAscending(data) {
    return data.sort((a, b) => a.current_marketcap - b.current_marketcap);
  }

  // Function to update the chart based on the selected comparison type
  function updateChart(comparisonType, chart) {
    // Create arrays to store yAxisData, minValues, diffValues, and colors
    sortDataAscending(data);
    const yAxisData = [];
    const minValues = [];
    const diffValues = [];
    const colors = [];
    const values = [];

    // Loop through the data to calculate values based on the selected comparison type
    data.forEach((item) => {
      yAxisData.push(item.sector); // Add sector name to yAxisData

      // Calculate the appropriate value based on the comparison type
      let value;
      if (comparisonType === 'previous') {
        value = item.previous_marketcap;
      } else if (comparisonType === 'oneweek') {
        value = item.oneweek_back;
      } else if (comparisonType === 'onemonth') {
        value = item.onemonth_back;
      } else if (comparisonType === 'threemonths') {
        value = item.threemonths_back;
      } else if (comparisonType === 'sixmonths') {
        value = item.sixmonths_back;
      } else if (comparisonType === 'oneyear') {
        value = item.oneyear_back;
      }
      values.push(value);
      minValues.push(Math.min(item.current_marketcap, value));

      // Calculate the difference between current and the selected value
      const diff = item.current_marketcap - value;
      // Add the absolute difference to diffValues
      diffValues.push(Math.abs(diff));

      // Determine the color based on the direction of change
      const color = diff >= 0 ? 'green' : 'red';
      // Add color to colors
      colors.push(color);
    });

    // Define the chart options
    const option = {
      tooltip: {
        trigger: 'axis',
        formatter: function (params) {
          const dataIndex = params[0].dataIndex;
          const sector = params[0].name;
          const diffVal = formatMarketCap(diffValues[dataIndex]);
          const val = formatMarketCap(values[dataIndex]);
          const currentMarketCap = formatMarketCap(data[dataIndex].current_marketcap);
          const percentage = ((diffValues[dataIndex] / values[dataIndex]) * 100).toFixed(2);
          const changeText =
            colors[dataIndex] === 'green' ? `+${percentage}%` :
            colors[dataIndex] === 'red' ? `-${percentage}%` : 'No change';
          return `
              <strong>${sector}</strong><br>
              Current Market Cap: ${currentMarketCap}<br>
              Previous Market Cap: ${val}<br>
              Difference: ${diffVal}<br>
              Percentage Change: ${changeText}
          `;
        },
      },
      yAxis: {
        type: 'category',
        data: yAxisData,
        axisLabel: {
          show: false,
        },
      },
      xAxis: {
        type: 'value',
        axisLabel: {
          formatter: function (value) {
            return formatMarketCap(value);
          },
        },
      },
      series: [
        {
          name: 'Remaining bar',
          type: 'bar',
          stack: 'sector',
          data: minValues,
          itemStyle: {
            color: '#00CED1',
          },
          label: {
            show: true,
            fontSize: 9.5,
            fontWeight: 'bold',
            formatter: function (params) {
              const sector = params.name;
              const currentMarketCap = data[params.dataIndex].current_marketcap;
              const current = formatMarketCap(currentMarketCap);
              const shortForms = {
                'Utilities': 'Utils',
                'Real Estate': 'RE',
                'Materials': 'Matls',
              };
              const shortForm = shortForms[sector] || sector;
              return `${shortForm}\n${current}`;
            },
          },
        },
        {
          name: 'Difference',
          type: 'bar',
          stack: 'sector',
          data: diffValues,
          itemStyle: {
            color: (params) => colors[params.dataIndex],
          },
          label: {
            show: false, // Hide the label for the Difference series
          },
        },
      ],
    };

    // Set the chart options
    chart.setOption(option);
  }

  // Function to populate the table with data
  function populateTable() {
    const tableBody = document.getElementById('data-table');
    tableBody.innerHTML = ''; // Clear existing rows

    // Loop through the data to create rows for the table
    data.forEach((item) => {
      const row = document.createElement('tr');
      row.innerHTML = `
          <td>${item.sector}</td>
          <td>${formatMarketCap(item.current_marketcap)}</td>
          <td>${formatMarketCap(item.previous_marketcap)}</td>
          <td>${formatMarketCap(item.oneweek_back)}</td>
          <td>${formatMarketCap(item.onemonth_back)}</td>
          <td>${formatMarketCap(item.threemonths_back)}</td>
          <td>${formatMarketCap(item.sixmonths_back)}</td>
          <td>${formatMarketCap(item.oneyear_back)}</td>
      `;
      tableBody.appendChild(row);
    });
  }

  // Function to handle button clicks and update the selected comparison type
  function handleButtonClick(comparisonType) {
    setSelectedComparison(comparisonType);
  }
  useEffect(() => {
    if (dataFetched) {
      const chart = echarts.init(document.getElementById('chart'));
      updateChart(selectedComparison, chart);
      populateTable();
    }
  }, [dataFetched, selectedComparison]);

  return (
      <div>
        <Link to="/" className="home-link">Home</Link>
      <div className="container">
      <div className="box chart-container">
        <div>
          <button
            onClick={() => handleButtonClick('previous')}
            className={selectedComparison === 'previous' ? 'selected-button' : ''}
          >
            1D
          </button>
          <button
            onClick={() => handleButtonClick('oneweek')}
            className={selectedComparison === 'oneweek' ? 'selected-button' : ''}
          >
            1W
          </button>
          <button
            onClick={() => handleButtonClick('onemonth')}
            className={selectedComparison === 'onemonth' ? 'selected-button' : ''}
          >
            1M
          </button>
          <button
            onClick={() => handleButtonClick('threemonths')}
            className={selectedComparison === 'threemonths' ? 'selected-button' : ''}
          >
            3M
          </button>
          <button
            onClick={() => handleButtonClick('sixmonths')}
            className={selectedComparison === 'sixmonths' ? 'selected-button' : ''}
          >
            6M
          </button>
          <button
            onClick={() => handleButtonClick('oneyear')}
            className={selectedComparison === 'oneyear' ? 'selected-button' : ''}
          >
            1Y
          </button>
        </div>
        <div id="chart" style={{ height: '650px' }}></div>
      </div>
      <div class="box table-container">
        <table>
          <thead>
            <tr>
              <th>Sector</th>
              <th>Current</th>
              <th>1D</th>
              <th>1W</th>
              <th>1M</th>
              <th>3M</th>
              <th>6M</th>
              <th>1YR</th>
            </tr>
          </thead>
          <tbody id="data-table">
          </tbody>
        </table>
      </div>
      </div>
      </div>
  );
};

export default CompareMarketCap;
