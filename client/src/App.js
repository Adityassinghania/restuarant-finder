import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Restaurant from './pages/Restaurant'


function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path='/restaurants/:cityName' element={<Restaurant/>} />
        </Routes>
      </Router>     
    </>
  );
}

export default App;
