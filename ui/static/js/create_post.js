document.getElementById("create_post").addEventListener('submit', transformData);

function transformData(event) {
    event.preventDefault();
    data = {
        "title": event.target["0"].value,
        "content": event.target["1"].value,
    };
    fetch("/api/blog/create", {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((json) => console.log(json));
}