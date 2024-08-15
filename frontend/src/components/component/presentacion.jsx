/**
* This code was generated by v0 by Vercel.
* @see https://v0.dev/t/wr4uAZJ2Xah
* Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
*/

/** Add fonts into your Next.js project:

import { Inter } from 'next/font/google'

inter({
  subsets: ['latin'],
  display: 'swap',
})

To read more about using these font, please visit the Next.js documentation:
- App Directory: https://nextjs.org/docs/app/building-your-application/optimizing/fonts
- Pages Directory: https://nextjs.org/docs/pages/building-your-application/optimizing/fonts
**/
"use client"

import { useState, useEffect } from "react"
import axios from 'axios'
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from "@/components/ui/table"
// import { AlertDialog, AlertDialogContent, AlertDialogHeader, AlertDialogTitle, AlertDialogDescription, AlertDialogFooter, AlertDialogCancel, AlertDialogAction } from "@/components/ui/alert"

export function Presentacion() {

  const [textname, setTextName] = useState("");
  const [textDescription, setTextDescription] = useState("");
  const [error, setError] = useState("");
  const [data, setData] = useState([]); // Actualizado para manejar los datos de la API
  const [showForm, setShowForm] = useState(false)
  const [editingId, setEditingId] = useState(null)
  const [showDeleteConfirmation, setShowDeleteConfirmation] = useState(false)
  const [deleteId, setDeleteId] = useState(null)

  useEffect(() => {
    // Obtener los datos de la API cuando el componente se monte
    async function fetchData() {
      try {
        const response = await axios.get('http://localhost:8000/api/presentacionesObtener/');
        const fetchedData = response.data.map(item => ({
          id: item.idpresentacion,
          name: item.nombre,
          description: item.descripcion
        }));
        setData(fetchedData);
      } catch (error) {
        console.error('Error al obtener los datos:', error);
      }
    }

    fetchData();
  }, []);

  function handleTextName(event) {
    setTextName(event.target.value);
  }

  function handleTextDescription(event) {
    setTextDescription(event.target.value);
  }

  async function handleSave() {
    try {
      await axios.post('http://localhost:8000/api/presentaciones/', {
        nombre: textname,
        descripcion: textDescription,
      }, { withCredentials: true });

      // Actualiza los datos después de guardar
      const response = await axios.get('http://localhost:8000/api/presentacionesObtener/');
      const fetchedData = response.data.map(item => ({
        id: item.idpresentacion,
        name: item.nombre,
        description: item.descripcion
      }));
      setData(fetchedData);
      
    } catch (error) {
      setError("Error al crear la presentación");
    }
    setShowForm(false);
    setEditingId(null);
  }

  const handleAdd = () => {
    setShowForm(true);
    setEditingId(null);
  }
  const handleEdit = (id) => {
    setShowForm(true);
    setEditingId(id);
  }
  const handleDelete = (id) => {
    setShowDeleteConfirmation(true);
    setDeleteId(id);
  }
  const handleConfirmDelete = () => {
    setData(data.filter((item) => item.id !== deleteId));
    setShowDeleteConfirmation(false);
    setDeleteId(null);
  }
  const handleCancelDelete = () => {
    setShowDeleteConfirmation(false);
    setDeleteId(null);
  }
  const handleCloseForm = () => {
    setShowForm(false);
    setEditingId(null);
  }
  return (
    (<div className="w-full max-w-3xl mx-auto">
      <div className="flex justify-between items-center mb-4">
        <div>
          <h2 className="text-2xl font-bold mb-2">Presentación</h2>
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
            <CardTitle>Presentación</CardTitle>
            <CardDescription>Completa los campos a continuación.</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="name">Nombre</Label>
              <Input
                id="name"
                placeholder="Ingresa tu nombre"
                value={textname}
                onChange={handleTextName} />
            </div>
            <div className="space-y-2">
              <Label htmlFor="description">Descripción</Label>
              <Textarea
                id="description"
                placeholder="Escribe una breve descripción"
                rows={3}
                value={textDescription}
                onChange={handleTextDescription} />
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
              <TableHead>Descripción</TableHead>
              <TableHead>Acciones</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((item) => (
              <TableRow key={item.id}>
                <TableCell>{item.id}</TableCell>
                <TableCell>{item.name}</TableCell>
                <TableCell>{item.description}</TableCell>
                <TableCell>
                  <div className="flex gap-2">
                    <Button onClick={() => handleEdit(item.id)}>Editar</Button>
                  </div>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>)
  );
}

function XIcon(props) {
  return (
    (<svg
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
      <path d="M18 6 6 18" />
      <path d="m6 6 12 12" />
    </svg>)
  );
}
