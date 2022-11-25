import React from 'react';

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import Header from './components/Header';

function App() {
  return (
    <div className="App">
      <Header/>
    </div>
  );
}

export default App;
