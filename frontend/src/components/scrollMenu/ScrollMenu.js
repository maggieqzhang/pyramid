import React from 'react';
import './styles.css';

const ScrollMenu = () => {
    
    return (
        <div className='scrollmenu-wrapper'>
            <div className='scrollmenu-highlighted'>
                <div className='single-menu'>
                    <h2 className='scrollmenu-header'>12:00 PM</h2>
                    <div className='venue-option'>Chipotle</div>
                    <div className='venue-option'>Panda Express</div>
                    <div className='venue-option'>Cane's</div>
                    <div className='venue-option'>In'n'Out</div>
                    <div className='venue-option'>Falafel Time</div>
                </div>
                <div className='single-menu'>
                    <h2 className='scrollmenu-header'>12:30 PM</h2>
                    <div className='venue-option'>Chipotle</div>
                    <div className='venue-option'>Panda Express</div>
                    <div className='venue-option'>Cane's</div>
                    <div className='venue-option'>In'n'Out</div>
                    <div className='venue-option'>Falafel Time</div>
                </div>
                <div className='single-menu'>
                    <h2 className='scrollmenu-header'>13:00 PM</h2>
                    <div className='venue-option'>Chipotle</div>
                    <div className='venue-option'>Panda Express</div>
                    <div className='venue-option'>Cane's</div>
                    <div className='venue-option'>In'n'Out</div>
                    <div className='venue-option'>Falafel Time</div>
                </div>
            </div>
        </div>
    )
};

export default ScrollMenu;