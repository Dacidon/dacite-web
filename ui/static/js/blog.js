function fetchBlogs(callback) {
    fetch("/blog/data")
        .then(res => res.json())
        .then(data => callback(data))
        .catch(err => console.error(err));
}

fetchBlogs(data => {
    data.articles.forEach(article => {
        const { title, content, date } = article;
        const postElement = document.createElement("div");
        postElement.innerHTML = `Title: ${title}<br><br>Text: ${content}`;
        postElement.className = "post-container";
        document.body.appendChild(postElement);
    });
});