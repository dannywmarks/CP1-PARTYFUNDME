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

/** handleResponse: deal with response from our lucky-num API. */

  // function handleResponse(data) {
  //   let year = data.year.year;
  //   let yearFact = data.year.fact;
  //   let luckyNumber = data.num.num;
  //   let luckyNumberFact = data.num.fact;

  //   $("#lucky-results")
  //     .text(`Your lucky number is ${luckyNumber}. ${luckyNumberFact}
  //   Your birth year is ${year}. The fact is ${yearFact}`);
  // }

//   <div class="container">
//     <div class="row">
//         <div class="col-xs-12 col-sm-6 col-md-6">
//             <div class="well well-sm">
//                 <div class="row">
//                     <div class="col-sm-6 col-md-4">
//                         <img src="http://placehold.it/380x500" alt="" class="img-rounded img-responsive" />
//                     </div>
//                     <div class="col-sm-6 col-md-8">
//                         <h4>
//                             Bhaumik Patel</h4>
//                         <small><cite title="San Francisco, USA">San Francisco, USA <i class="glyphicon glyphicon-map-marker">
//                         </i></cite></small>
//                         <p>
//                             <i class="glyphicon glyphicon-envelope"></i>email@example.com
//                             <br />
//                             <i class="glyphicon glyphicon-globe"></i><a href="http://www.jquery2dotnet.com">www.jquery2dotnet.com</a>
//                             <br />
//                             <i class="glyphicon glyphicon-gift"></i>June 02, 1988</p>
//                         <!-- Split button -->
//                         <div class="btn-group">
//                             <button type="button" class="btn btn-primary">
//                                 Social</button>
//                             <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
//                                 <span class="caret"></span><span class="sr-only">Social</span>
//                             </button>
//                             <ul class="dropdown-menu" role="menu">
//                                 <li><a href="#">Twitter</a></li>
//                                 <li><a href="https://plus.google.com/+Jquery2dotnet/posts">Google +</a></li>
//                                 <li><a href="https://www.facebook.com/jquery2dotnet">Facebook</a></li>
//                                 <li class="divider"></li>
//                                 <li><a href="#">Github</a></li>
//                             </ul>
//                         </div>
//                     </div>
//                 </div>
//             </div>
//         </div>
//     </div>
// </div>




$("#lucky-form").on("submit", processForm);
