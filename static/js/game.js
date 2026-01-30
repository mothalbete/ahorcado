import {
    initEquiposUI,
    resetFallosTodos,
    actualizarPanelEquipoActivo,
    actualizarFallosPanel,
    resetPalabrasResueltasTodos
} from "./equipos.js";

import { initTeclado } from "./teclado.js";
import {
    initCitaControles,
    nuevaCita,
    jugarLetra,
    toggleRevelar,
    completarCita
} from "./cita.js";

import { initVideoControles, cerrarVideo } from "./video.js";

document.addEventListener("DOMContentLoaded", () => {
    initEquiposUI();
    initTeclado(jugarLetra);
    initCitaControles();
    initVideoControles();

    const btnIniciar = document.getElementById("btn-iniciar");
    const btnSiguiente = document.getElementById("btn-siguiente");
    const btnResetFallos = document.getElementById("btn-reset-fallos");

    btnIniciar.addEventListener("click", () => {
        resetFallosTodos();
        resetPalabrasResueltasTodos();
        actualizarFallosPanel();
        actualizarPanelEquipoActivo();
        nuevaCita();
    });

    btnSiguiente.addEventListener("click", () => {
        resetFallosTodos();
        resetPalabrasResueltasTodos();
        actualizarFallosPanel();
        actualizarPanelEquipoActivo();
        nuevaCita();
    });

    btnResetFallos.addEventListener("click", () => {
        // solo equipo activo
        resetFallosTodos(true);
        actualizarFallosPanel();
        actualizarPanelEquipoActivo();
    });

    // completar cita
    document.getElementById("btn-completar-cita").addEventListener("click", () => {
        completarCita();
    });

    // revelar / ocultar
    document.getElementById("btn-revelar").addEventListener("click", () => {
        toggleRevelar();
    });

    // vídeo: siguiente desde modal
    const btnSiguienteDesdeVideo = document.getElementById("siguiente-desde-video");
    btnSiguienteDesdeVideo.addEventListener("click", () => {
        cerrarVideo();
        resetFallosTodos();
        resetPalabrasResueltasTodos();
        actualizarFallosPanel();
        actualizarPanelEquipoActivo();
        nuevaCita();
    });
});
