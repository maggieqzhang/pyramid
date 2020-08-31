import React from 'react';
import './styles.css';
import SearchForm from '../components/search/SearchForm';

const Home = () => {
  return (
    <div className='main'>
      <h1>Welcome to the Group Delivery app!</h1>
      <SearchForm/>
    </div>
  );
}

export default Home;