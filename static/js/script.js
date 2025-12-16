function showLoading() {
    const loader = document.getElementById("pageLoader");
    const btn = document.getElementById("analyzeBtn");

    // Show loader immediately
    loader.style.display = "flex";

    if (btn) btn.disabled = true;

    // Auto-hide loader after 5 seconds (UX only)
    setTimeout(() => {
        loader.style.display = "none";
    }, 5000); // 5 seconds

    // IMPORTANT: allow form submission
    return true;
}
function showFileName(input) {
    if (input.files && input.files.length > 0) {
        const fileName = input.files[0].name;
        document.getElementById("uploadText").textContent =
            "Selected file: " + fileName;
    }
}
const text = "Resume Analyzer";
const speed = 150;      // typing speed (ms)
const delay = 5000;     // wait time before retyping (ms)

let i = 0;
let element = null;

function typeLogo() {
    if (i < text.length) {
        element.textContent += text.charAt(i);
        i++;
        setTimeout(typeLogo, speed);
    } else {
        // wait 5 seconds, then reset and retype
        setTimeout(() => {
            element.textContent = "";
            i = 0;
            typeLogo();
        }, delay);
    }
}

window.addEventListener("load", () => {
    element = document.getElementById("typing-logo");
    typeLogo();
});