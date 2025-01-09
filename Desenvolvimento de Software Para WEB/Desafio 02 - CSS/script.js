// https://github.com/DenilsonRabelo/API-Receitas
const API_URL = "https://api-receitas-pi.vercel.app/receitas/todas";

async function fetchReceitas() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error("Erro ao buscar receitas");
        }
        const receitas = await response.json();
        renderReceitas(receitas);
    } catch (error) {
        console.error("Erro:", error);
        document.getElementById("receitas").innerHTML = "<p>Não foi possível carregar as receitas.</p>";
    }
}

function renderReceitas(receitas) {
    const container = document.getElementById("receitas");
    container.innerHTML = "";

    receitas.forEach(receita => {
        const card = document.createElement("div");
        card.className = "card";

        card.innerHTML = `
            <h2>${receita.receita}</h2>
            <div>
                <img src="${receita.link_imagem}" alt="${receita.receita}">
                <p><strong>Ingredientes:</strong> ${receita.ingredientes}</p>
                <p><strong>Modo de preparo:</strong> ${receita.modo_preparo}</p>
            </div>
        `;

        container.appendChild(card);
    });
}

document.addEventListener("DOMContentLoaded", fetchReceitas);
