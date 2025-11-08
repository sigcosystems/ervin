// utils.js - Funciones de utilidad globales

// Mostrar notificación toast
function mostrarNotificacion(mensaje, tipo = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${tipo}`;
    toast.textContent = mensaje;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('show');
    }, 100);
    
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Formatear precio
function formatearPrecio(precio) {
    return `S/${precio.toFixed(2)}`;
}

// Validar DNI peruano
function validarDNI(dni) {
    return /^\d{8}$/.test(dni);
}

// Validar teléfono peruano
function validarTelefono(telefono) {
    return /^9\d{8}$/.test(telefono);
}

// Debounce para búsquedas
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Mostrar/ocultar loading spinner
function toggleLoading(show) {
    let spinner = document.getElementById('global-spinner');
    
    if (!spinner) {
        spinner = document.createElement('div');
        spinner.id = 'global-spinner';
        spinner.className = 'spinner-overlay';
        spinner.innerHTML = '<div class="spinner"></div>';
        document.body.appendChild(spinner);
    }
    
    spinner.style.display = show ? 'flex' : 'none';
}

// Export para usar en otros archivos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        mostrarNotificacion,
        formatearPrecio,
        validarDNI,
        validarTelefono,
        debounce,
        toggleLoading
    };
}