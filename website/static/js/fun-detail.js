$(document).ready(function() {
    function changeImage(image) {
        document.getElementById("img-large").src = "images/item0" + image + ".jpg";
    }
    
    function wcqib_refresh_quantity_increments() {
        jQuery("div.quantity:not(.buttons_added), td.quantity:not(.buttons_added)").each(function(a, b) {
            var c = jQuery(b);
            c.addClass("buttons_added"), c.children().first().before('<input type="button" value="-" class="minus" />'), c.children().last().after('<input type="button" value="+" class="plus" />')
        })
    }

    String.prototype.getDecimals || (String.prototype.getDecimals = function() {
        var a = this,
            b = ("" + a).match(/(?:\.(\d+))?(?:[eE]([+-]?\d+))?$/);
        return b ? Math.max(0, (b[1] ? b[1].length : 0) - (b[2] ? +b[2] : 0)) : 0
    }), jQuery(document).ready(function() {
        wcqib_refresh_quantity_increments()
    }), jQuery(document).on("updated_wc_div", function() {
        wcqib_refresh_quantity_increments()
    }), jQuery(document).on("click", ".plus, .minus", function() {
        var a = jQuery(this).closest(".quantity").find(".qty"),
            b = parseFloat(a.val()),
            c = parseFloat(a.attr("max")),
            d = parseFloat(a.attr("min")),
            e = a.attr("step");
        b && "" !== b && "NaN" !== b || (b = 0), "" !== c && "NaN" !== c || (c = ""), "" !== d && "NaN" !== d || (d = 0), "any" !== e && "" !== e && void 0 !== e && "NaN" !== parseFloat(e) || (e = 1), jQuery(this).is(".plus") ? c && b >= c ? a.val(c) : a.val((b + parseFloat(e)).toFixed(e.getDecimals())) : d && b <= d ? a.val(d) : b > 0 && a.val((b - parseFloat(e)).toFixed(e.getDecimals())), a.trigger("change")
    });

    // GLOBAL VARIABLE
    var jsonObject = localStorage.getItem("foodId");
    var parseToObject = JSON.parse(jsonObject);
    
    // add to cart
    checkFoodInLocal();
    function checkFoodInLocal() {
        var jsonObject = localStorage.getItem("foodId");
        var parseToObject = JSON.parse(jsonObject);
        if(!parseToObject) {
            $(".badge").remove();
        } else {
            addBadgeNumber(parseToObject);
        }
        console.log(!parseToObject);
    }


    $("#addCartBtn").on("click", function() {
        var gUrlString = window.location.href;
        var gUrl = new URL(gUrlString);
        var gFoodId = gUrl.searchParams.get("id");
        var qty = $("#qty").val();
        addToLocalStorage(gFoodId, qty);
        console.log(gFoodId, qty);
    })

    function addBadgeNumber(pObject) {
        var badge = `
        <span class="badge bg-danger rounded-circle">${pObject.length}</span> 
        `;
    $(".cart").append(badge);
    }

    function addToLocalStorage(pFoodId, pQty) {
        var foodObjectToLocal = {
            id: pFoodId,
            qty: pQty
        }
        if(!parseToObject) {
            parseToObject = [];
            parseToObject.push(foodObjectToLocal);
            window.localStorage.setItem("foodId", JSON.stringify(parseToObject));
        } else {
            for(let i = 0; i < parseToObject.length; i++) {
                if(pFoodId === parseToObject[i].id) {
                    parseToObject[i].qty++;
                } else if (i == parseToObject.length - 1 && pFoodId != parseToObject[i].id) {
                    addCartItemToCartList(foodObjectToLocal);
                    break;
                }
            }
            window.localStorage.setItem("foodId", JSON.stringify(parseToObject));
        }
        checkFoodInLocal();
    }

    function addCartItemToCartList (paramObject) {
        parseToObject.push(paramObject);
        window.localStorage.setItem("foodId", JSON.stringify(parseToObject));
    }
})

