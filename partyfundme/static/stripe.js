const checkoutButton = document.querySelector("#buy_now_btn");
console.log('loaded')
checkoutButton.addEventListener("click", (event) => {
  console.log('loaded')
  fetch("/stripe")
    .then((result) => {

      return result.json();
    })
    .then((data) => {
      var stripe = Stripe(data.checkout_public_key);
      stripe
        .redirectToCheckout({
          // Make the id field from the Checkout session creation API response
          // available to this file, so you can provide it asa  parameter here
          // instead of the {{CHECKOUG_SESSION_ID}} placeholder.
          sessionId: data.checkout_session_id,
        })
        .then(function (result) {
          // IF `redirectToCheckout` fails due to a browser or network
          // error, display the localized error message to your customer
          // using `result.error.message`
        });
    });
});
