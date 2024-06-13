var cart = [];

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function (event) {
  stored_cart = localStorage.getItem("cart");

  if (localStorage.getItem("cart")) {
    cart = JSON.parse(stored_cart);
    $("#cart").html(cart.length);
  }
});

function addToCart(item) {
  var check = cart.filter((product) => product.id === item.id);

  if (check.length === 0) {
    cart.push(item);
    localStorage.setItem("cart", JSON.stringify(cart));
    $("#cart").html(cart.length);
  }
}

function handleQty(item, op) {
  var cart_item = cart.findIndex((p) => p.id === item);
  var qty = parseInt($("#p-" + item).val());

  if (op == "add") {
    qty = qty + 1;
  } else if (op == "min") {
    if (qty > 1) {
      qty = qty - 1;
    } else {
      newCart = cart.filter((p) => p.id !== item);

      localStorage.setItem("cart", JSON.stringify(newCart));
      loadCart();
      return true;
    }
  }

  cart[cart_item].qty = qty;
  localStorage.setItem("cart", JSON.stringify(cart));
  loadCart();

  $("#p-" + item).val(qty);
  $("#cart").html(cart.length);
}

function loadCart() {
  var stored_cart = localStorage.getItem("cart");

  if (localStorage.getItem("cart")) {
    cart = JSON.parse(stored_cart);
  }
  var temp_arr = "";
  var num = 0;
  var total = 0;

  if (cart && cart.length > 0) {
    cart.map((product) => {
      num++;
      total = total + parseFloat(product.price) * parseInt(product.qty);

      temp_arr += `<li class="list-group-item">
                        <div class="row">
                            <div class="col-7">${num} - ${product.title}</div>
                            <div class="col-2">OMR ${product.price}</div>
                            <div class="col-3">
                                <div class="btn-group" role="group" aria-label="Basic example">
                                    <button type="button" class="btn btn-success" onClick="handleQty(${product.id}, 'add')"><i class="fa fa-plus"></i></button>
                                    <input type="text" min="0" class="btn border text-center" value="${product.qty}" style="width: 80px; text-align: center" disabled id="p-${product.id}" />
                                    <button type="button" onClick="handleQty(${product.id}, 'min')" class="btn btn-danger"><i class="fa fa-minus"></i></button>
                                </div>
                            </div>
                        </div>
                    </li>`;
    });
  } else {
    temp_arr =
      '<div class="text-center text-muted p-4 m-5">Add items to the shoppig card to checkout.</div>';
  }

  document.getElementById("items").innerHTML = temp_arr;
  document.getElementById("total").innerText = total;
}

function ask() {
    var question = $('#question').val()
    if(question != ''){
        var question_buble = '<div class="p-3 bg-info text-white rounded m-3 col-5" style="float: right !important;">'+question+'</div>'

        $('#chatBox').append(question_buble)
        $("#chatBox").scrollTop($("#chatBox")[0].scrollHeight);

        answer(question)

        $('#question').val('')
    }
}

function answer(params) {
    $.ajax({
        url: 'http://127.0.0.1:8000/chatbot/',
        method: 'post',
        data: { "question": params, "csrfmiddlewaretoken": CSRF_TOKEN },
        success: function(res) {
            var ansr = ''
            if(res){
                ansr = '<div class="row col-9 m-2"><div class="p-3 m-0 col-2"><img src="/static/assets/images/bot.png" style="width: 50px;" alt=""></div><div class="p-3 m-0 card rounded col-8 float-end">'+res.answer+'</div></div>'
            } else {
                ansr = '<div class="row col-9 m-2"><div class="p-3 m-0 col-2"><img src="/static/assets/images/bot.png" style="width: 50px;" alt=""></div><div class="p-3 m-0 card rounded col-8 float-end">Sorry I find have no answer for this question, try again or contact us for more inforamtion..</div></div>'
            }

            setTimeout(function() {
                $('#chatBox').append(ansr)
                $("#chatBox").scrollTop($("#chatBox")[0].scrollHeight);
            }, 700)
        },
        error: function(err) {
            setTimeout(function() {
                $('#chatBox').append('<div class="row col-9 m-2"><div class="p-3 m-0 col-2"><img src="/static/assets/images/bot.png" style="width: 50px;" alt=""></div><div class="p-3 m-0 card rounded col-8 float-end">Sorry I find have no answer for this question, try again or contact us for more inforamtion...</div></div>')

                $("#chatBox").scrollTop($("#chatBox")[0].scrollHeight);
            }, 700)
            
        }
    })
}

function displayChatbot() {
    $('#chatbot').removeClass('d-none').fadeToggle( "slow", "linear" );
}

function checkout(e) {
    var address = $('#address').val();
    var governate = $('#governate').val();
    var payment = $('[name="payment"]').val();
    if(address !== ''){
        $("#error").html("")
        $.ajax({
            url: 'http://127.0.0.1:8000//checkout/',
            type: "POST",
            data: {
                "governate": governate,
                "address": address,
                "payment": payment,
                "cart": JSON.stringify(cart),
                "csrfmiddlewaretoken": CSRF_TOKEN
            },
            success: function (data) {
                console.log(data)
                if(data.success === 'true'){
                    localStorage.clear()
                    window.location = '/thankyou'
                } else {
                    $("#error").html("Sorry we faced some problem while processing your order please try again.");
                }
            },
            error: function () {
                $("#error").html("Sorry we faced some problem while processing your order please try again.");
            }
        });
    } else {
        $("#error").html("Please enter your address.")
    }
}