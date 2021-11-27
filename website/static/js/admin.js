$(document).ready(function() {
    const orderAllAPI = "http://127.0.0.1:5000/cart/"

    var orderTable = $("#order-list-table").DataTable({
        columns: [
            {
                data: "id"
            }, 
            {
                data: "date_created"
            },
            {
                data: "status"
            },
            {
                data: "phone"
            },
            {
                data: "address"
            },
            {
                data: "method"
            },
            {
                data: "Action"
            }
        ],
        columnDefs: [
            {
                targets: -1,
                defaultContent: "<button class='btn-success order-detail'><i class='fas fa-info'></i></button>"
            }
        ]
    })

    $("#order-list-table").on("click", ".order-detail", function () {
        orderDetailHandle(this);
    })

    getAllOrder()
    
    function getAllOrder() {
        $.ajax({
            url: orderAllAPI + "order-all",
            type: "GET",
            dataType: 'json',
            success: function (responseObject) {
                console.log(responseObject);
                //goi ham de lay du lieu truye vào dataTable
                loadOrderDataTable(responseObject);
            },
            error: function (error) {
                console.log(error.responseText);
            }
        });
    }

    function loadOrderDataTable(paramObject) {
        orderTable.clear();
        orderTable.rows.add(paramObject);
        orderTable.draw();
    }

    function orderDetailHandle(btn) {
        var selectedRow = $(btn).parents("tr");
        var selectedDataTableRow = orderTable.row(selectedRow);
        var orderData = selectedDataTableRow.data();
        $("#myModal").modal("show")
        getDishByOrderId(orderData.id)
    }

    function getDishByOrderId(paramId) {
        $.ajax({
            url: orderAllAPI + "order-item/" + paramId,
            type: "GET",
            dataType: 'json',
            success: function (responseObject) {
                console.log(responseObject);
                //goi ham de lay du lieu truye vào dataTable
                loadDishDataTable(responseObject);
            },
            error: function (error) {
                console.log(error.responseText);
            }
        });
    }
    
})