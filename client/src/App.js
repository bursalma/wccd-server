import React from 'react';
import {
  BrowserRouter as Router,
  Route
} from 'react-router-dom'
import FormPage from './pages/FormPage/form-page.component'

import 'semantic-ui-css/semantic.min.css'

function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path='/' component={FormPage} />
      </Router>
    </div>
  );
}

export default App;
