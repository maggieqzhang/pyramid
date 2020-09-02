import React from 'react';
import './styles.css';
import location from './../../assets/place.png';
import avocado from './../../assets/avocado.png';
import { Link } from 'react-router-dom';

const Location = () => {
  
  return (
    <div className='location-wrapper'>
        <h1>Find a Pickup Point</h1>
        <h2>enter an address, zip code, or neighborhood</h2>
        <img id='avocado' src={avocado} alt='avocado'/>
        <div className='search-field'>
          <img src={location} alt='location'/>
          <input placeholder='Search'></input>
        </div>
        <Link to='/pick-time'>
          <div className='location-option'>
              <p className='location-number'>1</p>
              <p className='location-result-name'>Harmony Trails Park</p>
              <p className='distance'>2.4 miles away</p>
          </div>
        </Link>
        <div className='location-option'>
            <p className='location-number'>2</p>
            <p className='location-result-name'>Trail Hills Park</p>
            <p className='distance'>4.2 miles away</p>
        </div>
        <div className='location-option'>
            <p className='location-number'>3</p>
            <p className='location-result-name'>Westbury Road Park</p>
            <p className='distance'>5.6 miles away</p>
        </div>
        <div className='location-option'>
            <p className='location-number'>4</p>
            <p className='location-result-name'>School St. Mall</p>
            <p className='distance'>6.3 miles away</p>
        </div>
        <div className='location-option'>
            <p className='location-number'>5</p>
            <p className='location-result-name'>Decatur Hills Courtyard</p>
            <p className='distance'>7.3 miles away</p>
        </div>
    </div>      
  );
}

export default Location;