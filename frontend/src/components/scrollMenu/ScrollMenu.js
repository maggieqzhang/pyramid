import React from 'react';
import './styles.css';
import OrderForm from './../../components/orderForm/OrderForm';
import useModal from './../../useModal';
import leftarrow from './../../assets/leftarrow.png';
import rightarrow from './../../assets/rightarrow.png';

const ScrollMenu = () => {
    const {isShowing, toggle} = useModal();
    const timePeriods = [];
    
    let text = '';
    const leftArrowClick = ()=> {
        let i;
        for (i = 0; i < timePeriods.length; i++) {
        text += timePeriods[i] + "PM";
    }}

    return (
        <div className='scrollmenu-wrapper'>
            <div className='scrollmenu-highlighted'>
                <img src={leftarrow} alt='Left Arrow' onClick={leftArrowClick}/>
                <div className='single-menu'>
                    <h2 className='scrollmenu-header'>12:00 PM</h2>
                    <div className='venue-option' onClick={toggle}>Chipotle</div>
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
                <img src={rightarrow} alt='Right Arrow'/>
            </div>
            <OrderForm isShowing={isShowing} hide={toggle}/>
        </div>
    )
};

export default ScrollMenu;