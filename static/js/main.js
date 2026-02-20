// ClínicaSalud – main.js

// Animación de aparición al hacer scroll (Intersection Observer)
document.addEventListener('DOMContentLoaded', () => {

  // Highlight link activo en navbar
  const links = document.querySelectorAll('.nav-links a');
  links.forEach(link => {
    if (link.getAttribute('href') === window.location.pathname) {
      link.style.color = 'var(--teal)';
      link.style.fontWeight = '600';
    }
  });

  // Efecto de aparición para cards
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.card').forEach(card => {
    observer.observe(card);
  });

});
