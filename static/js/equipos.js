export const maxFallos = 3;

const equipos = {
    1: { nombre: "Equipo 1", fallos: 0, palabrasResueltas: [], citasGanadas: 0 },
    2: { nombre: "Equipo 2", fallos: 0, palabrasResueltas: [], citasGanadas: 0 },
    3: { nombre: "Equipo 3", fallos: 0, palabrasResueltas: [], citasGanadas: 0 },
    4: { nombre: "Equipo 4", fallos: 0, palabrasResueltas: [], citasGanadas: 0 }
};

let equipoActivo = 1;
let ultimoEquipoID = 4;

export function getEquipoActivoId() {
    return equipoActivo;
}

export function getEquipoActivo() {
    return equipos[equipoActivo];
}

export function getPalabrasResueltasActivo() {
    return equipos[equipoActivo].palabrasResueltas;
}

export function setPalabraResueltaActivo(index) {
    equipos[equipoActivo].palabrasResueltas[index] = true;
}

export function incCitasGanadasActivo() {
    equipos[equipoActivo].citasGanadas++;
}

export function incFallosActivo() {
    equipos[equipoActivo].fallos++;
}

export function resetFallosTodos(soloActivo = false) {
    if (soloActivo) {
        equipos[equipoActivo].fallos = 0;
        return;
    }
    Object.keys(equipos).forEach(id => {
        equipos[id].fallos = 0;
    });
}

export function resetPalabrasResueltasTodos() {
    Object.keys(equipos).forEach(id => {
        equipos[id].palabrasResueltas = [];
    });
}

export function actualizarFallosPanel() {
    const fallos = equipos[equipoActivo].fallos;
    const panel = document.getElementById("panel-fallos");
    if (panel) {
        panel.textContent = `Fallos: ${fallos}/${maxFallos}`;
    }
}

export function actualizarPanelEquipoActivo() {
    const eq = equipos[equipoActivo];
    const panel = document.getElementById("panel-equipo-activo");
    if (!panel) return;

    document.getElementById("equipo-activo-nombre").textContent = eq.nombre;
    document.getElementById("equipo-activo-fallos").textContent = eq.fallos;
    document.getElementById("equipo-activo-ganadas").textContent = eq.citasGanadas;

    panel.style.display = "block";
}

export function initEquiposUI() {
    activarSelectorEquipos();
    activarBotonAgregarEquipo();
    activarBotonRenombrarEquipo();
    actualizarPanelEquipoActivo();
    actualizarFallosPanel();
}

function activarSelectorEquipos() {
    document.querySelectorAll(".btn-equipo").forEach(btn => {
        btn.onclick = () => {
            document.querySelectorAll(".btn-equipo").forEach(b => b.classList.remove("activo"));
            btn.classList.add("activo");

            equipoActivo = parseInt(btn.dataset.equipo);
            actualizarFallosPanel();
            actualizarPanelEquipoActivo();
        };
    });
}

function activarBotonAgregarEquipo() {
    const selector = document.getElementById("selector-equipos");
    const btnAdd = selector.querySelector(".btn-equipo-add");

    btnAdd.onclick = () => {
        ultimoEquipoID++;
        const id = ultimoEquipoID;

        equipos[id] = {
            nombre: `Equipo ${id}`,
            fallos: 0,
            palabrasResueltas: [],
            citasGanadas: 0
        };

        const btn = document.createElement("button");
        btn.classList.add("btn-equipo");
        btn.dataset.equipo = id;
        btn.innerHTML = `
            <span class="nombre-equipo">${equipos[id].nombre}</span>
            <span class="rename-equipo" data-equipo="${id}">✏️</span>
        `;

        selector.insertBefore(btn, btnAdd);

        activarSelectorEquipos();
        activarBotonRenombrarEquipo();
    };
}

function activarBotonRenombrarEquipo() {
    document.querySelectorAll(".rename-equipo").forEach(btn => {
        btn.onclick = () => {
            const id = parseInt(btn.dataset.equipo);
            const nuevoNombre = prompt("Nuevo nombre del equipo:", equipos[id].nombre);

            if (nuevoNombre && nuevoNombre.trim() !== "") {
                equipos[id].nombre = nuevoNombre.trim();

                const tab = document.querySelector(
                    `.btn-equipo[data-equipo="${id}"] .nombre-equipo`
                );
                if (tab) tab.textContent = equipos[id].nombre;

                if (equipoActivo === id) {
                    actualizarPanelEquipoActivo();
                }
            }
        };
    });
}
