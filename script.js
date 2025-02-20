document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const hash = urlParams.get("id");

    const encryptionKey = "YOUR_BASE64_KEY"; // Use your actual base64 key here

    fetch("data.json")
        .then(response => response.text())
        .then(encryptedData => {
            // Decode the base64 key
            const key = new fernet.Secret(encryptionKey);

            // Decrypt the data using fernet.js
            const token = new fernet.Token({
                secret: key,
                token: encryptedData,
                ttl: 0 // Setting TTL to 0 to disable expiration
            });

            const decryptedText = token.decode();
            const data = JSON.parse(decryptedText);
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
