function getCupcakeDetails(cupcake) {
    return '<li data-cupcake-id=${cupcake.id}><b>${cupcake.flavor}</b> - ${cupcake.size} - Rating: ${cupcake.rating} <button class="delete">X</button>'
}

async function getAllCupcakes() {
    const res = await axios.get('http://localhost:5000/api/cupcakes')

    for (let cupcake of res.data.cupcakes) {
        let cupcakeData = $(getCupcakeDetails(cupcake));
        $("#cupcake-list").append(cupcakeData);
    }
}

$(getAllCupcakes);