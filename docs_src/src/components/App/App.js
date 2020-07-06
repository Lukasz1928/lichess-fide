import React from 'react';
import './App.css';
import Home from '../Home/Home/Home';
import Result from '../Result/Result/Result';
import {BrowserRouter as Router, Route} from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="container">
        <Route exact path="/" component={Home}/>
        <Route path="/result" component={Result}/>
        <Route component={Home}/>
      </div>
    </Router>
  );
}

export default App;
