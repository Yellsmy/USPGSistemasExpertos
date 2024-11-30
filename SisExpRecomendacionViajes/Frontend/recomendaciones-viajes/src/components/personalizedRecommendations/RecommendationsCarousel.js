import React from 'react';
import './RecommendationsCarousel.css';

const RecommendationsCarousel = () => {
  return (
    <div className="recommendations-carousel">
      <h3>Recomendaciones</h3>
      <div className="recommendation-card">
        {/* Card individual */}
        <h4>Destino</h4>
        <p>Detalles aquí</p>
        <button>Me interesa</button>
      </div>
    </div>
  );
};

export default RecommendationsCarousel;
