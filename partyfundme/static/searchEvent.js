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
<form>
<input
  class="form-control mr-sm-2 input ml-3"
  id="searchBar"
  type="search"
  placeholder="Search"
  aria-label="Search"
/>


  <div class="dropdown">
  
    <div class="dropdown-menu">
      <div class="dropdown-content results"></div>
    </div>
  </div></form>`;

const input = document.querySelector(".input");
const dropdown = document.querySelector(".dropdown");
const resultsWrapper = document.querySelector(".results");
const posterIntoSignup = document.getElementById('poster-div')
const signupBTN = document.getElementById('sign-in')

dropdown.classList.add("is-active");
  
const searchBar = document.querySelector("#searchBar");

searchBar.addEventListener("keyup", (e) => {
  const searchString = e.target.value;
  
  const filteredEvents = partyEvents.events.filter((partyEvent) => {
    return partyEvent.name_of_event.includes(searchString)
  });
  displayEvents(filteredEvents)
});

console.log(searchBar)
loadEvents();






const displayEvents = (events) => {
  // if (!events.length) {
  //   dropdown.classList.remove("is-active");
  //   return;
  // }
  resultsWrapper.innerHTML = "";
  dropdown.classList.add("is-active");
  for (let event of events) {
    console.log(event.info.event_flyer_img)
    const option = document.createElement("a");
    const imgSrc = `../${event.info.event_flyer_img}`

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