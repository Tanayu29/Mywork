document.getElementById('testcase-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    
    fetch('/generate', {
        method: 'POST',
        body: formData
    }).then(response => response.json())
    .then(data => {
        if (data.links) {
            const downloadDiv = document.getElementById('download-links');
            downloadDiv.innerHTML = '';
            data.links.forEach(link => {
                const a = document.createElement('a');
                a.href = `/download/${link.url}`;
                a.textContent = `Download ${link.format}`;
                a.download = 'output.txt';  // 保存するファイル名を指定
                downloadDiv.appendChild(a);
                downloadDiv.appendChild(document.createElement('br'));
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
