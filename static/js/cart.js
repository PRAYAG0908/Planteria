var UpdateButtons = document.getElementsByClassName('update-cart')

for (var i = 0; i < UpdateButtons.length; i++) {
    UpdateButtons[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId , 'action:',action)
        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log("Log in first!")
        }
        else{
            UpdateUserData(productId,action)
        }
    })
}

function UpdateUserData(productId,action){
    console.log("Loggedin ,sending data...")

    var url = '/updatecart/'

    fetch(url,{
        method: 'POST',
        headers :{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action' : action})
    })

    .then((respone)=>{
       return respone.json()
    })

    .then((data)=>{
        console.log('data', data)
        location.reload()
    })
}