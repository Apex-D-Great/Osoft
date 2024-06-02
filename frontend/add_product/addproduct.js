document.getElementById('productForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    
    const formData = new FormData();
    formData.append('name', document.getElementById('name').value);
    formData.append('discount', document.getElementById('discount').value);
    formData.append('price', document.getElementById('price').value);
    formData.append('stock', document.getElementById('stock').value);
    formData.append('description', document.getElementById('description').value);
    formData.append('image', document.getElementById('image').files[0]);
    
    fetch('http://localhost:5000/product/addproduct', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert('Product data submitted successfully');
        // redirect to another page after successful submission
        window.location.href = 'http://127.0.0.1:5500/frontend/homepage/homepage.html';
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while submitting product data');
    });
});