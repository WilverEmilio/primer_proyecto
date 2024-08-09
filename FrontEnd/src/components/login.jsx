import { useState } from "react";
import {Link} from "react-router-dom";

export default function Login() {
    const [textname, setTextName] = useState("");
    const [textpassword, setTextPassword] = useState("");
    const [error, setError] = useState("");

    function handleTextName(event) {
        setTextName(event.target.value);
    }

    function handleTextPassword(event) {
        setTextPassword(event.target.value);
    }

    async function handleClicked(event) {
        event.preventDefault();

        if (textname === "" || textpassword === "") {
            alert("Por favor llene todos los campos");
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:8000/api/login/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    nombre: textname,
                    contrasena: textpassword
                })
            });

            if (response.ok) {
                const data = await response.json();
                const token = data.token;

                console.log('Token recibido:', token);

                localStorage.setItem('token', token);

                setTextName("");
                setTextPassword("");

                // Opcional: Redirigir al usuario o mostrar un mensaje de éxito
                // window.location.href = '/dashboard'; // Ejemplo de redirección
            } else {
                const errorData = await response.json();
                setError(errorData.detail || 'Error en el inicio de sesión');
            }
        } catch (error) {
            console.error('Error al iniciar sesión:', error);
            setError('Error en el inicio de sesión');
        }
    }

    return (
        <form>
            <label htmlFor="nombre">Nombre</label>
            <input id="Nombre" type="text" onChange={(e) => setTextName(e.target.value)} value={textname} />
            <label htmlFor="contrasena">Contraseña</label>
            <input id="Contrasena" type="password" onChange={(e) => setTextPassword(e.target.value)} value={textpassword} />
            <button type="submit" onClick={handleClicked}>Iniciar sesión</button>

            {error && <p>{error}</p>}

            <p style={{ marginTop: '20px' }}>
            ¿No tienes cuenta? <Link to="/createUser">Crear usuario</Link>
            </p>
            <p>
            <Link to="/products">Agregar Producto</Link>
            </p>
        </form>
    );
}