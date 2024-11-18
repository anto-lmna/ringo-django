// Carga de foto de perfil
document.getElementById('id_foto').addEventListener('change', function(event) {
    var reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('foto-preview').src = e.target.result;
    }
    reader.readAsDataURL(event.target.files[0]);
});

// Espera a que el DOM esté cargado
document.addEventListener("DOMContentLoaded", function() {
    // Obtiene el input de la foto y la vista previa
    const fotoInput = document.getElementById("id_foto");
    const fotoPreview = document.getElementById("foto-preview");

    // Agrega un evento para actualizar la vista previa cuando el usuario selecciona un archivo
    fotoInput.addEventListener("change", function(event) {
        const file = event.target.files[0];
        
        // Verifica si se seleccionó un archivo
        if (file) {
            // Crea una URL para la imagen seleccionada
            const reader = new FileReader();
            
            // Cuando la imagen se carga, actualiza el src de la imagen de vista previa
            reader.onload = function(e) {
                fotoPreview.src = e.target.result;
            };
            
            // Lee el archivo como una URL de datos
            reader.readAsDataURL(file);
        }
    });
});
