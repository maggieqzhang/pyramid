import React from 'react';
import './styles.css';
import SearchForm from '../components/search/SearchForm';
import HomeNav from '../components/nav/HomeNav';

const Home = () => {
  return (
      <React.Fragment>
        <HomeNav/>
        <div className='main'>
        {/* <h1>Welcome to the Group Delivery app!</h1>
        <SearchForm/> */}
        </div>
      </React.Fragment>
  );
}

export default Home;