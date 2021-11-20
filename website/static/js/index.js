$( document ).ready(function() {
   $("#signupForm").validate({
        rules: {
            firstname: "required",
            lastname:"required",

            email: {
                required: true,
                email: true
            },
            numberphone: {
                required: true,
                digits: true
            },
            password: {
                required: true,
                minlength: 5
            },
            repassword: {
                required: true,
                minlength: 5,
                equalTo: "#password"
            },
            address: "required",

            user:"required",

            loginpassword: "required",
               

        },
        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            email:{
                required: "Please enter a valid email address",
                email: "email chua dung dinh dang"
            },
            numberphone: {
                required: "Please enter your numberphone",
                digits: "Numberphone chua dung dinh dang"
            },
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            repassword: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long",
                equalTo: "Please enter the same password as above"
            },
            address: "Please enter your address",

            user:"Please enter your email or phone number",
            
            loginpassword: "Please provide a password",
        
        },
    });

    $("#loginForm").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            loginpassword: {
                required: true,
            },


        },
        messages: {
            email:{
                required: "Please enter a valid email address",
                email: "email chua dung dinh dang"
            },

            loginpassword: {
                required: "Please provide a password",
            },
        },
    });
    getCurrentUser();
});

const getCurrentUser = () => {
    $.get( "/current-user", function( data ) {
        $('#headerUserName').html('Welcome ' + data.firstname + ' ' + data.lastname)
        $('#login-register-link').hide()
    });
}

