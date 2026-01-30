export function initTeclado(onLetra) {
    const letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ".split("");
    const teclado = document.getElementById("teclado");

    teclado.innerHTML = "";

    letras.forEach(l => {
        const btn = document.createElement("button");
        btn.textContent = l;
        btn.classList.add("tecla");
        btn.addEventListener("click", () => onLetra(l));
        teclado.appendChild(btn);
    });
}

export function resetearTeclado() {
    document.querySelectorAll(".tecla").forEach(b => {
        b.disabled = false;
        b.classList.remove("acierto", "fallo");
    });
}
