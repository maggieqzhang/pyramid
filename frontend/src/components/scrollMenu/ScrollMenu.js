import React from 'react';
import './styles.css';

const ScrollMenu = () => {
    
    return (
        <div className='scrollmenu-wrapper'>
            <div className='scrollmenu-highlighted'>
                <div className='single-menu'>
                    <h1 className='scrollmenu-header'>12:00 PM</h1>
                    <div className='venue-option'></div>
                </div>
            </div>
        </div>
    )
};

export default ScrollMenu;