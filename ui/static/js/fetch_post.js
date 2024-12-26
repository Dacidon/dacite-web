const postId = window.location.pathname.substring(6);

function fetchPost(callback) {
    fetch(`/api/blog/${postId}`)
        .then(res => res.json())
        .then(data => callback(data))
        .catch(err => console.error(err));
}

fetchPost(post => {
    let { id, title, content, created_at, updated_at } = post;

    created_at = new Date(created_at).toLocaleString();
    updated_at = new Date(updated_at).toLocaleString()
    const postElement = document.createElement("div");
    postElement.innerHTML = `
        <span style="font-size: 30px; flex: 1">${title}</span>
        <span style="align-self: center; flex: 6;">${content}</span>
        <span class="dates">created: ${created_at}<br>edited: ${updated_at === created_at ? "never" : updated_at}</span>
    `;
    postElement.classList = "base post-container post";

    const editLink = document.createElement("a");
    editLink.href = `/blog/edit/${id}`;
    editLink.innerText = "Edit";
    editLink.className = "base";
    editLink.style = "border-style: groovy;";

    document.body.appendChild(postElement);
    document.body.appendChild(editLink);
})