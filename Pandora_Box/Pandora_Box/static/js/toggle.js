document.addEventListener("DOMContentLoaded", function() {
    var dropdown = document.querySelector('.dropdown');
    var dropdownMenu = dropdown.querySelector('.dropdown-menu');
  
    // Show dropdown menu when hovering over the dropdown or its options
    dropdown.addEventListener('mouseenter', function() {
      dropdownMenu.style.display = 'block';
    });
  
    // Hide dropdown menu when not hovering over the dropdown or its options
    dropdown.addEventListener('mouseleave', function(event) {
      if (!dropdown.contains(event.relatedTarget)) {
        dropdownMenu.style.display = 'none';
      }
    });
  
    // Close dropdown on click outside
    document.addEventListener('click', function(event) {
      if (!dropdown.contains(event.target)) {
        dropdownMenu.style.display = 'none';
      }
    });
  });
  