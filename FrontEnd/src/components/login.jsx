import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";

export default function Login() {
    const [textname, setTextName] = useState("");
    const [textpassword, setTextPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        // Eliminar la cookie cuando el componente Login se monta
        document.cookie = "access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        console.log('Token eliminado al regresar al login');
    }, []);

    function handleTextName(event) {
        setTextName(event.target.value);
    }

    function handleTextPassword(event) {
        setTextPassword(event.target.value);
    }

    async function handleLogin(event) {
        event.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/login/', {
                nombre: textname,
                contrasena: textpassword,
            }, { withCredentials: true });
            
            const { token, expires_at } = response.data;

            console.log('Token:', token);
            console.log('Expira en:', expires_at);

            navigate('/Dashboard'); 
        } catch (error) {
            setError("Error al iniciar sesión. Verifique sus credenciales y vuelva a intentarlo.");
            console.error('Error during login:', error);
        }
    }

    return (
        <div>
            <form onSubmit={handleLogin}>
                <input type="text" value={textname} onChange={handleTextName} placeholder="Username" required />
                <input type="password" value={textpassword} onChange={handleTextPassword} placeholder="Password" required />
                {error && <p>{error}</p>}
                <button type="submit">Login</button>
                <p style={{ marginTop: '20px' }}>
                ¿No tienes cuenta? <Link to="/createUser">Crear usuario</Link>
                </p>
                <p>
                <Link to="/products">Agregar Producto</Link>
                </p>
                </form>
        </div>
    );
}
