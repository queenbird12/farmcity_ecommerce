var updateBtns = document.getElementsByClassName('updatecart')


for (var i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        console.log('productId:', productId, 'action',action)

        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}
function updateUserOrder(productId, action){
    console.log('User is logged in, sending data.')

    var url = '/updateitem/'

    fetch (url, {
        method:'POST',
        headers:{
            'content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId' : productId, 'action' : action})
    })
    .then((response)=> {
        return response.json();
    })
    .then((data)=>{
        console.log('data:',data);
        location.reload()
    });
}
function processOrder(paymentMethod) {
    const orderData = {
        paymentMethod: paymentMethod,
        orderId: 'order-id-goes-here', // Replace with the actual order ID
        amount: 0.01, // Replace with the actual order amount
    };

    fetch('/process_payment/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(), // Include CSRF token for security
        },
        body: JSON.stringify(orderData),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                alert('Payment recorded. Waiting for admin approval.');
            } else {
                alert('Payment failed: ' + data.message);
            }
        })
        .catch((error) => {
            console.error('Error processing payment:', error);
        });
}

// Helper function to retrieve the CSRF token
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}
