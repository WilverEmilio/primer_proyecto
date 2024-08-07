import {useState } from "react"

export default function CreateUser() {
    const [textname, setTextName] = useState("")
    const [textpassword, setTextPassword] = useState("")
    const [textemail, setTextEmail] = useState("")
    const [textjob, setTextJob] = useState("")
    function handleTextName(event) {
        setTextName(event.target.value)
    }
    function handleTextPassword(event) {
        setTextPassword(event.target.value)
    }
    function handleTextEmail(event) {
        setTextEmail(event.target.value)
    }
    function handleTextJob(event) {
        setTextJob(event.target.value)
    }
    function handleClicked(event) {
        event.preventDefault()
        console.log(textname, textpassword, textemail, textjob)

        fetch("http://127.0.0.1:8000/api/usuarios/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre: textname,
                contrasena: textpassword,
                correo: textemail,
                cargo: textjob
            })
        }).then(() => {
            setTextName("")
            setTextPassword("")
            setTextEmail("")
            setTextJob("")
        })
    }
    return(
    <form>
        <label htmlFor="nombre">Nombre</label>
        <input id = "nombre" type="text" onChange={handleTextName} value={textname} />
        <label htmlFor="contrasena">Contraseña</label>
        <input id = "contrasena" type="password" onChange={handleTextPassword} value={textpassword} />
        <label htmlFor="correo">Correo</label>
        <input id = "correo" type="email" onChange={handleTextEmail}  value={textemail}/>
        <label htmlFor="cargo">Cargo</label>
        <input id = "cargo" type="text" onChange={handleTextJob}  value={textjob}/>
        <button type="submit" value={"Create User"} onClick={handleClicked}>Crear usuario</button>
    </form>
    )
}