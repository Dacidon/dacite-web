const postId = window.location.pathname.substring(11);

function fetchPost(callback) {
    fetch(`/api/blog/${postId}`)
        .then(res => res.json())
        .then(data => callback(data))
        .catch(err => console.error(err));
}

fetchPost(data => {
    document.getElementById("post").innerText = data["content"];
})

document.getElementById("edit_post").addEventListener('submit', transformData);

function transformData(event) {
    event.preventDefault();
    data = {
        "content": event.target["0"].value,
    };
    fetch(`/api/blog/edit/${postId}`, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((json) => console.log(json));
}