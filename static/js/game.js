let citaOriginal = "";
let citaNorm = "";
let autorOriginal = "";
let anioOriginal = "";
let idioma = "";

let aciertosCita = [];
let citaRevelada = false;
let ultimaAdivinada = []; // variantes de la última letra acertada

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
function normalizar(texto) {
    return texto
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toUpperCase();
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("btn-iniciar").addEventListener("click", iniciarJuego);
    document.getElementById("btn-siguiente").addEventListener("click", iniciarJuego);

    document.getElementById("btn-completar-cita").addEventListener("click", () => {
        aciertosCita = citaOriginal.toUpperCase().split("");
        ultimaAdivinada = [];
        mostrarPaneles();
    });

    document.getElementById("btn-revelar").addEventListener("click", toggleRevelar);

    // estado inicial del panel (para animación de entrada)
    const panelCita = document.getElementById("panel-cita");
    panelCita.classList.add("panel-inactivo");

    generarTeclado();
});

/* ======== INICIAR JUEGO ======== */
function iniciarJuego() {
    fetch("/cita")
        .then(r => r.json())
        .then(data => {

            // 🔧 Normalizamos SIEMPRE en frontend
            citaOriginal = data.cita_original || "";
            citaNorm = normalizar(citaOriginal);

            autorOriginal = data.autor_original || "";
            anioOriginal = data.anio_original || "";

            idioma = data.idioma || "";
            document.getElementById("panel-idioma").textContent = idioma.toUpperCase();

            aciertosCita = [];
            citaRevelada = false;
            ultimaAdivinada = [];

            // Mostrar autor y año directamente como pistas
            document.getElementById("panel-autor").textContent = autorOriginal;
            document.getElementById("panel-anio").textContent = anioOriginal;

            resetearTeclado();
            mostrarPaneles();

            // reset botón revelar
            document.getElementById("btn-revelar").textContent = "Revelar cita";

            // animación de expansión del panel
            const panelCita = document.getElementById("panel-cita");
            panelCita.classList.remove("panel-inactivo");
            panelCita.classList.add("panel-activo");
        })
        .catch(err => console.error("Error cargando cita:", err));
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
    if (citaRevelada) return;

    const botones = [...document.querySelectorAll(".tecla")];
    const boton = botones.find(b => b.textContent === letra);
    if (!boton) return;
    boton.disabled = true;

    let acierto = false;

    const variantes = equivalencias[letra] || [letra];

    // CITA
    if (variantes.some(v => citaNorm.includes(normalizar(v)))) {
        variantes.forEach(v => aciertosCita.push(v.toUpperCase()));
        acierto = true;
    }

    boton.classList.add(acierto ? "acierto" : "fallo");

    // guardar qué variantes se acaban de adivinar para animarlas
    ultimaAdivinada = acierto ? variantes.map(v => v.toUpperCase()) : [];

    mostrarPaneles();
}

/* ======== REVELAR / OCULTAR ======== */
function toggleRevelar() {
    citaRevelada = !citaRevelada;

    document.getElementById("btn-revelar").textContent =
        citaRevelada ? "Ocultar cita" : "Revelar cita";

    if (citaRevelada) {
        const cont = document.getElementById("panel-cita");
        cont.textContent = citaOriginal;
        return;
    }

    ultimaAdivinada = [];
    mostrarPaneles();
}

/* ======== MOSTRAR PANELES ======== */
function mostrarPaneles() {
    if (citaRevelada) {
        const cont = document.getElementById("panel-cita");
        cont.textContent = citaOriginal;
        return;
    }

    mostrarPanel("panel-cita", citaOriginal, citaNorm, aciertosCita, ultimaAdivinada);
    ajustarPanel("panel-cita");
}

/* ======== MOSTRAR PANEL INDIVIDUAL (con spans por letra) ======== */
function mostrarPanel(id, original, normalizada, aciertos, ultima) {
    const cont = document.getElementById(id);
    if (!cont || !original) {
        cont.innerHTML = "";
        return;
    }

    // 🔧 Seguridad extra: si algo falla, normalizamos aquí
    normalizada = normalizada || normalizar(original);

    const lineasOriginal = original.split("\n");
    const lineasNorm = normalizada.split("\n");

    let html = "";

    for (let li = 0; li < lineasOriginal.length; li++) {
        const lineaOriginal = lineasOriginal[li];
        const lineaNorm = lineasNorm[li] || "";

        for (let i = 0; i < lineaNorm.length; i++) {
            const letraOriginal = lineaOriginal[i] || " ";
            const letraMayus = letraOriginal.toUpperCase();

            if (letraOriginal === " ") {
                html += `<span class="letra espacio">&nbsp;</span>`;
            }
            else if (!/[A-ZÁÉÍÓÚÑ]/i.test(letraOriginal)) {
                html += `<span class="letra simbolo">${letraOriginal}</span>`;
            }
            else {
                const esAcierto = aciertos.includes(letraMayus);
                const esRecien = esAcierto && ultima.includes(letraMayus);

                const contenido = esAcierto ? letraMayus : "_";
                const clases = ["letra"];
                if (esRecien) clases.push("flip");

                html += `<span class="${clases.join(" ")}">${contenido}</span>`;
            }

            html += " ";
        }

        html += "<br>";
    }

    cont.innerHTML = html;

    // quitar la clase flip después de la animación
    if (ultima.length > 0) {
        setTimeout(() => {
            cont.querySelectorAll(".letra.flip").forEach(span => {
                span.classList.remove("flip");
            });
        }, 400);
    }
}

/* ============================================================
   🔧 AJUSTE AUTOMÁTICO DE TAMAÑO PARA EVITAR PALABRAS ROTAS
   ============================================================ */
function ajustarPanel(id) {
    const el = document.getElementById(id);
    if (!el) return;

    el.style.whiteSpace = "pre";

    let fontSize = parseFloat(getComputedStyle(el).fontSize);
    const minSize = 18;

    while (el.scrollWidth > el.clientWidth && fontSize > minSize) {
        fontSize -= 1;
        el.style.fontSize = fontSize + "px";
    }
}
