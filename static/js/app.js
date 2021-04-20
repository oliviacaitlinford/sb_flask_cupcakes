function getCupcakeDetails(cupcake) {
    return `<li data-cupcake-id=${cupcake.id}><b>${cupcake.flavor}</b> - ${cupcake.size} - Rating: ${cupcake.rating} <button class="delete">X</button></li>`
}

async function getAllCupcakes() {
    const res = await axios.get('http://localhost:5000/api/cupcakes')

    for (let cupcake of res.data.cupcakes) {
        let cupcakeData = $(getCupcakeDetails(cupcake));
        $("#cupcake-list").append(cupcakeData);
    }
}

$("#cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();

    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#rating").val();
    let image = $("#image").val();

    const res = await axios.post('http://localhost:5000/api/cupcakes', {flavor, size, rating, image});

    let newCupcake = $(getCupcakeDetails(res.data.cupcake));
    $("#cupcake-list").append(newCupcake);
    $("#cupcake-form").trigger("reset");
});

$("#cupcake-list").on("click", ".delete", async function(evt) {
    evt.preventDefault();

    let $cupcake = $(evt.target).closest("li");
    let cupcakeId = $cupcake.attr("data-cupcake-id");

    await axios.delete(`http://localhost:5000/api/cupcakes/${cupcakeId}`);
    $cupcake.remove();
})

$(getAllCupcakes);