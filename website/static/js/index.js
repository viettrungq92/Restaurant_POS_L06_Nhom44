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
                email: "Please enter a valid email address"
            },
            numberphone: {
                required: "Please enter your phone number",
                digits: "Please enter a valid phone number"
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
            user: {
                required: true,
                email: true
            },
            loginpassword: {
                required: true,
            },


        },
        messages: {
            user:{
                required: "Please enter a valid email address",
                email: "Please enter a valid email address"
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

const toggleShowPassword = () => {
    const passwordInput = document.getElementById('password');
    const togglePasswordIcon = document.getElementById('togglePassword');
    if(passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePasswordIcon.className = "fa fa-eye-slash"
    } else {
        passwordInput.type = "password";
        togglePasswordIcon.className = "far fa-eye"
    }
}
