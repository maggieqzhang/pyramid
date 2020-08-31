import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Nav from './components/nav/Nav';
import Home from './pages/Home';

function App() {
  return (
    <Router>
      <Nav/>
      <Switch>
        <Route path='/' exact component={Home} />
        <Route path='/login' exact component={Login} />
        <Route path='/signup' exact component={Signup} />
      </Switch>
    </Router>
  );
}

export default App;
