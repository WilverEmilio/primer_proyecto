import { useState } from "react"

export default function CreateCategoria() {
    const [nombre, setNombre] = useState("")
    const [descripcion, setDescripcion] = useState("")

    function handleNombreChange(event) {
        setNombre(event.target.value)
    }

    function handleDescripcionChange(event) {
        setDescripcion(event.target.value)
    }

    function handleClicked(event) {
        event.preventDefault()
        console.log(nombre, descripcion)

        fetch("http://127.0.0.1:8000/api/categorias/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre: nombre,
                descripcion: descripcion
            })
        }).then(() => {
            setNombre("")
            setDescripcion("")
        })
    }

    return (
        <form>
            <label htmlFor="nombre">Nombre</label>
            <input id="nombre" type="text" onChange={handleNombreChange} value={nombre} />

            <label htmlFor="descripcion">Descripción</label>
            <input id="descripcion" type="text" onChange={handleDescripcionChange} value={descripcion} />

            <button type="submit" onClick={handleClicked}>Crear categoría</button>
        </form>
    )
}
