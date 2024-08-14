import { useState } from "react";

export default function Proveedor() {
    const [razonSocial, setRazonSocial] = useState("");
    const [tipoDocumento, setTipoDocumento] = useState("");
    const [numDocumento, setNumDocumento] = useState("");
    const [direccion, setDireccion] = useState("");
    const [telefono, setTelefono] = useState("");
    const [email, setEmail] = useState("");
    const [url, setUrl] = useState("");

    function handleRazonSocial(event) {
        setRazonSocial(event.target.value);
    }
    
    function handleTipoDocumento(event) {
        setTipoDocumento(event.target.value);
    }
    
    function handleNumDocumento(event) {
        setNumDocumento(event.target.value);
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
    
    function handleUrl(event) {
        setUrl(event.target.value);
    }

    function handleSubmit(event) {
        event.preventDefault();

        // Ajusta la URL a la de tu API
        fetch("http://127.0.0.1:8000/api/proveedores/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                razon_social: razonSocial,
                tipo_documento: tipoDocumento,
                num_documento: numDocumento,
                direccion: direccion,
                telefono: telefono,
                email: email,
                url: url
            })
        })
        .then(response => response.json())
        .then(() => {
            // Limpiar los campos del formulario
            setRazonSocial("");
            setTipoDocumento("");
            setNumDocumento("");
            setDireccion("");
            setTelefono("");
            setEmail("");
            setUrl("");
        });
    }

    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="razon_social">Razón Social</label>
            <input id="razon_social" type="text" onChange={handleRazonSocial} value={razonSocial} />
            
            <label htmlFor="tipo_documento">Tipo de Documento</label>
            <input id="tipo_documento" type="text" onChange={handleTipoDocumento} value={tipoDocumento} />
            
            <label htmlFor="num_documento">Número de Documento</label>
            <input id="num_documento" type="text" onChange={handleNumDocumento} value={numDocumento} />
            
            <label htmlFor="direccion">Dirección</label>
            <input id="direccion" type="text" onChange={handleDireccion} value={direccion} />
            
            <label htmlFor="telefono">Teléfono</label>
            <input id="telefono" type="text" onChange={handleTelefono} value={telefono} />
            
            <label htmlFor="email">Email</label>
            <input id="email" type="email" onChange={handleEmail} value={email} />
            
            <label htmlFor="url">URL</label>
            <input id="url" type="text" onChange={handleUrl} value={url} />
            
            <button type="submit">Agregar Proveedor</button>
        </form>
    );
}
