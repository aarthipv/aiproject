async function correctText() {
    const text = document.getElementById('inputText').value;
    const response = await fetch('/correct-grammar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text })
    });
    const result = await response.json();
    document.getElementById('output').textContent = result.corrected_text;
}

async function getSuggestions() {
    const text = document.getElementById('inputText').value;
    const response = await fetch('/get-suggestions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text })
    });
    const result = await response.json();
    document.getElementById('output').textContent = result.suggestions.join('\n');
}

async function enhanceContent() {
    const text = document.getElementById('inputText').value;
    const response = await fetch('/enhance-content', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text })
    });
    const result = await response.json();
    document.getElementById('output').textContent = result.enhanced_text;
}
async function checkPlagiarism() {
    const text1 = document.getElementById('inputText').value;
    const text2 = prompt("Enter the second text to check for plagiarism:");

    const response = await fetch('/check-plagiarism', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text1, text2 })
    });

    const result = await response.json();
    document.getElementById('output').textContent = result.plagiarism_result;
}
