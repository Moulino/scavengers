document.addEventListener('DOMContentLoaded', function() {
    // Gestion du bouton de retour en haut et du logo
    const scrollBtn = document.getElementById('scrollTopBtn');
    const logoLink = document.querySelector('.logo-link');
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollBtn.classList.add('visible');
        } else {
            scrollBtn.classList.remove('visible');
        }
    });

    // Fonction de défilement vers le haut
    function scrollToTop(duration) {
        const start = window.pageYOffset;
        const startTime = 'now' in window.performance ? performance.now() : new Date().getTime();

        function scroll() {
            const now = 'now' in window.performance ? performance.now() : new Date().getTime();
            const time = Math.min(1, ((now - startTime) / duration));
            const easeInOutQuart = t => t < .5 ? 8 * t * t * t * t : 1 - 8 * (--t) * t * t * t;
            
            window.scrollTo(0, start * (1 - easeInOutQuart(time)));

            if (time < 1) {
                requestAnimationFrame(scroll);
            }
        }

        requestAnimationFrame(scroll);
    }

    // Défilement fluide pour les liens du menu avec offset
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') {
                // Pour le logo et le bouton de retour en haut
                scrollToTop(2000);
            } else {
                const targetElement = document.querySelector(targetId);
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - 30;
                const startPosition = window.pageYOffset;
                const distance = targetPosition - startPosition;
                const duration = 2000;
                const startTime = 'now' in window.performance ? performance.now() : new Date().getTime();

                function scrollToSection() {
                    const now = 'now' in window.performance ? performance.now() : new Date().getTime();
                    const time = Math.min(1, ((now - startTime) / duration));
                    const easeInOutQuart = t => t < .5 ? 8 * t * t * t * t : 1 - 8 * (--t) * t * t * t;
                    
                    window.scrollTo(0, startPosition + (distance * easeInOutQuart(time)));

                    if (time < 1) {
                        requestAnimationFrame(scrollToSection);
                    }
                }

                requestAnimationFrame(scrollToSection);
            }
        });
    });

    // Utiliser la même fonction pour le bouton de retour en haut
    scrollBtn.addEventListener('click', function(e) {
        e.preventDefault();
        scrollToTop(1500);
    });

    // Ajout de la gestion du menu burger
    const burgerMenu = document.querySelector('.burger-menu');
    const navLinks = document.querySelector('.nav-links');
    const navLinksItems = document.querySelectorAll('.nav-links a');

    burgerMenu.addEventListener('click', function() {
        burgerMenu.classList.toggle('active');
        navLinks.classList.toggle('active');
        document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
    });

    // Fermer le menu lors du clic sur un lien
    navLinksItems.forEach(link => {
        link.addEventListener('click', function() {
            burgerMenu.classList.remove('active');
            navLinks.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
});