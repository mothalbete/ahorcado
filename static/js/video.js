let videoURLActual = null;

export function mostrarVideo(url) {
    if (!url) return;
    videoURLActual = url;

    const modal = document.getElementById("video-modal");
    const video = document.getElementById("video-player");

    video.src = videoURLActual;
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

export function cerrarVideo() {
    const modal = document.getElementById("video-modal");
    const video = document.getElementById("video-player");

    video.pause();
    video.currentTime = 0;
    video.autoplay = false;

    modal.classList.remove("visible");
}

export function initVideoControles() {
    const btnCerrar = document.getElementById("cerrar-video");
    if (btnCerrar) {
        btnCerrar.onclick = () => cerrarVideo();
    }
}
