/*
-----------------------------------------------------------------
res_app/static/js/index.js
-----------------------------------------------------------------
Using the revealing module pattern to define custom functions and constants for our res_app application.
*/
var resApp = (function(){
  function fetchLoad(el) {
    let url = el.dataset.url;
    if (url) {
      let resp = fetch(url);
      resp.then(response=>response.json()).then(json=>{
            if (json.is_valid) {
              el.innerHTML = json.html;
            } else {
              alert(json.error);
            }
          }).catch(err=>{
            console.log(err);
          });
    } else {
      console.log('No URL defined!');
    }
  }
  function loadDivs() {
    let elems = document.querySelectorAll('.js-load-div');
    for (var i = 0; i < elems.length; i++) {
      fetchLoad(elems[i]);
    }
  }
  return {
    loadDivs: loadDivs,
  };
})();
