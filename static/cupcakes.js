// Define the base URL for API requests
const BASE_URL = "http://localhost:5000/api";

/** Given data about a cupcake, generate HTML */
function generateCupcakeHTML(cupcake) {
     return `
        <div data-cupcake-id=${cupcake.id}>
            <li>
                ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
                <button class="delete-button">X</button>
            </li>
            <img class="Cupcake-img"
                src="${cupcake.image}"
                alt="(no image provided)">
        </div>
    `;
}

/** Put initial cupcakes on the page */
function showInitialCupcakes() {
     // Fetch cupcakes from the API
     axios.get(`${BASE_URL}/cupcakes`)
          .then(response => {
               // Iterate through the cupcakes and append them to the list
               for (let cupcakeData of response.data.cupcakes) {
                    let newCupcake = $(generateCupcakeHTML(cupcakeData));
                    $("#cupcakes-list").append(newCupcake);
               }
          })
          .catch(error => console.error(error));
}

/** Handle form for adding new cupcakes */
$("#new-cupcake-form").on("submit", async function (evt) {
     evt.preventDefault();

     // Get the form input values
     let flavor = $("#form-flavor").val();
     let size = $("#form-size").val();
     let rating = $("#form-rating").val();
     let image = $("#form-image").val();

     // Send a POST request to create a new cupcake
     const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
          flavor,
          size,
          rating,
          image
     });

     // Append the new cupcake to the list and reset the form
     let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
     $("#cupcakes-list").append(newCupcake);
     $("#new-cupcake-form").trigger("reset");
});

/** Handle clicking delete: delete a cupcake */
$(document).ready(function () {
     $("#cupcakes-list").on("click", ".delete-button", async function (evt) {
          evt.preventDefault();
          // Get the cupcake ID from the data attribute
          let $cupcake = $(evt.target).closest("div");
          let cupcakeId = $cupcake.attr("data-cupcake-id");

          // Send a DELETE request to remove the cupcake
          await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
          // Remove the cupcake from the list
          $cupcake.remove();
     });
});

// Show the initial cupcakes when the document is ready
$(showInitialCupcakes);
