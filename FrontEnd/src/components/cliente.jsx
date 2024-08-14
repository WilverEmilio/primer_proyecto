import { useState } from "react";

export default function Cliente() {
    const [nombre, setNombre] = useState("");
    const [apellido, setApellido] = useState("");
    const [runDocumento, setRunDocumento] = useState("");
    const [direccion, setDireccion] = useState("");
    const [telefono, setTelefono] = useState("");
    const [email, setEmail] = useState("");

    function handleNombre(event) {
        setNombre(event.target.value);
    }
    
    function handleApellido(event) {
        setApellido(event.target.value);
    }
    
    function handleRunDocumento(event) {
        setRunDocumento(event.target.value);
    }
    
    function handleDireccion(event) {
        setDireccion(event.target.value);
    }
    
    function handleTelefono(event) {
        setTelefono(event.target.value);
    }
    
    function handleEmail(event) {
        setEmail(event.target.value);
    }

    function handleSubmit(event) {
        event.preventDefault();

        // Puedes ajustar la URL a la de tu API
        fetch("http://127.0.0.1:8000/api/clientes/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre: nombre,
                apellido: apellido,
                run_documento: runDocumento,
                direccion: direccion,
                telefono: telefono,
                email: email
            })
        })
        .then(response => response.json())
        .then(() => {
            // Limpiar los campos del formulario
            setNombre("");
            setApellido("");
            setRunDocumento("");
            setDireccion("");
            setTelefono("");
            setEmail("");
        });
    }

    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="nombre">Nombre</label>
            <input id="nombre" type="text" onChange={handleNombre} value={nombre} />
            
            <label htmlFor="apellido">Apellido</label>
            <input id="apellido" type="text" onChange={handleApellido} value={apellido} />
            
            <label htmlFor="run_documento">RUN Documento</label>
            <input id="run_documento" type="text" onChange={handleRunDocumento} value={runDocumento} />
            
            <label htmlFor="direccion">Dirección</label>
            <input id="direccion" type="text" onChange={handleDireccion} value={direccion} />
            
            <label htmlFor="telefono">Teléfono</label>
            <input id="telefono" type="text" onChange={handleTelefono} value={telefono} />
            
            <label htmlFor="email">Email</label>
            <input id="email" type="email" onChange={handleEmail} value={email} />
            
            <button type="submit">Agregar Cliente</button>
        </form>
    );
}
