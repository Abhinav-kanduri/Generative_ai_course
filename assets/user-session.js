(function () {
  const storageKey = "generativeAiCourseUser";
  const loginPage = "login.html";
  const configuredLoginUrl = document.body.dataset.loginUrl || loginPage;

  function loginUrl() {
    return configuredLoginUrl;
  }

  function readUser() {
    try {
      const value = window.localStorage.getItem(storageKey);
      return value ? JSON.parse(value) : null;
    } catch (_error) {
      return null;
    }
  }

  function saveUser(user) {
    window.localStorage.setItem(storageKey, JSON.stringify(user));
  }

  function clearUser() {
    window.localStorage.removeItem(storageKey);
  }

  function isLoginPage() {
    return window.location.pathname.endsWith("/" + loginPage) || window.location.pathname.endsWith(loginPage);
  }

  function redirectToLogin() {
    const next = window.location.href;
    window.location.href = loginUrl() + "?next=" + encodeURIComponent(next);
  }

  function redirectAfterLogin() {
    const params = new URLSearchParams(window.location.search);
    const next = params.get("next") || "index.html";
    window.location.href = next;
  }

  const user = readUser();

  if (document.body.dataset.requireLogin === "true" && !user && !isLoginPage()) {
    redirectToLogin();
    return;
  }

  const form = document.querySelector("[data-login-form]");
  if (form) {
    if (user) {
      redirectAfterLogin();
      return;
    }

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      const formData = new FormData(form);
      const name = String(formData.get("name") || "").trim();
      const email = String(formData.get("email") || "").trim().toLowerCase();

      if (!name || !email) {
        return;
      }

      saveUser({ name, email, loggedInAt: new Date().toISOString() });
      redirectAfterLogin();
    });
  }

  const chip = document.querySelector("[data-user-chip]");
  if (chip && user) {
    chip.textContent = user.name + " (" + user.email + ")";
    chip.hidden = false;
  }

  const logoutButton = document.querySelector("[data-logout]");
  if (logoutButton && user) {
    logoutButton.hidden = false;
    logoutButton.addEventListener("click", function () {
      clearUser();
      redirectToLogin();
    });
  }
})();
