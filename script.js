'use strict'
// path -- string specifying URL to which data request is sent 
// callback -- function called by JavaScript when response is received                     
function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}
function getData(){
 ajaxGetRequest("/bar", showBar);
 ajaxGetRequest("/pie", showPie);
//  ajaxGetRequest("/line", show_lineGraph)
}
function showBar(response){
  let data = JSON.parse(response)
  let bar = [{"x":[], "y":[], type: 'bar'}]
  let layout = {title:"Fully Vaccinated by Location", font :{family: 'Times New Roman'},xaxis: {title: "Location"}, yaxis:{title:"% Fully Vaccinated"}}
  for(let lst of data){
    bar[0]["x"].push(lst[0])
    bar[0]["y"].push(Number(lst[1]))
  }
  Plotly.newPlot("bar", bar, layout)
}
function showPie(response){
  let data = JSON.parse(response)
  let pieChart = [{"values": [], "labels":[], type: 'pie'}]
  let labels = ['Janssen', 'Moderna', 'Pfizer', 'Unknown']
  for(let la of labels){
   pieChart[0]["labels"].push(la)
  }
  let layout = {height: 400, width: 500};
  let moderna = 0;
  let pfizer = 0;
  let janssen = 0;
  let unknown = 0;
  for(let d of data){
    moderna = moderna + d[0]
    pfizer = pfizer + d[1]
    janssen = janssen + d[2]
    unknown = unknown + d[3]
  }
  pieChart[0]["values"].push(moderna)
  pieChart[0]["values"].push(pfizer)
  pieChart[0]["values"].push(janssen)
  pieChart[0]["values"].push(unknown)
  Plotly.newPlot("pie",pieChart, layout)   
}
// path -- string specifying URL to which data request is sent
// data -- JSON blob being sent to the server
// callback -- function called by JavaScript when response is received
function ajaxPostRequest(path, data, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("POST", path);
    request.send(data);
}
function getLocData(){
  let location = document.getElementById("locText")
  let json_blob = JSON.stringify(location["value"]);

  ajaxPostRequest("/line", json_blob, show_lineGraph)
}
function show_lineGraph(response){
  let data = JSON.parse(response)
  let graph = [{"x": [], "y": [], type: 'line'}]
  let location = data[0][1]
  for(let x of data){
    graph[0]["x"].push(x[0])
    graph[0]["y"].push(Number(x[2]))
  }
  let layout = {
  title: '% of '+ location + ' Fully Vaccinated By Date',
  xaxis: {
    title: 'Date'
  },
  yaxis: {
    title: '% Fully Vaccinated'
  }
 };
  Plotly.newPlot("line", graph, layout);
}
