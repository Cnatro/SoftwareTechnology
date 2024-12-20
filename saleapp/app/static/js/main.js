function updateItem(data){
    let items = document.getElementsByClassName('cart-counter');
        for(let item of items )
            item.innerText = data.total_quantity;

    let items_ = document.getElementsByClassName('cart-price');
        for(let item of items_ )
            item.innerText = data.total_prices.toLocaleString() + ' VND';
}

function addToCart(id,name,price){
    fetch('/api/carts',{
        method : 'post',
        body:JSON.stringify({
                "id" : id,
                "name" : name,
                "price" : price
            }),
        headers:{
            'Content-Type':'application/json'
        }
    }).then(res => res.json())
      .then(data =>{
            updateItem(data);
      });
}

function updateCart(productID,obj){
      fetch(`/api/carts/${productID}`,{
        method : 'put',
        body:JSON.stringify({
                'quantity':obj.value
            }),
        headers:{
            'Content-Type':'application/json'
        }
    }).then(res => res.json())
      .then(data =>{
            updateItem(data);
      });
}

function deleteCart(productID){
      fetch(`/api/carts/${productID}`,{
        method : 'delete',
     }).then(res => res.json())
      .then(data =>{
            updateItem(data);
            document.getElementById(`cart${productID}`).style.display = 'none'
      });
}

function pay(){
      if(confirm('Ban co chac chan muon thanh toan') === true){
            fetch('/api/pay',{
                method : 'post',
             }).then(res => res.json())
              .then(data =>{
              console.log(data)
                   if(data.status === 200){
                       alert("Thanh toan thanh cong!!");
                       location.reload();
                   }
              });
      }
}