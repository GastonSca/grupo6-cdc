function validarPerfilAdmin() {

    let nombAdmin = document.getElementById("nombAdmin").value
    let lblNombAdmin = document.getElementById("lblNombAdmin").textContent

    if (validarVacio(nombAdmin, lblNombAdmin)) {
        document.getElementById("nombAdmin").focus()
        return 0
    } else if (validarTexto(nombAdmin, lblNombAdmin)) {
        document.getElementById("nombAdmin").focus()
        return 0
    } else if (validarVaciosInternos(nombAdmin, lblNombAdmin)){
        document.getElementById("nombAdmin").focus()
        return 0
    }


    let apellidoAdmin = document.getElementById("apellidoAdmin").value
    let lblApellidoAdmin = document.getElementById("lblApellidoAdmin").textContent

    if (validarVacio(apellidoAdmin, lblApellidoAdmin)) {
        document.getElementById("apellidoAdmin").focus()
        return 0
    } else if (validarTexto(apellidoAdmin, lblApellidoAdmin)) {
        document.getElementById("apellidoAdmin").focus()
        return 0
    } else if (validarVaciosInternos(apellidoAdmin, lblApellidoAdmin)){
        document.getElementById("apellidoAdmin").focus()
        return 0
    }


    let dniAdmin = document.getElementById("dniAdmin").value
    let lblDniAdmin = document.getElementById("lblDniAdmin").textContent

    if (validarVacio(dniAdmin, lblDniAdmin)) {
        document.getElementById("dniAdmin").focus()
        return 0
    } else if (validarEntero(dniAdmin, lblDniAdmin)) {
        document.getElementById("dniAdmin").focus()
        return 0
    }else if (dniAdmin < 5000000) {
        alert("El N° de DNI no puede ser inferior a 5.000.000")
        document.getElementById("dniAdmin").focus()
        return 0
    } else if (dniAdmin > 99999999) {
        alert("El N° de DNI no puede ser superior a 99.999.999")
        document.getElementById("dniAdmin").focus()
        return 0
    } 


    let nacAdmin = document.getElementById("nacAdmin").value
    let lblNacAdmin = document.getElementById("lblNacAdmin").textContent

    if (validarVacio(nacAdmin, lblNacAdmin)) {
        document.getElementById("nacAdmin").focus()
        return 0
    }


    let contactoAdmin = document.getElementById("contactoAdmin").value
    let lblContactoAdmin = document.getElementById("lblContactoAdmin").textContent

    if (validarVacio(contactoAdmin, lblContactoAdmin)) {
        document.getElementById("contactoAdmin").focus()
        return 0
    } else if (validarEntero(contactoAdmin, lblContactoAdmin)) {
        document.getElementById("contactoAdmin").focus()
        return 0
    }

    alert("¡¡Se ha completado el perfil con éxito!!")
    document.fvalida.submit()
    window.location.href = "admin-inicio.html"
}

function validarVacio(text, lbl) {
    let cadenaText = text.split("")
    if (text.length == " ") {
        alert(`El campo '${alertaLabel(lbl)}' no puede estar vacío.`)
        return true
    }
    if(cadenaText[0] == " "){
        alert(`El campo '${alertaLabel(lbl)}' no puede iniciar vacío.`)
        return true
    }
    if(cadenaText[-1] == " "){
        alert(`El campo '${alertaLabel(lbl)}' no puede finalizar vacío.`)
        return true
    }

    return false
}

// Valida que un campo sea de solo caracteres alfabéticos. 
function validarTexto(text, lbl) {
    let cadenaText = text.split("")

    for (let index = 0; index < cadenaText.length; index++) {
        if (parseInt(cadenaText[index])) {
            alert(`El campo '${alertaLabel(lbl)}' debe contener LETRAS solamente.`)
            return true
        }
    }

    return false
}

// Valida que un campo sea de solo números.
function validarEntero(val, lbl) {
    num = parseInt(val)

    if (isNaN(val)) {
        alert(`El campo '${alertaLabel(lbl)}' debe contener NÚMEROS ENTEROS solamente.`)
        return true
    }
    return false
}

// Valida espacios internos que no deberían estar, como a la hora de colocar el apellido o nombre.
function validarVaciosInternos(val, lbl) {
    val = val.split("")
    for (let i = 0; i < val.length; i++) {
        if (val[i] == " ") {
            alert(`El campo '${alertaLabel(lbl)}' no puede tener ESPACIOS VACIOS.`)
            return true
        }
    }
}