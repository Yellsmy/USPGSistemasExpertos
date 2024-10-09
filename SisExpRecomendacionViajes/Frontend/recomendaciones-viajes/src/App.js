import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainPage from './components/MainPage';
import RecomendacionesGenerales from './components/RecomendacionesGenerales';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/recomendaciones-generales" element={<RecomendacionesGenerales />} />
      </Routes>
    </Router>
  );
}

export default App;

