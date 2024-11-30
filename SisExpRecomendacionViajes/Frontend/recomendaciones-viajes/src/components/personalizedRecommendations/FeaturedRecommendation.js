import React from 'react';

const FeaturedRecommendation = () => {
  return (
    <div className="section-2">
      <h2>Creemos que te podría gustar</h2>
      <div className="featured-recommendation">
        <img src="/path/to/your/featured-image.jpg" alt="Recomendación Destacada" />
        <h3>Nombre del Destino</h3>
        <p>Presupuesto: Medio</p>
        <p>Actividad: Playa</p>
        <button onClick={() => alert('Dirigiendo a la búsqueda...')}>Me interesa</button>
      </div>
    </div>
  );
};

export default FeaturedRecommendation;
