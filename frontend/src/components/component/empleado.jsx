"use client"

import { useState, useEffect } from "react";
import axios from "axios";
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from "@/components/ui/table";
//import { AlertDialog, AlertDialogContent, AlertDialogHeader, AlertDialogTitle, AlertDialogDescription, AlertDialogFooter, AlertDialogCancel, AlertDialogAction } from "@/components/ui/alert";

export function Empleado() {
  const [empleados, setEmpleados] = useState([]);
  const [nombre, setNombre] = useState("");
  const [apellidos, setApellido] = useState("");
  const [telefono, setTelefono] = useState("");
  const [direccion, setDireccion] = useState("");
  const [disponible, setDisponible] = useState(true);
  const [editingId, setEditingId] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [showDeleteConfirmation, setShowDeleteConfirmation] = useState(false);
  const [deleteId, setDeleteId] = useState(null);

  useEffect(() => {
    // Obtener los datos al montar el componente
    axios.get("http://localhost:8000/api/empleadosObtener/")
      .then((response) => {
        setEmpleados(response.data);
      })
      .catch((error) => {
        console.error("Error al obtener los empleados:", error);
      });
  }, []);

  const handleAdd = () => {
    setShowForm(true);
    setEditingId(null);
    setNombre("");
    setApellido("");
    setTelefono("");
    setDireccion("");
  };

  const handleEdit = (id) => {
    const empleado = empleados.find((item) => item.idempleado === id);
    setNombre(empleado.nombre);
    setApellido(empleado.apellidos);
    setTelefono(empleado.telefono);
    setDireccion(empleado.direccion);
    setEditingId(id);
    setShowForm(true);
  };

  const handleSave = async () => {
    try {
      const empleadoData = {
        nombre,
        apellidos,
        telefono,
        direccion,
        disponible,  // Booleano
      };
  
      console.log(empleadoData);  // Imprime los datos que estás enviando
  
      if (editingId) {
        // Editar empleado
        await axios.put(`http://localhost:8000/api/empleadoUpdate/${editingId}`, empleadoData);
      } else {
        // Crear nuevo empleado
        const response = await axios.post("http://localhost:8000/api/empleados/", empleadoData);
        setEmpleados([...empleados, response.data]);
      }
      setShowForm(false);
      setEditingId(null);
    } catch (error) {
      console.error("Error al guardar el empleado:", error);
    }
  };
  
  const handleDelete = (id) => {
    setShowDeleteConfirmation(true);
    setDeleteId(id);
  };

  const handleConfirmDelete = async () => {
    try {
      await axios.delete(`http://localhost:8000/api/empleadoDelete/${deleteId}`);
      setEmpleados(empleados.filter((item) => item.idempleado !== deleteId));
      setShowDeleteConfirmation(false);
      setDeleteId(null);
    } catch (error) {
      console.error("Error al eliminar el empleado:", error);
    }
  };

  const handleCancelDelete = () => {
    setShowDeleteConfirmation(false);
    setDeleteId(null);
  };

  const handleCloseForm = () => {
    setShowForm(false);
    setEditingId(null);
  };

  return (
    <div className="w-full max-w-3xl mx-auto">
      <div className="flex justify-between items-center mb-4">
        <div>
          <h2 className="text-2xl font-bold mb-2">Empleados</h2>
          <p className="text-muted-foreground">Completa los campos a continuación.</p>
        </div>
        <Button onClick={handleAdd}>Agregar</Button>
      </div>
      {showForm && (
        <Card className="w-full max-w-md mt-4 relative z-10">
          <button
            className="absolute top-4 right-4 text-muted-foreground hover:text-primary"
            onClick={handleCloseForm}>
            <XIcon className="w-5 h-5" />
          </button>
          <CardHeader>
            <CardTitle>Empleado</CardTitle>
            <CardDescription>Completa los campos a continuación.</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="name">Nombre</Label>
              <Input
                id="name"
                placeholder="Ingresa tu nombre"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)} />
            </div>
            <div className="space-y-2">
              <Label htmlFor="lastName">Apellidos</Label>
              <Input
                id="lastName"
                placeholder="Ingresa tus apellidos"
                value={apellidos}
                onChange={(e) => setApellido(e.target.value)} />
            </div>
            <div className="space-y-2">
              <Label htmlFor="phone">Teléfono</Label>
              <Input
                id="phone"
                placeholder="Ingresa tu teléfono"
                value={telefono}
                onChange={(e) => setTelefono(e.target.value)} />
            </div>
            <div className="space-y-2">
              <Label htmlFor="address">Dirección</Label>
              <Input
                id="address"
                placeholder="Ingresa tu dirección"
                value={direccion}
                onChange={(e) => setDireccion(e.target.value)} />
            </div>
          </CardContent>
          <CardFooter className="flex justify-end">
            <Button onClick={handleSave}>Guardar</Button>
          </CardFooter>
        </Card>
      )}
      <div className="border rounded-lg overflow-hidden">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>ID</TableHead>
              <TableHead>Nombre</TableHead>
              <TableHead>Apellidos</TableHead>
              <TableHead>Teléfono</TableHead>
              <TableHead>Dirección</TableHead>
              <TableHead>Disponible</TableHead>
              <TableHead>Acciones</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {empleados.map((item) => (
              <TableRow key={item.idempleado}>
                <TableCell>{item.idempleado}</TableCell>
                <TableCell>{item.nombre}</TableCell>
                <TableCell>{item.apellidos}</TableCell>
                <TableCell>{item.telefono}</TableCell>
                <TableCell>{item.direccion}</TableCell>
                <TableCell>{item.disponible ? "Sí" : "No"}</TableCell>
                <TableCell>
                  <div className="flex gap-2">
                    <Button onClick={() => handleEdit(item.idempleado)}>Editar</Button>
                    <Button onClick={() => handleDelete(item.idempleado)}>
                      Deshabilitar
                    </Button>
                  </div>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>

    </div>
  );
}

function XIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round">
      <path d="M18 6L6 18" />
      <path d="M6 6L18 18" />
    </svg>
  );
}
