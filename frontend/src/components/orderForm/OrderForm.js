import React from 'react';
import ReactDOM from 'react-dom';
import './styles.css';
import { Link } from 'react-router-dom';
import entreeMeal1 from './../../assets/entreeMeal1.jpg';
import entreeMeal2 from './../../assets/entreeMeal2.jpg';
import entreeMeal3 from './../../assets/entreeMeal3.jpg';
import entreeMeal4 from './../../assets/entreeMeal4.jpg';

const OrderForm = ({ isShowing, hide }) => isShowing ? ReactDOM.createPortal(
    <React.Fragment>
      <div className="modal-overlay"/>
      <div className="modal-wrapper" aria-modal aria-hidden tabIndex={-1} role="dialog">
        <div className="modal">
          <div className="modal-header">
            <button type="button" className="modal-close-button" data-dismiss="modal" aria-label="Close" onClick={hide}>
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <h1>Ordering from: Chipotle</h1>
          <h2>Entrees</h2>
          <div className='venue-meals'>
            <img src={entreeMeal1}/>
            <img src={entreeMeal2}/>
            <img src={entreeMeal3}/>
            <img src={entreeMeal4}/>
          </div>
          <h2>Sides</h2>
          <div className='venue-meals'>
            <img src={entreeMeal1}/>
            <img src={entreeMeal2}/>
            <img src={entreeMeal3}/>
            <img src={entreeMeal4}/>
          </div>
          <Link to='/checkout'><button className='add-to-cart-btn'>Add to Cart</button></Link>
        </div>
      </div>
    </React.Fragment>, document.body
  ) : null;
  
  export default OrderForm;