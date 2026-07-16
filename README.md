# Edukron — HTML & CSS Blog

A tech blog with learning logs, Python and SQL learning paths, and hands-on assignments.

## Run the site

**No Python, Node, or npm required.** The site is fully static HTML/CSS/JavaScript.

1. Open **`login.html`** in your browser (or start at `index.html` — you will be redirected to login).
2. Sign in with your authorized email and password.

Optionally, use any static file server for a closer-to-production experience (recommended so `data/users.json` is loaded via `fetch`):

```bash
# Examples (pick one):
npx serve .
python -m http.server 3000
# VS Code: "Live Server" extension → Open with Live Server
```

Then open **http://localhost:3000/login.html** (port may vary).

### Credentials

Authorized users are configured in `data/users.json` (email → password). Edit that file (and the matching fallback list in `js/auth.js`) to add or change users. Usernames are email addresses and match case-insensitively; passwords are case-sensitive.

### Logout

Click **Logout** in the nav (on the homepage). This clears `sessionStorage` and returns you to `login.html`.

## Authentication (client-side)

Auth is handled by **`js/auth.js`**:

- On login, credentials are checked against `data/users.json` (or embedded fallback).
- A session is stored in **`sessionStorage`** (`{ username, loggedIn: true }`).
- Protected pages load `auth.js`, which calls `requireAuth()` and redirects to login if needed.

### Security caveat

**This is demo/learning auth only — not secure for production.**

- Passwords are visible in `data/users.json` (and in `js/auth.js` fallback).
- Anyone can view source, skip `auth.js`, or open HTML files directly.
- `sessionStorage` is trivial to forge in DevTools.

Use a real server-side auth system for anything sensitive.

### `file://` vs `http://`

Opening files directly (`file:///...`) may block `fetch("data/users.json")` in some browsers. Login still works via embedded fallback credentials in `auth.js`. For editing users in JSON only, serve the folder over `http://`.

## Site structure

```
index.html                  Homepage (protected)
login.html                  Login page
data/users.json             Authorized user credentials
js/auth.js                  Client-side auth
css/style.css               All styles
blog/                       Tech log posts
learn/python/               45-hour Python sprint
learn/sql/                  SQL learning path
assignments/                Practice exercises
```

## Design

- White background throughout
- Code blocks with syntax-colored comments
- Responsive layout (mobile-friendly)
