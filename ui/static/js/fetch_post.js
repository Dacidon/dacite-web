const postId = window.location.pathname.substring(6);

function fetchPost(callback) {
    fetch(`/api/blog/${postId}`)
        .then(res => res.json())
        .then(data => callback(data))
}

fetchPost(data => {
    data.forEach(post => {
        let { id, title, content, created_at, updated_at } = post;
        created_at = new Date(created_at).toLocaleString();
        updated_at = new Date(updated_at).toLocaleString()
        const postElement = document.createElement("div");
        postElement.innerHTML = `
            <span style="font-size: 30px;">${title}</span>
            <span>${content}</span>
            <span class="dates">created: ${created_at}</span>
            <span class="dates">updated: ${updated_at === created_at ? "never" : updated_at}</span>
        `;
        postElement.className = "post-container";
        document.body.appendChild(postElement);
    });
})