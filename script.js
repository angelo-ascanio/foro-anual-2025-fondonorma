document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const id = window.location.pathname.split("/").pop();

    fetch("data.json")
        .then(response => response.json())
        .then(data => {
            const user = data.find(item => item.ID === id);
            const infoDiv = document.getElementById("info");

            if (user) {
                infoDiv.innerHTML = `
                    <p><strong>ID:</strong> ${user.ID}</p>
                    <p><strong>Nombre:</strong> ${user.Nombre}</p>
                    <p><strong>Apellido:</strong> ${user.Apellido}</p>
                    <p><strong>Empresa:</strong> ${user.Empresa}</p>
                `;
            } else {
                infoDiv.innerHTML = "<p>ID not found.</p>";
            }
        })
        .catch(error => console.error("Error fetching data:", error));
});
