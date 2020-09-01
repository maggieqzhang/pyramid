import React from 'react';
import './styles.css';
import HomeNav from './../../components/nav/HomeNav';

const Location = () => {
  
  return (
      <React.Fragment>
        <HomeNav/>
        <div className='location-wrapper'>
            <h1>Find a Pickup Point</h1>
            <h2>enter an address, zip code, or neighborhood</h2>
            <input placeholder='Search'></input>
            <div className='location-option'>
                <p className='location-number'>1</p>
                <p className='location-result-name'>Lake Pinnacle Park</p>
                <p className='distance'>2.4 miles away</p>
            </div>
            <div className='location-option'>
                <p className='location-number'>2</p>
                <p className='location-result-name'>Trail Hills Park</p>
                <p className='distance'>4.2 miles away</p>
            </div>
        </div>
      </React.Fragment>
  );
}

export default Location;