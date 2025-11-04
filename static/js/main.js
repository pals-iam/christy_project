// Main JavaScript for Christian Author Website

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Scroll reveal animation
    const scrollRevealElements = document.querySelectorAll('.scroll-reveal, .pillar-card, .theme-card, .testimonial-card, .verse-item');
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    scrollRevealElements.forEach(element => {
        element.classList.add('scroll-reveal');
        observer.observe(element);
    });

    // Contact form handling
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formMessage = document.getElementById('formMessage');
            const formData = new FormData(this);
            
            // Get CSRF token
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            
            // Show loading state
            const submitButton = this.querySelector('button[type="submit"]');
            const originalButtonText = submitButton.innerHTML;
            submitButton.disabled = true;
            submitButton.innerHTML = '<i class="bi bi-hourglass-split me-2"></i>Sending...';
            
            // Simulate form submission (replace with actual backend endpoint)
            setTimeout(() => {
                formMessage.innerHTML = `
                    <div class="alert alert-success alert-dismissible fade show" role="alert">
                        <i class="bi bi-check-circle-fill me-2"></i>
                        <strong>Thank you!</strong> Your message has been sent. I'll get back to you soon. God bless you!
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                `;
                contactForm.reset();
                submitButton.disabled = false;
                submitButton.innerHTML = originalButtonText;
                
                // Scroll to message
                formMessage.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }, 1500);
            
            // Note: In production, replace with actual AJAX call to Django view
            /*
            fetch('/contact/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams(formData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    formMessage.innerHTML = `
                        <div class="alert alert-success alert-dismissible fade show" role="alert">
                            <i class="bi bi-check-circle-fill me-2"></i>
                            <strong>Thank you!</strong> Your message has been sent. I'll get back to you soon. God bless you!
                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>
                    `;
                    contactForm.reset();
                } else {
                    formMessage.innerHTML = `
                        <div class="alert alert-danger alert-dismissible fade show" role="alert">
                            <i class="bi bi-exclamation-triangle-fill me-2"></i>
                            <strong>Oops!</strong> Something went wrong. Please try again or contact me directly.
                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>
                    `;
                }
                submitButton.disabled = false;
                submitButton.innerHTML = originalButtonText;
            })
            .catch(error => {
                formMessage.innerHTML = `
                    <div class="alert alert-danger alert-dismissible fade show" role="alert">
                        <i class="bi bi-exclamation-triangle-fill me-2"></i>
                        <strong>Error!</strong> Please try again later or contact me directly.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                `;
                submitButton.disabled = false;
                submitButton.innerHTML = originalButtonText;
            });
            */
        });
    }

    // Navbar background on scroll
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });

    // Add fade-in animation to page load
    document.body.classList.add('fade-in');

    // Verse text animation on scroll
    const verseBoxes = document.querySelectorAll('.verse-box, .verse-highlight-box');
    verseBoxes.forEach(box => {
        box.classList.add('scroll-reveal');
        observer.observe(box);
    });

    // Smooth hover effects for book covers
    const bookCovers = document.querySelectorAll('.hero-book-cover, .main-book-cover, .book-cover-preview');
    bookCovers.forEach(cover => {
        cover.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
        });
    });

    // Add subtle animation to icons
    const icons = document.querySelectorAll('.pillar-icon, .theme-icon, .audience-icon, .testimonial-icon');
    icons.forEach(icon => {
        icon.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1) rotate(5deg)';
            this.style.transition = 'transform 0.3s ease';
        });
        icon.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    });

    // Parallax effect for hero section (subtle)
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            if (scrolled < heroSection.offsetHeight) {
                heroSection.style.transform = `translateY(${scrolled * 0.5}px)`;
            }
        });
    }

    // Console message
    console.log('%c✝ Welcome to Christiana Catherine White\'s Website ✝', 'color: #8B6F7E; font-size: 20px; font-weight: bold;');
    console.log('%c"Victory in His Blood" - A journey of faith, hope, and redemption', 'color: #6B6B6B; font-size: 14px;');
});

