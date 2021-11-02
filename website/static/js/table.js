date_config = {
    minDate: "today",
    dateFormat: "M d, Y",
    allInput: true
}

flatpickr("input[type=date]", date_config)


$("#datepicker").on("change", function() {
    console.log("Select Input")
})

$(document).ready(function() {
    
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