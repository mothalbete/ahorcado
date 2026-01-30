let citaOriginal = "";
let citaNorm = "";
let autorOriginal = "";
let anioOriginal = "";
let idioma = "";
let videoURL = null;

let aciertosCita = [];
let citaRevelada = false;
let ultimaAdivinada = [];

// === FALLOS ===
let fallos = 0;
const maxFallos = 3;

const equivalencias = {
    "A": ["A", "Á"],
    "E": ["E", "É"],
    "I": ["I", "Í"],
    "O": ["O", "Ó"],
    "U": ["U", "Ú"],
    "N": ["N"],
    "Ñ": ["Ñ"]
};

function normalizar(texto) {
    return texto
        .normalize("NFD")
        .replace(/[\u0300-\u0362\u0364-\u036f]/g, "")
        .toUpperCase();
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("btn-iniciar").addEventListener("click", iniciarJuego);
    document.getElementById("btn-siguiente").addEventListener("click", iniciarJuego);

    document.getElementById("btn-completar-cita").addEventListener("click", () => {
        aciertosCita = citaOriginal.toUpperCase().split("");
        ultimaAdivinada = [];
        mostrarPaneles();
        mostrarVideo();
    });

    document.getElementById("btn-revelar").addEventListener("click", toggleRevelar);

    document.getElementById("cerrar-video").addEventListener("click", cerrarVideo);

    document.getElementById("siguiente-desde-video").addEventListener("click", () => {
        cerrarVideo();
        iniciarJuego();
    });

    // === RESET FALLOS ===
    document.getElementById("btn-reset-fallos").addEventListener("click", () => {
        fallos = 0;
        actualizarFallos();
    });

    generarTeclado();
});

/* ======== INICIAR JUEGO ======== */
function iniciarJuego() {
    fetch("/cita")
        .then(r => r.json())
        .then(data => {
            citaOriginal = data.cita_original || "";
            citaNorm = normalizar(citaOriginal);

            autorOriginal = data.autor_original || "";
            anioOriginal = data.anio_original || "";
            idioma = data.idioma || "";
            videoURL = data.video_url || null;

            document.getElementById("panel-idioma").textContent = idioma.toUpperCase();
            document.getElementById("panel-autor").textContent = autorOriginal;
            document.getElementById("panel-anio").textContent = anioOriginal;

            aciertosCita = [];
            citaRevelada = false;
            ultimaAdivinada = [];

            // === RESET FALLOS AL INICIAR ===
            fallos = 0;
            actualizarFallos();

            resetearTeclado();
            mostrarPaneles();

            document.getElementById("btn-revelar").textContent = "Revelar cita";
        });
}

/* ======== TECLADO ======== */
function generarTeclado() {
    const letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ".split("");
    const teclado = document.getElementById("teclado");

    teclado.innerHTML = "";

    letras.forEach(l => {
        const btn = document.createElement("button");
        btn.textContent = l;
        btn.classList.add("tecla");
        btn.addEventListener("click", () => jugarLetra(l));
        teclado.appendChild(btn);
    });
}

function resetearTeclado() {
    document.querySelectorAll(".tecla").forEach(b => {
        b.disabled = false;
        b.classList.remove("acierto", "fallo");
    });
}

/* ======== PROCESAR LETRA ======== */
function jugarLetra(letra) {
    if (citaRevelada) return;

    const boton = [...document.querySelectorAll(".tecla")].find(b => b.textContent === letra);
    if (!boton) return;

    boton.disabled = true;

    let acierto = false;
    const variantes = equivalencias[letra] || [letra];

    if (variantes.some(v => citaNorm.includes(normalizar(v)))) {
        variantes.forEach(v => aciertosCita.push(v.toUpperCase()));
        acierto = true;
    }

    boton.classList.add(acierto ? "acierto" : "fallo");
    ultimaAdivinada = acierto ? variantes.map(v => v.toUpperCase()) : [];

    // === FALLO ===
    if (!acierto) {
        fallos++;
        actualizarFallos();
    }

    mostrarPaneles();
}

/* ======== REVELAR ======== */
function toggleRevelar() {
    citaRevelada = !citaRevelada;

    document.getElementById("btn-revelar").textContent =
        citaRevelada ? "Ocultar cita" : "Revelar cita";

    if (citaRevelada) {
        document.getElementById("panel-cita").textContent = citaOriginal;
        return;
    }

    ultimaAdivinada = [];
    mostrarPaneles();
}

/* ======== MOSTRAR PANELES ======== */
function mostrarPaneles() {
    if (citaRevelada) {
        document.getElementById("panel-cita").textContent = citaOriginal;
        return;
    }

    mostrarPanel("panel-cita", citaOriginal, citaNorm, aciertosCita, ultimaAdivinada);
}

/* ============================================================
   PANEL AGRUPADO POR PALABRAS (NO SE CORTAN)
   ============================================================ */
function mostrarPanel(id, original, normalizada, aciertos, ultima) {
    const cont = document.getElementById(id);
    if (!cont || !original) {
        cont.innerHTML = "";
        return;
    }

    normalizada = normalizada || normalizar(original);

    const lineasOriginal = original.split("\n");
    const lineasNorm = normalizada.split("\n");

    let html = "";

    for (let li = 0; li < lineasOriginal.length; li++) {
        const palabrasOriginal = lineasOriginal[li].split(" ");
        const palabrasNorm = lineasNorm[li].split(" ");

        palabrasOriginal.forEach((palabraOriginal, idx) => {
            const palabraNorm = palabrasNorm[idx] || "";

            html += `<span class="palabra">`;

            for (let i = 0; i < palabraNorm.length; i++) {
                const letraOriginal = palabraOriginal[i] || " ";
                const letraMayus = letraOriginal.toUpperCase();

                if (!/[A-ZÁÉÍÓÚÑ]/i.test(letraOriginal)) {
                    html += `<span class="letra simbolo">${letraOriginal}</span>`;
                } else {
                    const esAcierto = aciertos.includes(letraMayus);
                    const esRecien = esAcierto && ultima.includes(letraMayus);

                    const contenido = esAcierto ? letraMayus : "";

                    const clases = ["letra"];
                    if (esAcierto) clases.push("acertada");
                    if (esRecien) clases.push("animar");

                    html += `<span class="${clases.join(" ")}">${contenido}</span>`;
                }
            }

            html += `</span> `;
        });

        html += "<br>";
    }

    cont.innerHTML = html;
}

/* ============================================================
   FALLOS: ACTUALIZAR PANEL
   ============================================================ */
function actualizarFallos() {
    const panel = document.getElementById("panel-fallos");
    panel.textContent = `Fallos: ${fallos}/${maxFallos}`;
}

/* ============================================================
   VÍDEO (CON AUTOPLAY + AUDIO)
   ============================================================ */

function mostrarVideo() {
    if (!videoURL) return;

    const modal = document.getElementById("video-modal");
    const video = document.getElementById("video-player");

    video.src = videoURL;

    video.muted = true;
    video.autoplay = true;

    const playPromise = video.play();

    if (playPromise !== undefined) {
        playPromise.then(() => {
            video.muted = false;
            video.play();
        }).catch(() => {
            setTimeout(() => {
                video.muted = false;
                video.play();
            }, 150);
        });
    }

    modal.classList.add("visible");
}

function cerrarVideo() {
    const modal = document.getElementById("video-modal");
    const video = document.getElementById("video-player");

    video.pause();
    video.currentTime = 0;
    video.autoplay = false;

    modal.classList.remove("visible");
}
