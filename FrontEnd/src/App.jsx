import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { useEffect, useState } from 'react';

import UserBox from './components/userBox';
import CreateUser from './components/createUser';
import Login from './components/login';
import Products from './components/Products'; 

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/usuarios/')
      .then(res => res.json())
      .then(res => setUsers(res))
  },[])

  return (
    <Router>
      <div>
        <h1>Abarrotería "La Bendición"</h1>

        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/createUser" element={<CreateUser />} />
          <Route path="/Products" element={<Products />} />
        </Routes>

        {/* {
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
        } */}
      </div>
    </Router>
  )
}

export default App;
