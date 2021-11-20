$(document).ready(function () {

    // Table Database
    // const tableJSON = JSON.parse({{ table|tojson }})
    // console.log(tableJSON)
    // var tableObject = require('website/table.json')
    // console.log(tableObject)

    // let myRequest = new Request("table.json")
    // fetch(myRequest)
    //     .then(function(resp) {
    //         return resp.json();
    //     })
    //     .then(function (data) {
    //         console.log(data.booking)
    //     }) 
    const bookingURL = "http://127.0.0.1:5000/"

    const tableJSON = `{
        "booking": [
            {
                "name": "Hiep",
                "phone_number:": "0958456781",
                "date":"2021-11-05",
                "time": "18:00 PM",
                "nop": "4",
                "msg": "None"
            },
            {
                "name": "An",
                "phone_number:": "0958456461",
                "date":"2021-11-06",
                "time": "15:00 PM",
                "nop": "6",
                "msg": "None"
            },
            {
                "name": "Binh",
                "phone_number:": "0924456781",
                "date":"2021-11-05",
                "time": "19:00 PM",
                "nop": "6",
                "msg": "None"
            },
            {
                "name": "Chau",
                "phone_number:": "0914656781",
                "date":"2021-11-05",
                "time": "18:00 PM",
                "nop": "2",
                "msg": "None"
            }
        ]
    }`
    // console.log(JSON.parse(tableJSON))
    var dataStore = (function () {
        var object;

        $.ajax({
            url: bookingURL + "all",
            type: "GET",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            async: false,
            success: function (responseObject) {
                object = responseObject
                // console.log(responseObject)
                // console.log(object)
            },
            error: function (error) {
                console.log(error)
            }
        })

        return {
            getObject: function () {
                if (object) return object;
            }
        }
    })();

    var tableObject = $(dataStore.getObject())
    console.log(tableObject.length)

    // const json = '[{"name":"Hiep","phone_number":"0958456781","date":"2021-11-05","time":"18","nop":"4","msg":"none"},' +
    //     '{"name":"An","phone_number":"0958456461","date":"2021-11-06","time":"15","nop":"6","msg":"none"},' +
    //     '{"name":"Binh","phone_number":"0924456781","date":"2021-11-05","time":"19","nop":"6","msg":"none"},' +
    //     '{"name":"Chau","phone_number":"0914656781","date":"2021-11-05","time":"18","nop":"2","msg":"none"},' +
    //     '{"name":"Dieu","phone_number":"0915756781","date":"2021-11-08","time":"10","nop":"2","msg":"none"},' +
    //     '{"name":"Giang","phone_number":"0924456821","date":"2021-11-08","time":"12","nop":"2","msg":"none"},' +
    //     '{"name":"Hai","phone_number":"0910656781","date":"2021-11-08","time":"15","nop":"4","msg":"none"},' +
    //     '{"name":"Hanh","phone_number":"0924167423","date":"2021-11-08","time":"18","nop":"6","msg":"none"},' +
    //     '{"name":"Kiet","phone_number":"0924412049","date":"2021-11-08","time":"18","nop":"2","msg":"none"},' +
    //     '{"name":"Kiet","phone_number":"0924412049","date":"2021-11-09","time":"18","nop":"2","msg":"none"},' +
    //     '{"name":"Khiem","phone_number":"0924154763","date":"2021-11-08","time":"18","nop":"4","msg":"none"}]'

    // const tableObject = JSON.parse(json);

    // console.log(tableObject);

    date_config = {
        minDate: "today",
        // dateFormat: "M d, Y",
        dateFormat: "Y-m-d",
        allInput: true,
        onChange: function (selectedDate, dateStr, instance) {
            selectedDate.forEach(function (date) {
                getDate(date)
                return date
            })
        }
    }

    // var jsonstr = '"' + $("#user-data").html() + '"';
    // var jsontest = JSON.parse($("#user-data").html())

    flatpickr("input[type=date]", date_config)

    function getDate(pDate) {
        console.log(pDate)
        console.log(pDate.getFullYear(), pDate.getMonth() + 1, pDate.getDate())
    }

    $("#datepicker").on("change", function () {
        let date = new Date($("#datepicker").val());
        let time = $("#timepicker").val();
        let nob = $("#peoplepicker").val();

        tableBookinginFormation(date, time, nob);
    })

    // input timepicker on change 
    $("#timepicker").on("change", function () {
        let date = new Date($("#datepicker").val());
        let time = $("#timepicker").val();
        let nob = $("#peoplepicker").val();

        tableBookinginFormation(date, time, nob);
    })

    // Nob on change
    $("#peoplepicker").on("change", function () {
        let date = new Date($("#datepicker").val());
        let time = $("#timepicker").val();
        let nob = $("#peoplepicker").val();

        tableBookinginFormation(date, time, nob);
    })

    function tableBookinginFormation(pDate, pTime, pNop) {
        let dateSelect = $("#datepicker").val();
        let timeSelect = $("#timepicker").val();
        let typeSelect = $("#peoplepicker").val();
        // console.log(tableObject)
        // if(tableObject[1].date == dateSelect) {
        //     console.log("Yes");
        // } else console.log("No")
        // console.log(dateSelect)

        if (pDate != "Invalid Date" && pTime != 0 && pNop == 0) {
            // $("#datepicker").flatpickr({
            //     dateFormat: "Y-m-d",
            //     disable: ["2021-11-08"]
            // })

            let typeArr = [];
            for (i = 0; i < tableObject.length; i++) {
                if (tableObject[i].date == dateSelect && tableObject[i].time == timeSelect) {
                    typeArr.push(tableObject[i].nop);
                }
            }
            console.log(typeArr);
            $("#peoplepicker > option").each(function () {
                $(this).removeClass('disable');
                $(this).attr('disabled', false);
            })
            $("#peoplepicker > option").each(function () {
                for (j = 0; j < typeArr.length; j++) {
                    if (typeArr[j] == this.value) {
                        $(this).addClass('disable');
                        $(this).attr('disabled', true);
                    }
                }
            })
            console.log(dateSelect, timeSelect);
        } else if (pDate != "Invalid Date" && pNop != 0 && pTime == 0) {
            let timeArr = [];
            for (i = 0; i < tableObject.length; i++) {
                if (tableObject[i].date == dateSelect && tableObject[i].nop == typeSelect) {
                    timeArr.push(tableObject[i].time);
                }
            }
            console.log(timeArr)
            $("#timepicker > option").each(function () {
                $(this).removeClass('disable');
                $(this).attr('disabled', false);
            })
            console.log(timeArr)
            $("#timepicker > option").each(function () {
                for (let j = 0; j < timeArr.length; j++) {
                    if (timeArr[j] == this.value) {
                        $(this).addClass('disable');
                        $(this).attr('disabled', true);
                    }
                }
            })
            console.log(dateSelect, typeSelect);
        } else if (pTime != 0 && pNop != 0 && pDate == "Invalid Date") {
            let dateArr = [];
            for (let i = 0; i < tableObject.length; i++) {
                if (tableObject[i].time == timeSelect && tableObject[i].nop == typeSelect) {
                    dateArr.push(tableObject[i].date);
                }
            }
            console.log(dateArr);

            $("#datepicker").flatpickr({
                minDate: "today",
                dateFormat: "Y-m-d",
                disable: dateArr
            })
        } else if (pDate != "Invalid Date" && pTime != 0 && pNop != 0) {
            for (let i = 0; i < tableObject.length; i++) {
                if (tableObject[i].date == dateSelect && tableObject[i].time == timeSelect && tableObject[i].nop == typeSelect) {
                    $("#datepicker").flatpickr().clear();
                }
            }
        }
        console.log(pDate, pTime, pNop)
    }

    $("#book_info").on("click", function () {
        var date = $("#datepicker").val();
        var time = $("#timepicker").val();
        var type = $("#peoplepicker").val();
        if (date === "Invalid Date") {
            actionOfToast("show", "warning", "Warning: Vui lòng chọn ngày!");
        }
        if (time === "0") {
            actionOfToast("show", "warning", "Warning: Vui lòng chọn giờ!");
        }
        if (type === "0") {
            actionOfToast("show", "warning", "Warning: Vui lòng chọn loại bàn!");
        }
        if (date != "Invalid Date" && time != "0" && type != "0") {
            $("#myModal").modal("show")
            console.log(date, time, type);
        }

    })

    $("#book").on("click", function () {
        var name = $("#name");
        var nameValue = $("#name").val().trim();
        var phone = $("#phonenumber")
        var phoneValue = $("#phonenumber").val().trim();
        var date = $("#datepicker").val();
        var time = $("#timepicker").val();
        var type = $("#peoplepicker").val();
        var note = $("#note").val();
        var noteValue = $("#note").val().trim();
        if (validateForm(name, phone)) {
            var bookingObject = {
                "name": nameValue,
                "phone": phoneValue,
                "date": date,
                "time": time,
                "nop": type,
                "comment": ""
            }
            if (noteValue === "") {
                bookingObject.comment = "";
            } else {
                bookingObject.comment = note;
            }
            console.log(bookingObject);
            $.ajax({
                url: bookingURL + "add",
                method: "POST",
                headers: { "Content-Type": "application/json" },
                data: JSON.stringify(bookingObject),
                success: function () {
                    $("#myModal").modal("hide")
                    resetForm();
                    actionOfToast("show", "success", "Đặt bàn thành công!");
                    console.log("POST Success!")
                },
                error: function (error) {
                    console.log(error)
                }
            })
        }

    })

    // CHỨC NĂNG XEM ĐẶT BÀN THEO SỐ ĐIỆN THOẠI
    $(".check-btn").on("click", function () {
        $("#phone-check").val('');
        $(".booking-history").removeClass("show")
        $(".booking-history").addClass("hide")
        $("#checkModal").modal("show")
    })

    $("#check").on("click", function () {
        $("#table-booking-list > tr > td").remove();
        var phoneCheck = $("#phone-check")
        var phonCheckVal = $("#phone-check").val().trim()
        if (validateCheck(phoneCheck)) {
            $.ajax({
                url: bookingURL + "table/" + phonCheckVal,
                type: "GET",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                async: false,
                success: function (responseObject) {
                    loadBookingList(responseObject)
                },
                error: function (error) {
                    console.log(error)
                }
            })
        }
    })

    function resetForm() {
        $("#datepicker").flatpickr().clear();
        $("#timepicker").val(0);
        $("#peoplepicker").val(0);
        $("#note").val('');
    }

    function loadBookingList(pObject) {
        console.log(pObject)
        if (pObject.length == 0) {
            $(".booking-history").removeClass("show")
            $(".booking-history").addClass("hide")
            actionOfToast("show", "warning", "Không có bàn nào dược đặt!");
        } else {
            $(".booking-history").removeClass("hide")
            $(".booking-history").addClass("show")
            for (let i = 0; i < pObject.length; i++) {
                if (pObject[i].date < 12) {
                    var tr = ` 
                        <tr>
                            <td>${pObject[i].phone}</td>
                            <td>${pObject[i].date}</td>
                            <td>${pObject[i].time} AM</td>
                            <td>${pObject[i].nop} người</td>
                        </tr>`
                    $("#table-booking-list").append(tr)
                } else {
                    var tr = ` 
                    <tr>
                        <td>${pObject[i].phone}</td>
                        <td>${pObject[i].date}</td>
                        <td>${pObject[i].time} PM</td>
                        <td>${pObject[i].nop} người</td>
                    </tr>`
                    $("#table-booking-list").append(tr)
                }
            }
        }

    }

    function validateCheck(pPhone) {
        var phoneCheckVal = pPhone.val().trim()
        var check = true;
        if (phoneCheckVal === "") {
            check = false;
            setBookingErrorFor(pPhone, "Vui lòng điền số điện thoại!")
        } else if (phoneCheckVal.length != 10) {
            check = false;
            setBookingErrorFor(pPhone, "Số điện thoại phải là 10 số!")
        } else {
            setBookingSuccessFor(pPhone);
        }
        return check
    }

    function validateForm(pName, pPhone) {
        var nameValue = pName.val().trim();
        var phoneValue = pPhone.val().trim();
        var check = true;
        if (nameValue === "") {
            check = false;
            setBookingErrorFor(pName, "Vui lòng điền tên!");
        } else {
            setBookingSuccessFor(pName);
        }
        if (phoneValue === "") {
            check = false;
            setBookingErrorFor(pPhone, "Vui lòng điền số điện thoại!")
        } else if (phoneValue.length != 10) {
            check = false;
            setBookingErrorFor(pPhone, "Số điện thoại phải là 10 số!")
        } else {
            setBookingSuccessFor(pPhone);
        }
        return check;
    }

    $("#name").focusout(function () {
        const name = $("#name");
        const nameValue = $("#name").val().trim();
        if (nameValue === "") {
            setBookingErrorFor(name, "Vui lòng điền tên!");
        } else {
            setBookingSuccessFor(name);
        }
    })

    $("#phonenumber").focusout(function () {
        const phone = $("#phonenumber");
        const phoneValue = $("#phonenumber").val().trim();
        if (phoneValue === "") {
            setBookingErrorFor(phone, "Vui lòng điền số điện thoại!");
        } else if (phoneValue.length != 10) {
            setBookingErrorFor(phone, "Số điện thoại gồm 10 số!");
        } else {
            setBookingSuccessFor(phone);
        }
    })

    $("#phone-check").focusout(function () {
        const phone = $("#phone-check");
        const phoneValue = $("#phone-check").val().trim();
        if (phoneValue === "") {
            setBookingErrorFor(phone, "Vui lòng điền số điện thoại!");
        } else if (phoneValue.length != 10) {
            setBookingErrorFor(phone, "Số điện thoại gồm 10 số!");
        } else {
            setBookingSuccessFor(phone);
        }
    })

    function actionOfToast(action, status, message) {
        if (action === "show") {
            $(".alert").removeClass('hide');
            $(".alert").addClass('show');
        }
        $(".alert").addClass(status);
        $(".msg").text(message);
        setTimeout(function () {
            $(".alert").removeClass('show');
            $(".alert").addClass('hide');
        }, 5000);
        $(".close-btn").on("click", function () {
            $(".alert").addClass("hide");
            $(".alert").removeClass("show");
        })
    }

    function setBookingErrorFor(input, message) {
        const formControl = input.parent();
        const small = formControl.find('small');
        const checkIcon = formControl.find('fa-check-circle');
        small.text(message);
        checkIcon.attr("display", "none");
        formControl.removeClass("success");
        formControl.addClass("error");
    }

    function setBookingSuccessFor(input) {
        const formControl = input.parent();
        const small = formControl.find('small');
        small.attr("display", "none");
        formControl.removeClass("error");
        formControl.addClass("success");
    }
})