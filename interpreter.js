function runBrainfuck(code) {
    const tape = new Uint8Array(30000);
    let ptr = 0, output = '', i = 0;
    const loopStack = [];

    while (i < code.length) {
        switch (code[i]) {
            case '>': ptr++; break;
            case '<': ptr--; break;
            case '+': tape[ptr]++; break;
            case '-': tape[ptr]--; break;
            case '.': output += String.fromCharCode(tape[ptr]); break;
            
            case '[':
                if (tape[ptr] === 0) {
                    let open = 1;
                    while (open) {
                        i++;
                        if (code[i] === '[') open++;
                        if (code[i] === ']') open--;
                    }
                } else loopStack.push(i);
                break;

            case ']':
                if (tape[ptr] !== 0) i = loopStack[loopStack.length - 1]
                else loopStack.pop();
                break;
    }
    i++;
    }
    return output;
}

const routes = {
    "/": "/bf/home.bf"
};

const pageCache = {};

async function loadBF(path) {
    const res = await fetch(path);
    if (!res.ok) {
        return '<h1>404</h1><p>Page not found</p>';
    }
    return await res.text();
}

async function loadPage(path) {
    const route = routes[path] || routes["/"];

    if (!pageCache[path]) {
        const bfCode = await loadBF(route);
        // Interpret BrainFuck and generate HTML output
        pageCache[path] = runBrainfuck(bfCode);
    }

    const app = document.getElementById("app");
    app.innerHTML = pageCache[path];
}

function navigate(path) {
    history.pushState({}, "", path);
    loadPage(path);
}

window.addEventListener("popstate", () => {
    loadPage(location.pathname);   
});

document.addEventListener("click", (e) => {
    const link = e.target.closest("a");

    if (link && link.hasAttribute("data-link")) {
        e.preventDefault();
        const path = link.getAttribute("href");
        navigate(path);
    }
});

document.addEventListener("DOMContentLoaded", () => {
    loadPage(location.pathname);
});