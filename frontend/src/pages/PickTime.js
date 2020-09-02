import React from "react";
import UserNav from "../components/nav/UserNav";
import ScrollMenu from "../components/scrollMenu/ScrollMenu";

const PickTime = () => {

  return (
    <React.Fragment>
      <UserNav/>
      <div className='pick-time-wrapper'>
        <p>Choose a restaurant from one <br/>of the scheduled time columns.</p>
      </div>
      <ScrollMenu/>
    </React.Fragment>
  );
};

export default PickTime;