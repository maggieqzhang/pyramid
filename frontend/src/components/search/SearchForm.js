import React from 'react';
import './styles.css';

const SearchForm = () => {
    
    return (
        <div className='search-wrapper'>
            <input placeholder='Cuisine or Restaurant Name' type='text'></input>
            <input placeholder='Pickup Time' type='date'></input>
            <button className='submit-btn' type='submit'>Search</button>
        </div>
    )
};

export default SearchForm;