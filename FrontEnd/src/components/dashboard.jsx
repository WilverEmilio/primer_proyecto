import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function Dashboard() {
    const navigate = useNavigate();

    return (
        <div>
            <h1>Bienvenido al Dashboard</h1>
            <div>
                <button onClick={() => navigate('/perecederos')}>
                    Productos Perecederos
                </button>
                <button onClick={() => navigate('/noperecederos')}>
                    Productos No Perecederos
                </button>
                <button onClick={() => navigate('/')}>
                    Regresar
                </button>
            </div>
        </div>
    );
}
