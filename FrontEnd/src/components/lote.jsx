import { useState } from "react"

export default function CreateLote() {
    const [idArticulo, setIdArticulo] = useState("")
    const [numeroLote, setNumeroLote] = useState("")
    const [cantidad, setCantidad] = useState("")
    const [fechaVencimiento, setFechaVencimiento] = useState("")

    function handleIdArticuloChange(event) {
        setIdArticulo(event.target.value)
    }

    function handleNumeroLoteChange(event) {
        setNumeroLote(event.target.value)
    }

    function handleCantidadChange(event) {
        setCantidad(event.target.value)
    }

    function handleFechaVencimientoChange(event) {
        setFechaVencimiento(event.target.value)
    }

    function handleClicked(event) {
        event.preventDefault()
        console.log(idArticulo, numeroLote, cantidad, fechaVencimiento)

        fetch("http://127.0.0.1:8000/api/lotes/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                idarticulo: idArticulo,
                numero_lote: numeroLote,
                cantidad: cantidad,
                fecha_vencimiento: fechaVencimiento
            })
        }).then(() => {
            setIdArticulo("")
            setNumeroLote("")
            setCantidad("")
            setFechaVencimiento("")
        })
    }

    return (
        <form>
            <label htmlFor="idarticulo">ID Artículo</label>
            <input id="idarticulo" type="text" onChange={handleIdArticuloChange} value={idArticulo} />

            <label htmlFor="numero_lote">Número de Lote</label>
            <input id="numero_lote" type="text" onChange={handleNumeroLoteChange} value={numeroLote} />

            <label htmlFor="cantidad">Cantidad</label>
            <input id="cantidad" type="number" onChange={handleCantidadChange} value={cantidad} />

            <label htmlFor="fecha_vencimiento">Fecha de Vencimiento</label>
            <input id="fecha_vencimiento" type="date" onChange={handleFechaVencimientoChange} value={fechaVencimiento} />

            <button type="submit" onClick={handleClicked}>Crear lote</button>
        </form>
    )
}
