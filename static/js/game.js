let letraOriginal = "";
let letraNorm = "";
let tituloOriginal = "";
let tituloNorm = "";
let artistaOriginal = "";
let artistaNorm = "";
let idioma = "";

let aciertosLetra = [];
let aciertosTitulo = [];
let aciertosArtista = [];

/* ======== MAPA DE EQUIVALENCIAS PARA TILDES ======== */
const equivalencias = {
    "A": ["A", "Á"],
    "E": ["E", "É"],
    "I": ["I", "Í"],
    "O": ["O", "Ó"],
    "U": ["U", "Ú"],
    "N": ["N", "Ñ"]
};

/* ======== NORMALIZADOR PARA COMPARAR ======== */
function normalizar(letra) {
    return letra
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toUpperCase();
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("btn-iniciar").addEventListener("click", iniciarJuego);
    document.getElementById("btn-siguiente").addEventListener("click", iniciarJuego);

    document.getElementById("btn-completar-letra").addEventListener("click", () => {
        aciertosLetra = letraOriginal.toUpperCase().split("");
        mostrarPaneles();
    });

    document.getElementById("btn-completar-titulo").addEventListener("click", () => {
        aciertosTitulo = tituloOriginal.toUpperCase().split("");
        mostrarPaneles();
    });

    document.getElementById("btn-completar-artista").addEventListener("click", () => {
        aciertosArtista = artistaOriginal.toUpperCase().split("");
        mostrarPaneles();
    });

    generarTeclado();
});

/* ======== INICIAR JUEGO ======== */
function iniciarJuego() {
    fetch("/cancion")
        .then(r => r.json())
        .then(data => {
            letraOriginal = data.letra_original;
            letraNorm = data.letra_norm;

            tituloOriginal = data.titulo_original;
            tituloNorm = data.titulo_norm;

            artistaOriginal = data.artista_original;
            artistaNorm = data.artista_norm;

            idioma = data.idioma;
            document.getElementById("panel-idioma").textContent = idioma.toUpperCase();

            aciertosLetra = [];
            aciertosTitulo = [];
            aciertosArtista = [];

            resetearTeclado();
            mostrarPaneles();
        })
        .catch(err => console.error("Error cargando canción:", err));
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

/* ======== PROCESAR LETRA PULSADA ======== */
function jugarLetra(letra) {
    const botones = [...document.querySelectorAll(".tecla")];
    const boton = botones.find(b => b.textContent === letra);
    boton.disabled = true;

    let acierto = false;

    const variantes = equivalencias[letra] || [letra];

    // LETRA
    if (variantes.some(v => letraNorm.toUpperCase().includes(normalizar(v)))) {
        variantes.forEach(v => aciertosLetra.push(v));
        acierto = true;
    }

    // TÍTULO
    if (variantes.some(v => tituloNorm.toUpperCase().includes(normalizar(v)))) {
        variantes.forEach(v => aciertosTitulo.push(v));
        acierto = true;
    }

    // ARTISTA
    if (variantes.some(v => artistaNorm.toUpperCase().includes(normalizar(v)))) {
        variantes.forEach(v => aciertosArtista.push(v));
        acierto = true;
    }

    boton.classList.add(acierto ? "acierto" : "fallo");

    mostrarPaneles();
}

/* ======== MOSTRAR PANELES ======== */
function mostrarPaneles() {
    mostrarPanel("panel-letra", letraOriginal, letraNorm, aciertosLetra);
    ajustarPanel("panel-letra");

    mostrarPanel("panel-titulo", tituloOriginal, tituloNorm, aciertosTitulo);
    ajustarPanel("panel-titulo");

    mostrarPanel("panel-artista", artistaOriginal, artistaNorm, aciertosArtista);
    ajustarPanel("panel-artista");
}

/* ======== MOSTRAR PANEL INDIVIDUAL ======== */
function mostrarPanel(id, original, normalizada, aciertos) {
    const cont = document.getElementById(id);

    const lineasOriginal = original.split("\n");
    const lineasNorm = normalizada.split("\n");

    let html = "";

    for (let li = 0; li < lineasOriginal.length; li++) {
        const lineaOriginal = lineasOriginal[li];
        const lineaNorm = lineasNorm[li];

        let lineaHTML = "";

        for (let i = 0; i < lineaNorm.length; i++) {
            const letraOriginal = lineaOriginal[i];
            const letraNorm = lineaNorm[i].toUpperCase();

            if (letraOriginal === " ") {
                lineaHTML += "&nbsp;&nbsp;";
            }
            else if (!/[A-ZÁÉÍÓÚÑ]/i.test(letraOriginal)) {
                lineaHTML += letraOriginal;
            }
            else if (aciertos.includes(letraOriginal.toUpperCase())) {
                lineaHTML += letraOriginal.toUpperCase();
            }
            else {
                lineaHTML += "_";
            }

            lineaHTML += " ";
        }

        html += lineaHTML.trim() + "<br>";
    }

    cont.innerHTML = html;
}

/* ============================================================
   🔧 AJUSTE AUTOMÁTICO DE TAMAÑO PARA EVITAR PALABRAS ROTAS
   ============================================================ */
function ajustarPanel(id) {
    const el = document.getElementById(id);
    if (!el) return;

    // Evita que el navegador envuelva líneas
    el.style.whiteSpace = "pre";

    let fontSize = parseFloat(getComputedStyle(el).fontSize);
    const minSize = 18;

    // Reducir hasta que el contenido quepa sin romper palabras
    while (el.scrollWidth > el.clientWidth && fontSize > minSize) {
        fontSize -= 1;
        el.style.fontSize = fontSize + "px";
    }
}
