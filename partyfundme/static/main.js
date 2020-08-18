function getBars(evt) {
  evt.preventDefault();

  // API request from front end to back
  $.ajax({
    type: "GET",
    url: "/api/bars",
  }).done(function (data) {
    if (data.errors) {
      console.log(data.errors)
      handleErrorReponseExtra(data.errors);
    } else {
      console.log(data)
      handleResponse(data);
    }
  });
}



let partyEvents = [];

const loadEvents = async () => {
  try {
    const res = await fetch("http://localhost:5000/api/events");
    partyEvents = await res.json();
    console.log(partyEvents);
  } catch (err) {
    console.log(err);
  }
};

const root = document.querySelector(".auto-complete");
root.innerHTML = `


<input
  class="form-control mr-sm-2 input ml-3"
  id="searchBar"
  
  placeholder="Search Event Name"
  aria-label="Search"
  data-toggle="dropdown"
/>
<div class="dropdown ">
  <div class="dropdown-menu" id="event-dropdown">
      <div class="results"></div>
  </div>
</div>



`;

const input = document.querySelector(".input");
const dropdown = document.querySelector(".dropdown");
const resultsWrapper = document.querySelector(".results");



dropdown.classList.add("is-active");

const searchBar = document.querySelector("#searchBar");

searchBar.addEventListener("keyup", (e) => {
  console.log(event);
  const searchString = e.target.value;

  const filteredEvents = partyEvents.events.filter((partyEvent) => {
    return partyEvent.name_of_event.includes(searchString);
  });
  console.log(filteredEvents);
  displayEvents(filteredEvents);
});

console.log(searchBar);
loadEvents();

const displayEvents = (events) => {
  if (!events.length) {
    dropdown.classList.remove("is-active");
    return;
  }
  resultsWrapper.innerHTML = "";
  dropdown.classList.add("is-active");
  for (let event of events) {
    console.log(event.info.event_flyer_img);
    const option = document.createElement("a");
    const imgSrc = `static/profile_pics/${event.info.event_flyer_img}`;

    option.classList.add("dropdown-item");
    option.innerHTML = `
      <img src="${imgSrc}" />
      ${event.name_of_event}
      `;
    option.addEventListener("click", () => {
      dropdown.classList.remove("is-active");
      input.value = event.name_of_event;
    });

    resultsWrapper.appendChild(option);
  }
};

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
