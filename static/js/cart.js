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
            console.log("Loggedin ,sending data...")
        }
    })
}