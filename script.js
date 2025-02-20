document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const hash = urlParams.get("id");

    // Fetch the encryption key from GitHub Secrets (set it in your environment)
    const encryptionKey = process.env.ENCRYPTION_KEY;

    fetch("data.json")
        .then(response => response.arrayBuffer())
        .then(encryptedData => {
            // Convert encryption key from base64 to Uint8Array
            const keyBytes = Uint8Array.from(atob(encryptionKey), c => c.charCodeAt(0));
            
            // Use SubtleCrypto to decrypt the data
            const cryptoKey = window.crypto.subtle.importKey(
                "raw", 
                keyBytes, 
                "AES-CBC", 
                false, 
                ["decrypt"]
            );

            const iv = new Uint8Array(16);  // Assume that the IV is all zeros, you need to ensure this matches your encryption setup in Python.
            const decryptedData = window.crypto.subtle.decrypt(
                { name: "AES-CBC", iv: iv },
                cryptoKey,
                encryptedData
            );

            return decryptedData;
        })
        .then(decryptedArrayBuffer => {
            const decryptedText = new TextDecoder().decode(decryptedArrayBuffer);
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
