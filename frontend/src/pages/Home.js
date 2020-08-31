import React from 'react';
import './styles.css';
import SearchBar from '../components/search/SearchBar';

const Home = () => {
  return (
    <div className='main'>
      <h1>Welcome to the Group Delivery app!</h1>
      <SearchBar/>
    </div>
  );
}

export default Home;