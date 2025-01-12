const apiKey = '5796abbde9106b7da4febfae8c44c232';
const apiUrl = 'https://api.openweathermap.org/data/2.5/weather';

async function fetchWeather(city) {
    try {
        const response = await fetch(`${apiUrl}?q=${city}&units=metric&lang=pt_br&appid=${apiKey}`);
        if (response.status == 404) throw new Error('Localização não encontrada.');
        if (!response.ok) throw new Error('Erro ao buscar a previsão do tempo.');
        const data = await response.json();
        return {data:data, message:"sucesso"};
    } catch (error) {
        console.error(error);
        return {data:null, message:error.message};
    }
}

function formatUnixTimestamp(unixTimestamp) {
    const date = new Date(unixTimestamp * 1000);
    return date.toLocaleString('pt-BR', { timeZone: 'UTC' });
}

function displayWeather(data, message) {
    const resultDiv = document.getElementById('weather-result');

    resultDiv.style.display = 'initial';
    if (!data) {
        resultDiv.innerHTML = `<p>${message}</p>`;
        return;
    }

    const { name, sys, main, weather, wind, clouds, visibility, coord } = data;
    const sunrise = formatUnixTimestamp(sys.sunrise);
    const sunset = formatUnixTimestamp(sys.sunset);

    resultDiv.innerHTML = `
        <h2>${name}, ${sys.country}</h2>
        <p><strong>Temperatura Atual:</strong> ${main.temp.toFixed(1)}°C</p>
        <p><strong>Sensação Térmica:</strong> ${main.feels_like.toFixed(1)}°C</p>
        <p><strong>Temperatura Mínima:</strong> ${main.temp_min.toFixed(1)}°C</p>
        <p><strong>Temperatura Máxima:</strong> ${main.temp_max.toFixed(1)}°C</p>
        <p><strong>Condição Climática:</strong> ${weather[0].description} (${weather[0].main})</p>
        <p><strong>Humidade:</strong> ${main.humidity}%</p>
        <p><strong>Pressão:</strong> ${main.pressure} hPa</p>
        <p><strong>Nível do Mar:</strong> ${main.sea_level} hPa</p>
        <p><strong>Nível do Solo:</strong> ${main.grnd_level} hPa</p>
        <p><strong>Visibilidade:</strong> ${visibility} metros</p>
        <p><strong>Vento:</strong> ${wind.speed} m/s, Direção: ${wind.deg}°</p>
        <p><strong>Nuvens:</strong> ${clouds.all}% de cobertura</p>
        <p><strong>Nascer do Sol:</strong> ${sunrise}</p>
        <p><strong>Pôr do Sol:</strong> ${sunset}</p>
    `;
}


document.getElementById('weather-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const city = document.getElementById('city-name').value.trim();
    if (!city) return;
    const {weatherData, message} = await fetchWeather(city);
    displayWeather(weatherData, message);
});
