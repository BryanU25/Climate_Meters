function ObtenerCSRFToken() {
    const cookieName = "_csrf_token=";
    const decodedCookies = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookies.split(';');

    for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i].trim();
        if (cookie.indexOf(cookieName) === 0) {
            return cookie.substring(cookieName.length, cookie.length);
        }
    }

    return null; // Devuelve null si no se encuentra la cookie
}
