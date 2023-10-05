document.addEventListener("DOMContentLoaded", function() {
    // Найти все элементы с классом "dropdown"
    var dropdowns = document.querySelectorAll(".dropdown");

    // Обойти найденные элементы и добавить обработчики событий
    dropdowns.forEach(function(dropdown) {
        // Наведение мыши
        dropdown.addEventListener("mouseenter", function() {
            var dropdownContent = this.querySelector(".dropdown-content");
            dropdownContent.style.display = "block";
        });

        // Уход мыши
        dropdown.addEventListener("mouseleave", function() {
            var dropdownContent = this.querySelector(".dropdown-content");
            dropdownContent.style.display = "none";
        });
    });
});