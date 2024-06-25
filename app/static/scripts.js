document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];

    if (!file) {
        alert("Пожалуйста, выберите файл.");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/search', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    displayResults(data.results);
});

function displayResults(results) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';

    const filteredResults = results.filter(result => result.similarity > 0.5);

    if (filteredResults.length === 0) {
        resultsContainer.innerHTML = '<p>Нет похожих изображений с более чем 50% схожестью.</p>';
        return;
    }

    filteredResults.forEach(result => {
        const resultItem = document.createElement('div');
        resultItem.classList.add('result-item');

        const img = document.createElement('img');
        img.src = `/static/images/${result.image_name}`;
        resultItem.appendChild(img);

        const similarity = document.createElement('span');
        similarity.classList.add('similarity');
        similarity.textContent = `Схожесть: ${(result.similarity * 100).toFixed(2)}%`;
        resultItem.appendChild(similarity);

        resultsContainer.appendChild(resultItem);
    });
}
