document.addEventListener("DOMContentLoaded", function () {
    const contentDiv = document.getElementById("content");
    const btnPacientes = document.getElementById("btnPacientes");
    const btnMedicos = document.getElementById("btnMedicos");
    const btnCitas = document.getElementById("btnCitas");

    const loadContent = async (url) => {
        const response = await fetch(url);
        const html = await response.text();
        contentDiv.innerHTML = html;

        // Inicializar DataTable si es necesario
        if (url.includes("paciente")) {
            initDataTable();
        }
    };

    btnPacientes.addEventListener("click", () => {
        loadContent("{% url 'list_paciente' %}");
    });

    btnMedicos.addEventListener("click", () => {
        loadContent("{% url 'list_medico' %}");
    });

    btnCitas.addEventListener("click", () => {
        loadContent("{% url 'list_cita' %}");
    });
});
