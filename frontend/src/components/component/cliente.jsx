"use client"

import { useState, useEffect } from "react";
import axios from "axios";
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from "@/components/ui/table";

export function Cliente() {
  const [clientes, setClientes] = useState([]);
  const [nombre, setNombre] = useState("");
  const [apellido, setApellido] = useState("");
  const [run_documento, setRun] = useState("");
  const [direccion, setDireccion] = useState("");
  const [telefono, setTelefono] = useState("");
  const [email, setEmail] = useState("");
  const [editingId, setEditingId] = useState(null);
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    fetchClientes();
  }, []);

  const fetchClientes = async () => {
    try {
      const response = await axios.get("http://localhost:8000/api/clientesObtener/");
      setClientes(response.data);
    } catch (error) {
      console.error("Error al obtener los clientes:", error);
    }
  };

  const handleAdd = () => {
    setShowForm(true);
    clearForm();
    setEditingId(null);
  };

  const handleEdit = (id) => {
    const cliente = clientes.find((item) => item.idcliente === id);
    setNombre(cliente.nombre);
    setApellido(cliente.apellido);
    setRun(cliente.run_documento);
    setDireccion(cliente.direccion);
    setTelefono(cliente.telefono);
    setEmail(cliente.email);
    setEditingId(id);
    setShowForm(true);
  };

  const handleSave = async () => {
    const clienteData = {
      nombre,
      apellido,
      run_documento,
      direccion,
      telefono,
      email,
    };

    try {
      if (editingId) {
        await axios.put(`http://localhost:8000/api/clienteActualizar/${editingId}`, clienteData);
        fetchClientes();
      } else {
        const response = await axios.post("http://localhost:8000/api/clientes/", clienteData);
        setClientes([...clientes, response.data]);
      }
      setShowForm(false);
      clearForm();
    } catch (error) {
      console.error("Error al guardar el cliente:", error);
    }
  };

  const clearForm = () => {
    setNombre("");
    setApellido("");
    setRun("");
    setDireccion("");
    setTelefono("");
    setEmail("");
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/api/clienteDelete/${id}`);
      setClientes(clientes.filter((item) => item.idcliente !== id));
    } catch (error) {
      console.error("Error al eliminar el cliente:", error);
    }
  };

  const handleCloseForm = () => {
    setShowForm(false);
    clearForm();
    setEditingId(null);
  };

  return (
    <div className="w-full max-w-3xl mx-auto">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold mb-2">Clientes</h2>
        <Button onClick={handleAdd}>Agregar</Button>
      </div>

      {showForm && (
        <Card className="w-full max-w-md mt-4">
          <CardHeader>
            <CardTitle>Formulario de Cliente</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label>Nombre</Label>
              <Input value={nombre} onChange={(e) => setNombre(e.target.value)} placeholder="Nombre" />
            </div>
            <div className="space-y-2">
              <Label>Apellido</Label>
              <Input value={apellido} onChange={(e) => setApellido(e.target.value)} placeholder="Apellido" />
            </div>
            <div className="space-y-2">
              <Label>RUN Documento</Label>
              <Input value={run_documento} onChange={(e) => setRun(e.target.value)} placeholder="RUN Documento" />
            </div>
            <div className="space-y-2">
              <Label>Dirección</Label>
              <Input value={direccion} onChange={(e) => setDireccion(e.target.value)} placeholder="Dirección" />
            </div>
            <div className="space-y-2">
              <Label>Teléfono</Label>
              <Input value={telefono} onChange={(e) => setTelefono(e.target.value)} placeholder="Teléfono" />
            </div>
            <div className="space-y-2">
              <Label>Email</Label>
              <Input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
            </div>
          </CardContent>
          <CardFooter className="flex justify-end">
            <Button onClick={handleSave}>Guardar</Button>
            <Button onClick={handleCloseForm} variant="outline">Cancelar</Button>
          </CardFooter>
        </Card>
      )}

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>ID</TableHead>
            <TableHead>Nombre</TableHead>
            <TableHead>Apellido</TableHead>
            <TableHead>RUN</TableHead>
            <TableHead>Dirección</TableHead>
            <TableHead>Teléfono</TableHead>
            <TableHead>Email</TableHead>
            <TableHead>Acciones</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {clientes.map((cliente) => (
            <TableRow key={cliente.idcliente}>
              <TableCell>{cliente.idcliente}</TableCell>
              <TableCell>{cliente.nombre}</TableCell>
              <TableCell>{cliente.apellido}</TableCell>
              <TableCell>{cliente.run_documento}</TableCell>
              <TableCell>{cliente.direccion}</TableCell>
              <TableCell>{cliente.telefono}</TableCell>
              <TableCell>{cliente.email}</TableCell>
              <TableCell>
                <Button onClick={() => handleEdit(cliente.idcliente)}>Editar</Button>
                <Button onClick={() => handleDelete(cliente.idcliente)}>Eliminar</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
