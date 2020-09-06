
const searchEvents = async searchText => {

    const res = await fetch("https://partyfund.herokuapp.com/api/events");
    partyEvents = await res.json();
    console.log(partyEvents);


    // Get matchds to current text input
    let matches = partyEvents.events.filter((event) => {
      const regex = new RegExp(`^${searchText}`, "gi");
      return event.name_of_event.match(regex) ;
    });

    if (searchText.length === 0) {
      matches = [];
      matchList.innerHTML = ''
    }

    outputHtml(matches);

    console.log(matches);
  
};


// show results in HTML
const outputHtml = matches => {
  if(matches.length > 0) {
    const html = matches.map(match => `
    <div class="col-md-4 d-flex">
    <div class="card flex-fill">
      <a class="img-card" href="/events/${ match.id }">
        <img src="../../../static/profile_pics/${ match.info.event_flyer_img }" class="img-fluid mb-5" />
      </a>
      <br />
      <div class="event-content">
        <div class="event-content-header">
          <a href="#">
            <h3 class="event-title">${match.name_of_event}</h3>
          </a>
          <div class="ms-logo"></div>
        </div>
        <div class="event-info">
          <div class="info-section">
            <label>Date & Time</label>
            <span>${match.info.date_of_party}</span>
            <span>${match.info.time_of_party}</span>
          </div><!--date,time-->
          <div class="info-section">
            <label>Location</label>
            <span>{{bar.bar_name}}</span>
          </div><!--screen-->
          <div class="info-section">
            <label>Bar Tab Raised</label>
            <span>{{event.total_fund}}</span>
          </div><!--row-->
          <div class="info-section">
            <label>Goal</label>
            <span>{{event.total_fund}}</span>
          </div><!--seat-->
        </div>
      </div>

    
    </div>
  </div>
    `).join('');

    matchList.innerHTML = html;
  }
}

const root = document.querySelector(".auto-complete");
root.innerHTML = `
<div class="container mt-5">
  <div class="row">
      <div class="col-md-12 m-auto">
        <div class="form-group">
        <h1 class="text-center mb-3">Party Finder</h1>
          <input
            class="form-control mr-sm-2 input ml-3"
            id="search"
            placeholder="Search Event Name"
            aria-label="Search"
          />
        </div>
        <div class="d-flex" id="match-list"></div>
    </div>
  </div>
</div>
`;

const search = document.querySelector("#search");
const matchList = document.querySelector("#match-list");

// Search patryEvents.json and filter it

const allEvents = document.getElementById("all-events");

search.addEventListener("input", () => {
  
  if (allEvents.style.display === "none") {
    allEvents.style.display = "block";
  } else {
    allEvents.style.display = "none";
  }
  searchEvents(search.value)
});









