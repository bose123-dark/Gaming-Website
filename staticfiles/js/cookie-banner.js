/**
 * Cookie Consent Banner Script - Dark Game
 * Handles injection and logic for the premium cookie banner.
 */

document.addEventListener("DOMContentLoaded", function() {
    const CONSENT_KEY = 'dark_game_cookie_consent';
    
    // Check if user has already made a choice
    const hasConsent = localStorage.getItem(CONSENT_KEY);
    
    if (!hasConsent) {
        injectBanner();
    }

    function injectBanner() {
        // Create HTML structure
        const banner = document.createElement('div');
        banner.className = 'cookie-consent-overlay';
        banner.innerHTML = `
            <div class="cookie-content">
                <div class="cookie-icon"><i class="fa fa-shield"></i></div>
                <div class="cookie-text">
                    <h4>Neural Link Cookies</h4>
                    <p>We use cookies to enhance your gaming experience, analyze traffic, and personalize your digital journey across the multiverse.</p>
                </div>
            </div>
            <div class="cookie-actions">
                <button class="cookie-btn btn-decline" id="cookie-decline">Reject All</button>
                <button class="cookie-btn btn-accept" id="cookie-accept">Accept Protocol</button>
            </div>
        `;
        
        document.body.appendChild(banner);
        
        // Trigger animation
        setTimeout(() => {
            banner.classList.add('show');
        }, 1000);
        
        // Event Listeners
        document.getElementById('cookie-accept').addEventListener('click', () => {
            saveChoice('accepted');
        });
        
        document.getElementById('cookie-decline').addEventListener('click', () => {
            saveChoice('declined');
        });
    }

    function saveChoice(status) {
        localStorage.setItem(CONSENT_KEY, status);
        const banner = document.querySelector('.cookie-consent-overlay');
        
        if (banner) {
            banner.classList.remove('show');
            setTimeout(() => {
                banner.remove();
            }, 800);
        }
        
        console.log(`Cookie Protocol: ${status.toUpperCase()}`);
    }
});
