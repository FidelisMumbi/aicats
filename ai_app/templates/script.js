function send_json(datas,urlp){
    fetch(urlp,{
        method:"POST",
        //headers:{'Content-Type':'application/json'},
        body:JSON.stringify(datas)
    })
    .then(response => response.json())
    .then(data =>{
        //console.log('server_response',data);
        //alert(`received json:${JSON.stringify(data)}`)
        if (data && data.redirect){
            if(data.info == 'verified'){
                export_data('./index.html',data.user_id)
            }
            if(data.info == 'order_made'){
                alert(data)
                alert('Order has been made, successfully')
                window.location.href='./index.html'
            }
        }
    })
    .catch(error =>{
        alert('no connection..')
        console.log('error',error)
    });
  
  }