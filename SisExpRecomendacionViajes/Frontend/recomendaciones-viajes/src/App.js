import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainPage from './components/MainPage';
import RecomendacionesGenerales from './components/RecomendacionesGenerales';
import PersonalizedRecommendations from './components/personalizedRecommendations/PersonalizedRecommendations';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/recomendaciones-generales" element={<RecomendacionesGenerales />} />
        <Route path="/recomendaciones-personalizadas" element={<PersonalizedRecommendations />} />
      </Routes>
    </Router>
  );
}


export default App;

