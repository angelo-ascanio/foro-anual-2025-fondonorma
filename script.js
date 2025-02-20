document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const hash = urlParams.get("id");

    fetch("data.json")
        .then(response => response.json())
        .then(data => {
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
        })
        .catch(error => console.error("Error fetching data:", error));
});
