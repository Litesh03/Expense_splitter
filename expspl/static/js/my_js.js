function add_expense()
{
    console.log("INSIDE STORE");
	name = document.getElementById("name").value;
	item = document.getElementById("item").value;
	date = document.getElementById("date").value;
	price = document.getElementById("price").value;
    var sendData = JSON.stringify({name,item,date,price});

    $.ajax({
        url: '/api/v1/storeData',
        type: "POST",
        contentType: "application/json",
        dataType: 'json',
        data: sendData,
        //encode: true    
		}).done(function(ack) {
        console.log(ack);
		alert(sendData);
        event.preventDefault(); });
}

function get_expenses()
{
var tab = $.ajax({
        url: '/api/v1.0/get_table',
        type: "GET",
        contentType: "application/json",
        dataType: 'json',
        //encode: true    
		})
alert(tab)
		
buildTable(tab)

function buildTable(data){
	var table = document.getElementById('myTable')

	for (var i = 0; i < data.length; i++){
		var row = `<tr>
						<td>${data[i].name}</td>
						<td>${data[i].item}</td>
						<td>${data[i].price}</td>
				  </tr>`
		table.innerHTML += row


	}
}
}