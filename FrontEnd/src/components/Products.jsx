import { useState } from 'react';

export default function ProductForm() {
  const [productName, setProductName] = useState("");
  const [quantity, setQuantity] = useState("");
  const [batch, setBatch] = useState("");
  const [isPerishable, setIsPerishable] = useState("no");

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (productName === "" || quantity === "" || batch === "") {
      alert("Por favor llene todos los campos");
      return;
    }

    const product = {
      nombre: productName,
      cantidad: quantity,
      lote: batch,
      perecedero: isPerishable === "si"
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/api/products/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(product)
      });

      if (response.ok) {
        alert("Producto agregado con éxito");
        setProductName("");
        setQuantity("");
        setBatch("");
        setIsPerishable("no");
      } else {
        const errorData = await response.json();
        alert(errorData.detail || 'Error al agregar el producto');
      }
    } catch (error) {
      console.error('Error al agregar producto:', error);
      alert('Error al agregar el producto');
    }
  };
  const pageStyle = {
    backgroundImage: 'url(data:image/jpeg;base64)', 
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    minHeight: '50vh',
    padding: '30px',
    color: 'white'
  };

  return (
    <div style={pageStyle}>
      <form onSubmit={handleSubmit}>
        <label htmlFor="productName">Nombre del Producto</label>
        <input
          id="productName"
          type="text"
          onChange={(e) => setProductName(e.target.value)}
          value={productName}
        />

        <label htmlFor="quantity">Cantidad</label>
        <input
          id="quantity"
          type="number"
          onChange={(e) => setQuantity(e.target.value)}
          value={quantity}
        />

        <label htmlFor="batch">Lote</label>
        <input
          id="batch"
          type="text"
          onChange={(e) => setBatch(e.target.value)}
          value={batch}
        />

        <label htmlFor="isPerishable">¿Es Perecedero?</label>
        <select
          id="isPerishable"
          onChange={(e) => setIsPerishable(e.target.value)}
          value={isPerishable}
        >
          <option value="si">Sí</option>
          <option value="no">No</option>
        </select>

        <button type="submit">Agregar Producto</button>
      </form>
    </div>
  );
}
