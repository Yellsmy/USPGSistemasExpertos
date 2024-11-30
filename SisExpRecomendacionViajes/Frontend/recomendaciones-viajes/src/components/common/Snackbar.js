import React, { useEffect, useState } from 'react';
import './Snackbar.css';

const Snackbar = ({ message, onClose }) => {
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setVisible(false);
      onClose();
    }, 3000); // Desaparece en 3 segundos

    return () => clearTimeout(timer);
  }, [onClose]);

  if (!visible) return null;

  return <div className="snackbar">{message}</div>;
};

export default Snackbar;
