const mainColumn = document.getElementById("main-col");
const sidebarColumn = document.getElementById("sidebar-col");

document.addEventListener("DOMContentLoaded", () => {
    if(path === "main.displayData") {
        mainColumn.classList.remove("col-md-8");
        mainColumn.classList.add("col");
        sidebarColumn.classList.add("d-none");
    }
});
