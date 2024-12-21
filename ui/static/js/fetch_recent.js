function fetchRecentBlogs(callback) {
    fetch("/api/blog/recent")
        .then(res => res.json())
        .then(data => callback(data))
        .catch(err => console.error(err));
}

fetchRecentBlogs(data => {
    data.forEach(post => {
        let { id, title, content, created_at, updated_at } = post;
        const trimmedContent = content.substr(0, 70);
        created_at = new Date(created_at).toLocaleString();
        updated_at = new Date(updated_at).toLocaleString()
        const postElement = document.createElement("div");
        postElement.innerHTML = `
            <span><a href="/blog/${id}" class="base" style="border-bottom-style: solid; border-bottom-width: 2px;">${title}</a></span>
            <span>${trimmedContent.substring(0, Math.min(trimmedContent.length, trimmedContent.lastIndexOf(" "))) + "..."}</span>
            <span class="dates">created: ${created_at}</span>
            <span class="dates">edited: ${updated_at === created_at ? "never" : updated_at}</span>
        `;
        postElement.classList = "base post-preview-container post";
        document.body.appendChild(postElement);
    });
});