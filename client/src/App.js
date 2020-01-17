import React from 'react';
import {
  BrowserRouter as Router,
  Route
} from 'react-router-dom';
import HomePage from './pages/HomePage/home-page.component';

import './App.css';

import 'semantic-ui-css/semantic.min.css'

function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path='/' component={HomePage} />
      </Router>
    </div>
  );
}

export default App;
