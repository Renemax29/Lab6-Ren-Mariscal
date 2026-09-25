// Mensaje al cargar la página
console.log("Estación Meteorológica del Campus: página cargada correctamente.");

document.addEventListener("DOMContentLoaded", function () {
  const formulario = document.querySelector("#contacto form");
  if (formulario) {
    formulario.addEventListener("submit", function () {
      console.log("Suscripción a alertas climáticas enviada.");
    });
  }
});
