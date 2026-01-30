import {
    getPalabrasResueltasActivo,
    setPalabraResueltaActivo,
    incCitasGanadasActivo,
    incFallosActivo,
    actualizarFallosPanel,
    actualizarPanelEquipoActivo
} from "./equipos.js";

import { resetearTeclado } from "./teclado.js";
import { mostrarVideo } from "./video.js";

let citaOriginal = "";
let citaNorm = "";
let autorOriginal = "";
let anioOriginal = "";
let idioma = "";
let videoURL = null;

let aciertosCita = [];
let citaRevelada = false;
let ultimaAdivinada = [];

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

export function initCitaControles() {
    const btnRevelar = document.getElementById("btn-revelar");
    if (btnRevelar) {
        btnRevelar.textContent = "Revelar cita";
    }
}

export function nuevaCita() {
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

            resetearTeclado();
            mostrarPaneles();

            const btnRevelar = document.getElementById("btn-revelar");
            if (btnRevelar) btnRevelar.textContent = "Revelar cita";
        });
}

export function jugarLetra(letra) {
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

    if (!acierto) {
        incFallosActivo();
        actualizarFallosPanel();
        actualizarPanelEquipoActivo();
    }

    mostrarPaneles();
}

export function toggleRevelar() {
    citaRevelada = !citaRevelada;

    const btnRevelar = document.getElementById("btn-revelar");
    if (btnRevelar) {
        btnRevelar.textContent = citaRevelada ? "Ocultar cita" : "Revelar cita";
    }

    if (citaRevelada) {
        document.getElementById("panel-cita").textContent = citaOriginal;
        return;
    }

    ultimaAdivinada = [];
    mostrarPaneles();
}

export function completarCita() {
    if (!citaOriginal) return;

    aciertosCita = citaOriginal.toUpperCase().split("");
    ultimaAdivinada = [];
    incCitasGanadasActivo();
    actualizarPanelEquipoActivo();
    mostrarPaneles();
    mostrarVideo(videoURL);
}

function mostrarPaneles() {
    if (citaRevelada) {
        document.getElementById("panel-cita").textContent = citaOriginal;
        return;
    }

    mostrarPanel("panel-cita", citaOriginal, citaNorm, aciertosCita, ultimaAdivinada);
}

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
    let globalIndex = 0;

    const palabrasResueltas = getPalabrasResueltasActivo();

    for (let li = 0; li < lineasOriginal.length; li++) {
        const palabrasOriginal = lineasOriginal[li].split(" ");
        const palabrasNorm = lineasNorm[li].split(" ");

        palabrasOriginal.forEach((palabraOriginal, idx) => {
            const palabraNorm = palabrasNorm[idx] || "";
            const estabaResuelta = palabrasResueltas[globalIndex] === true;

            html += `<span class="palabra ${estabaResuelta ? "palabra-resuelta" : ""}" data-index="${globalIndex}">`;

            for (let i = 0; i < palabraNorm.length; i++) {
                const letraOriginal = palabraOriginal[i] || " ";
                const letraMayus = letraOriginal.toUpperCase();

                if (!/[A-ZÁÉÍÓÚÑ]/i.test(letraOriginal)) {
                    html += `<span class="letra simbolo" data-original="${letraOriginal}">${letraOriginal}</span>`;
                } else {
                    let contenido = "";
                    let clases = ["letra"];

                    if (estabaResuelta) {
                        contenido = letraMayus;
                        clases.push("acertada");
                    } else {
                        const esAcierto = aciertos.includes(letraMayus);
                        const esRecien = esAcierto && ultima.includes(letraMayus);

                        contenido = esAcierto ? letraMayus : "";
                        if (esAcierto) clases.push("acertada");
                        if (esRecien) clases.push("animar");
                    }

                    html += `<span class="${clases.join(" ")}" data-original="${letraOriginal}">${contenido}</span>`;
                }
            }

            html += `<button class="btn-resolver-palabra" ${estabaResuelta ? "disabled" : ""}>Resolver</button>`;
            html += `</span> `;

            globalIndex++;
        });

        html += "<br>";
    }

    cont.innerHTML = html;

    activarBotonesResolver();
}

function activarBotonesResolver() {
    document.querySelectorAll(".btn-resolver-palabra").forEach(btn => {
        btn.onclick = () => {
            const palabra = btn.closest(".palabra");
            resolverPalabraManual(palabra);
        };
    });
}

function resolverPalabraManual(palabraElem) {
    const index = parseInt(palabraElem.dataset.index);
    setPalabraResueltaActivo(index);

    const letras = palabraElem.querySelectorAll(".letra:not(.simbolo)");

    letras.forEach(l => {
        const original = l.dataset.original || "";
        l.textContent = original.toUpperCase();
        l.classList.add("acertada");
    });

    palabraElem.classList.add("palabra-resuelta");

    const btn = palabraElem.querySelector(".btn-resolver-palabra");
    if (btn) btn.disabled = true;
}
