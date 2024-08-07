import { useEffect, useState } from 'react'

import UserBox from './components/userBox'
import CreateUser from './components/createUser'
import Login from './components/login'

function App() {
  const [users, setUsers] = useState([])
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/usuarios/')
      .then(res => res.json())
      .then(res => setUsers(res))
  },[])
  return (  
    <>
      <h1>Frontend and Backend API</h1>

      {
        <Login />
      }

      {
        <CreateUser />
      }

      {
        users.map((user) => (
          <UserBox 
            key={user.id_usuario} 
            nombre={user.nombre} 
            contrasena={user.contrasena} 
            correo={user.correo} 
            cargo={user.cargo} 
            id_usuario={user.id_usuario} 
          />
        ))      
      }
    </>
  )
}

export default App