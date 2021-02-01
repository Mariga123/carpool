  function initMap() {

    console.log("initMap")
  }
  
  function calculateAndDisplayRoute(directionsService, directionsRenderer , params) {
    console.log("In calcandDisplay")
    console.log(params)

    directionsService.route(
    {
      origin:{lat: params['latVal'], lng: params['lngVal']},
      destination: params['pickup'],
      travelMode: 'DRIVING'
    },
    
    function(response, status) {
      if (status === 'OK') {
        directionsRenderer.setDirections(response);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });


  }