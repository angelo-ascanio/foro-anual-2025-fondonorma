document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const hash = urlParams.get("id");

    // Retrieve the environment secret
    const dataSecret = document.querySelector('meta[name="data-secret"]').getAttribute('content');

    // Parse the JSON data from the environment secret
    const data = JSON.parse(dataSecret);

    const user = data.find(item => item.hash === hash);
    const infoDiv = document.getElementById("info");

    if (user) {
        infoDiv.innerHTML = `
            <div class="info-entry">
                <p><strong>ID:</strong> ${user.ID}</p>
                <p><strong>Nombre:</strong> ${user.Nombre}</p>
                <p><strong>Apellido:</strong> ${user.Apellido}</p>
                <p><strong>Empresa:</strong> ${user.Empresa}</p>
            </div>
        `;
    } else {
        infoDiv.innerHTML = '<p class="not-found">¡ID sin registro!</p>';
    }
});
