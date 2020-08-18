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


