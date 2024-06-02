// document.getElementById('productSearchForm').addEventListener('submit', function(event) {
//     event.preventDefault();

//     const productName = document.getElementById('productName').value;

//     // Send an AJAX request to the backend to query the database based on the product name
//     // and render the results in the carousel
//     fetch(`/api/product?name=${productName}`)
//     .then(response => response.json())
//     .then(data => {
//         const carouselInner = document.getElementById('carouselInner');
//         carouselInner.innerHTML = ''; // Clear previous results

//         data.forEach(product => {
//             const card = document.createElement('div');
//             card.classList.add('card');

//             const cardImage = document.createElement('img');
//             cardImage.src = product.image;
//             card.appendChild(cardImage);

//             const cardContent = document.createElement('div');
//             cardContent.classList.add('card-content');

//             const productName = document.createElement('h2');
//             productName.textContent = product.name;
//             cardContent.appendChild(productName);

//             const productDescription = document.createElement('p');
//             productDescription.textContent = product.description;
//             cardContent.appendChild(productDescription);

//             card.appendChild(cardContent);
//             carouselInner.appendChild(card);
//         });
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });

document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:5000/product/addproduct') // Fetch data when the page loads
    .then(response => response.json())
    .then(data => {
        const carouselInner = document.getElementById('carouselInner');
        // carouselInner.innerHTML = ''; // Clear previous results
        data.forEach(product => {
            const card = document.createElement('div');
            card.classList.add('card');

            const cardImage = document.createElement('img');
            cardImage.src = `/frontend/image/${product.image}`;
            cardImage.style = "width:128px; height:128px;"
            card.appendChild(cardImage);

            const cardContent = document.createElement('div');
            cardContent.classList.add('card-content');

            const productName = document.createElement('h2');
            productName.textContent = product.name;
            cardContent.appendChild(productName);

            const productDescription = document.createElement('p');
            productDescription.textContent = product.description;
            cardContent.appendChild(productDescription);

            card.appendChild(cardContent);
            carouselInner.appendChild(card);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
});