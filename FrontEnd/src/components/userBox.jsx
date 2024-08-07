export default function UserBox({nombre, contrasena, correo,cargo, id_usuario}) {
    return (
    <article>
        <h2>{nombre}</h2>
        <p>{contrasena}</p>
        <p>{correo}</p>
        <p>{cargo}</p>
        <p>{id_usuario}</p>
    </article>
    )
}