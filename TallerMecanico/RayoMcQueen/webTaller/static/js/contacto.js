

function validarContacto(event) {
    event.preventDefault(); // Evita el envío del formulario

    var nombre = document.getElementById('txtNombre').value;
    var email = document.getElementById('txtEmailMensaje').value;
    var telefono = document.getElementById('txtTelefono').value;

    if (nombre.trim() === '' || email.trim() === '' || telefono.trim() === '') {
        alert('Por favor, complete todos los campos del formulario.');
        return;
    }

    var telefonoLength = telefono.trim().length;
    if (telefonoLength !== 9) {
        alert('El número de teléfono debe tener 9 dígitos.');
        return;
    }

    event.target.form.submit();
}

document.getElementById('contactoForm').addEventListener('submit', validarContacto);
