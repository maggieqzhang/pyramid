import React from 'react';
import './styles.css';
import SearchForm from '../components/search/SearchForm';
import HomeNav from '../components/nav/HomeNav';
import ScrollMenu from '../components/scrollMenu/ScrollMenu';

const Home = () => {
  return (
      <React.Fragment>
        <HomeNav/>
        <div className='main'>
        {/* <h1>Welcome to the Group Delivery app!</h1>
        <SearchForm/> */}
        <ScrollMenu/>
        </div>
      </React.Fragment>
  );
}

export default Home;