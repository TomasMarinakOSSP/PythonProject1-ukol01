document.addEventListener('DOMContentLoaded', function() {
    // Update current time
    function updateTime() {
        const now = new Date();
        const timeElement = document.getElementById('current-time');
        if (timeElement) {
            timeElement.textContent = now.toLocaleTimeString() + ' ' + now.toLocaleDateString();
        }
    }

    setInterval(updateTime, 1000);
    updateTime();

    // Toggle sidebar on mobile
    const sidebarToggle = document.querySelector('.sidebar-toggle');
    const sidebar = document.querySelector('.admin-sidebar');

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('active');
        });
    }

    // Close flash messages when clicking the close button
    document.querySelectorAll('.flash-close').forEach(button => {
        button.addEventListener('click', function() {
            this.closest('.flash-message').style.display = 'none';
        });
    });

    // Auto-close flash messages after 5 seconds
    setTimeout(() => {
        document.querySelectorAll('.flash-message').forEach(message => {
            message.style.display = 'none';
        });
    }, 5000);
});