/**
 * Edukron client-side authentication (demo / learning use only).
 *
 * SECURITY: Passwords in data/users.json are visible to anyone. Session is
 * sessionStorage only — pages can be bypassed. Use a real server for production.
 *
 * file:// note: Browsers block fetch() for local JSON files. Login falls back to
 * embedded credentials below. For full users.json support, serve the site over
 * http:// (e.g. `npx serve .`, VS Code Live Server, or `python -m http.server`).
 */
(function () {
  "use strict";

  const SESSION_KEY = "edukron_session";
  const LOGIN_PAGE = "login.html";

  /**
   * Fallback when fetch(users.json) fails (common on file://).
   * Keys are lowercase emails; values are the password string.
   * Keep in sync with data/users.json.
   */
  const EMBEDDED_USERS = {
    "lavanuruaswani34@gmail.com": "Edukron@123",
    "vaibhavchmishra29@outlook.com": "ytrewq29#vaibhav",
    "yuvateja.kulapatti@gmail.com": "Yuva@143@",
    "yarraguntlasainathreddy97@gmail.com": "sainath@1234",
    "shaiksalmanbasha315@gmail.com": "Sksalman0000@",
    "kaarunyaashree12@gmail.com": "kaarunyaa2000",
    "jayalakshmiyenamala25@gmail.com": "jaya@2005",
    "muzakeershaik1122@gmail.com": "Muzakeer@786",
    "nidhibharti578@gmail.com": "Nidhi@5789",
    "punithkumarrm1122@gmail.com": "Sanjana@1122",
    "manoj0250@gmail.com": "M@noj.6468",
    "ruthlessvows@gmail.com": "Amethyst@2003",
    "saivigneshrayavaram@gmail.com": "sairayavaram@",
    "ranganaths@gmail.com": "Ranga@123",
    "lakshminarasimha.in4@gmail.com": "Narasimha_02_",
    "prathyushagorantla9@gmail.com": "datascience09",
    "sudarshan@gmail.com": "Suda@969",
    "shravanreddy17445@gmail.com": "shravanreddy@9959",
    "keerthi@gmail.com": "Kvish@1101",
    "abhishekganganalli@gmail.com": "Abhi2004@",
    "maheguru.k@gmail.com": "Hotspot@123",
    "kartikgugadaddi771@gmail.com": "Kartik@2003@@",
    "likithmnv@gmail.com": "Likith@2003",
    "lakshminarayanareddy310@gmail.com": "Narayana@123",
    "sunilmahto311093@gmail.com": "Bnmhjkl@987",
    "tejaswini@gmail.com": "teju0424",
    "manojdasuri777@gmail.com": "M@noj_777",
    "haribathe9@gmail.com": "H@rish#9911",
    "navyanippatlapalli231@gmail.com": "navya@555",
    "kanupuruharitha@gmail.com": "Haritha@217",
    "kiraniddalagi@gmail.com": "kiran@12082004",
    "suvarnathathikalam2005@gmail.com": "Suvarna#834185",
    "poornareddy2004@gmail.com": "Kadhal8282",
    "prajwalkoladur47@gmail.com": "Prajwal@1111",
    "iddalagikiran24@gmail.com": "kiran@12082004",
    "sanachakravardhan@gmail.com": "Sanachakri@1234",
    "sarathreddy.in@gmail.com": "sarathedukron",
    "navitha42135@gmail.com": "Navi@2004",
    "yeddulajayanthkumarreddy@gmail.com": "7890@jay",
    "deepaktech1920@gmail.com": "Deepaktech#2020",
    "ikramdoti01@gmail.com": "Ikram@1997",
    "chaitujagan2005@gmail.com": "ChaituJagan@8919189194",
    "shaikzaifahamed27@gmail.com": "shaik@8861371323",
    "reddy6301shashe@gmail.com": "Shashe@6301",
    "bathuluripavanirathna@gmail.com": "Pavani@2004",
    "leelapavanroyal@gmail.com": "LeelaRoyal@1218",
    "pavankumar.de@gmail.com": "August1331*",
    "amrosejahan@gmail.com": "aliali786",
    "prabhapalagiri098@gmail.com": "Prabha@255198",
    "pavankumarb0225@gmail.com": "Pavan@0225",
    "e.pavithra@gmail.com": "Pavi@2004",
    "charithagudipati217@gmail.com": "cherry7799022",
    "pranuk050@gmail.com": "Hanuman@7890",
    "dasumunemma@gmail.com": "munemma@2026",
    "pavithraeraganaboyina0@gmail.com": "Pavi@2004",
    "arjunanav03@gmail.com": "KRATOS~9600",
    "gurramkonduramesh02@gmail.com": "Lakshmi@7931",
    "yuvi.ds2050@gmail.com": "Yuvi@2050",
    "doddiramya@gmail.com": "Doddiramya1025",
    "gayatri.web2026@gmail.com": "Gayatri@2311",
    "bhargavikalluri18@gmail.com": "Livanshi@102025",
    "nafimunnisa.89@gmail.com": "Aliza@2020",
    "sudarshanr@gmail.com": "Suda9699",
    "ranganaths0505@gmail.com": "Edukron@123",
    "rohithkumarmalle7@gmail.com": "Rohith@123",
    "srijamopuru699@gmail.com": "Srija@699",
    "amadhu1803@gmail.com": "Madhua@1803",
    "manojkumargudiyatham8@gmail.com": "Manoj@143",
    "shivamanohar@gmail.com": "Siva@630110",
    "nandini@gmail.com": "Nandi$789",
    "kushalgowda@gmail.com": "Kushal@1924",
    "yashwanth2026@gmail.com": "Yash@2026",
    "durgaprasadallada2005@gmail.com": "Prasad23",
    "k_vindya@gmail.com": "Tiger@123",
    "khan085796@gmail.com": "Edukron@123",
    "abhishekganganalli1902@gmail.com": "Edukron@123",
    "mamudurujagadeesh7@gmail.com": "Edukron@123",
    "munemmadasu@gmail.com": "Edukron@123",
    "amrosejahan98@gmail.com": "Edukron@123",
    "keerthivishnu1402@gmail.com": "Edukron@123",
    "yarraguntlasainathreddy122@gmail.com": "Edukron@123",
    "ravifeaturetechinnovation@gmail.com": "Edukron@123",
    "sivaprasad.rvm@gmail.com": "Edukron@123",
    "aswaninandu52@gmail.com": "Edukron@123",
    "bharatinidhi247@gmail.com": "Edukron@123",
    "msr48@live.com": "Edukron@123",
    "anilkumarm6366@gmail.com": "Edukron@123",
    "leelapavankumar16@gmail.com": "Edukron@123",
    "bhanuprakash.bhavanam1@gmail.com": "Edukron@123",
    "prabhaspalagiri119@gmail.com": "Edukron@123",
    "harithakanupuru636@gmail.com": "Edukron@123",
    "deepak1920p@gmail.com": "Edukron@123",
    "doddiramya10@gmail.com": "Edukron@123",
    "ramyays3098@gmail.com": "Edukron@123",
    "afrozsyed18103@gmail.com": "Edukron@123",
    "pavanpillar.de@gmail.com": "Edukron@123",
    "rahidisthif@gmail.com": "Edukron@123",
  };

  function getScriptEl() {
    return (
      document.currentScript ||
      document.querySelector('script[src*="auth.js"]')
    );
  }

  /** Site root URL derived from this script's resolved location. */
  function getSiteRoot() {
    const script = getScriptEl();
    if (script?.src) {
      return new URL("../", script.src).href;
    }
    const parts = window.location.pathname.split("/").filter(Boolean);
    if (parts.length && /\.html?$/i.test(parts[parts.length - 1])) {
      parts.pop();
    }
    const prefix = parts.length ? "../".repeat(parts.length) : "./";
    return new URL(prefix, window.location.href).href;
  }

  function url(path) {
    return new URL(path, getSiteRoot()).href;
  }

  function getSession() {
    try {
      const raw = sessionStorage.getItem(SESSION_KEY);
      if (!raw) return null;
      const session = JSON.parse(raw);
      return session?.loggedIn ? session : null;
    } catch {
      return null;
    }
  }

  function setSession(username) {
    sessionStorage.setItem(
      SESSION_KEY,
      JSON.stringify({ username, loggedIn: true })
    );
  }

  function isLoggedIn() {
    return getSession() !== null;
  }

  function isLoginPage() {
    const page = getScriptEl()?.dataset?.page;
    if (page === "login") return true;
    return /login\.html$/i.test(window.location.pathname);
  }

  async function loadUsers() {
    try {
      const res = await fetch(url("data/users.json"));
      if (!res.ok) throw new Error("users.json not found");
      const data = await res.json();
      return data.users || data;
    } catch {
      return { ...EMBEDDED_USERS };
    }
  }

  /**
   * Login with email (case-insensitive) and password (case-sensitive).
   * A user entry's value may be a single password or an array of accepted
   * passwords (used when the same email was registered more than once).
   */
  async function login(email, password) {
    const users = await loadUsers();
    const normalized = email.trim().toLowerCase();

    for (const [key, value] of Object.entries(users)) {
      if (key.toLowerCase() !== normalized) continue;
      const passwords = Array.isArray(value) ? value : [value];
      if (passwords.includes(password)) {
        setSession(normalized);
        return { ok: true, username: normalized };
      }
    }
    return { ok: false };
  }

  function logout() {
    sessionStorage.removeItem(SESSION_KEY);
    window.location.href = url(LOGIN_PAGE);
  }

  function requireAuth() {
    if (isLoggedIn()) return true;
    const redirect = encodeURIComponent(
      window.location.pathname + window.location.search + window.location.hash
    );
    window.location.replace(url(LOGIN_PAGE) + "?redirect=" + redirect);
    return false;
  }

  function getRedirectTarget() {
    const params = new URLSearchParams(window.location.search);
    const target = params.get("redirect");
    if (!target) return url("index.html");
    const decoded = decodeURIComponent(target);
    if (/^https?:\/\//i.test(decoded) || decoded.startsWith("//")) {
      return url("index.html");
    }
    try {
      return new URL(decoded, getSiteRoot()).href;
    } catch {
      return url("index.html");
    }
  }

  function wireLogoutLinks() {
    document.querySelectorAll('a[href="/logout"], a[href$="/logout"]').forEach((link) => {
      link.addEventListener("click", (e) => {
        e.preventDefault();
        logout();
      });
      link.setAttribute("href", "#");
      link.classList.add("auth-logout");
    });
  }

  function initLoginPage() {
    const form = document.getElementById("loginForm");
    const errorEl = document.getElementById("error");
    if (!form) return;

    if (isLoggedIn()) {
      window.location.replace(getRedirectTarget());
      return;
    }

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      errorEl?.classList.remove("show");
      if (errorEl) errorEl.textContent = "Invalid email or password";

      const username = document.getElementById("username")?.value ?? "";
      const password = document.getElementById("password")?.value ?? "";

      const result = await login(username, password);
      if (result.ok) {
        window.location.href = getRedirectTarget();
      } else {
        errorEl?.classList.add("show");
      }
    });
  }

  function init() {
    if (isLoginPage()) {
      initLoginPage();
      return;
    }
    requireAuth();
    wireLogoutLinks();
  }

  window.EdukronAuth = {
    login,
    logout,
    requireAuth,
    isLoggedIn,
    getSession,
    getSiteRoot,
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
