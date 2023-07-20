console.log('loaded');
let base = 'http://127.0.0.1:8000/';

// goes through excel sheet and converts data to objects
async function importExcel() {
  var file = document.getElementById('excel_file');
  var data = await readXlsxFile(file.files[0]);
  var columnNames = data[0];

  var objects = data.slice(1).map(row => {
    var object = {};
    columnNames.forEach((column, index) => {
      object[column] = row[index];
    });
    return object;
  });
  return objects;
}

async function postExcel() {
    var importObjects = await importExcel();
    //make a get request for location and if it doesnt return anything make the location with a post request
    var newGeoLoc = true;
    fetch(base + 'loc/', )
    .then(response => response.json())
    .then(data => {
        // Iterate over the data and see if GeoLoc already exist
        data.forEach(item => {
          if (importObjects[0].GeoLoc == item.GeoLoc) {
            newGeoLoc = false;
            return;
          }
        });
        // if GeoLoc doesnt exist POST new GeoLoc
        if (newGeoLoc == true) {
            fetch(base + 'loc/', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify({ GeoLoc: importObjects[0].GeoLoc })
            })
            .catch(error => {
                console.log('Error: ' + error);
            });
        }
    })
    .catch(error => {
    console.error('Error:', error);
    });

    // Get Each Object that needs to be imported
    importObjects.forEach(obj => {
        // Post Plane Data
        fetch(base + 'plane-data/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
                PlaneSN: obj.PlaneSN,
                GeoLoc: obj.GeoLoc,
//                MDS: obj.MDS,
//                WUC_LCN: obj.WUC_LCN,
                EQP_ID: obj.EQP_ID,
                TailNumber: obj.TailNumber
          })
        })
        .then(response => {
            if (response.ok) {
              console.log('Plane Data POST request succeeded');
            } else {
              console.error('Plane Data POST request failed');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });

        // POST resource
        fetch(base + 'resource/', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({
            TailNumber: obj.TailNumber,
            GeoLoc: obj.GeoLoc,
            })
        })
        .then(response => {
            if (response.ok) {
              return response.json(); // Parse the response as JSON
            } else {
              throw new Error('resource Data POST request failed');
            }
        })
        .then(data => {
            // Extract the resourceId from the response
            var resourceId = data.ResourceID;

            // Post Part/Plane Maintenance
            var startD = new Date(obj.start);
            var start = startD.getFullYear() + '-' + (startD.getMonth() + 1) + '-' + startD.getDate();
            var endD = new Date(obj.end);
            var end = endD.getFullYear() + '-' + (endD.getMonth() + 1) + '-' + endD.getDate();
            var dueD = new Date();
            var due = dueD.getFullYear() + '-' + (dueD.getMonth() + 1) + '-' + dueD.getDate();
            if (obj.Maintenance.toUpperCase() == 'PART') {
                fetch(base + 'part-maintenance/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({
                        PlaneSN: obj.PlaneSN,
                        MDS: obj.MDS,
                        EQP_ID: obj.EQP_ID,
                        PartSN: obj.PartSN,
                        PartNum: obj.PartSN,
                        Narrative: obj.Narrative,
                        WUC_LCN: obj.WUC_LCN,
                        CatNum: obj.CatNum,
                        CrntTime: obj.CrntTime,
                        TimeRemain: obj.TimeRemain,
                        DueTime: obj.DueTime,
                        DueDate: due,
                        Freq: obj.Freq,
                        Type: obj.Type,
                        JST: obj.JST,
                        TFrame: obj.TFrame,
                        E_F: obj.E_F,
                        title: obj.title
                  })
                })
                .then(response => response.json())
                .then(data => {
                  // Extract the ID from the response
                  const id = data.PartMaintenanceID;
                  // Second POST request using the ID from the first response
                  return fetch(base + 'calendar/', {
                    method: 'POST',
                    headers: {
                      'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                      PartMaintenanceID: id,
                      PlaneMaintenanceID: '0',
                      GeoLoc: obj.GeoLoc,
                      FHours: obj.FHours,
                      EHours: obj.EHours,
                      title: obj.title,
                      MDS: obj.MDS,
                      JulianDate: obj.JulianDate,
                      end: end,
                      start: start,
                      TailNumber: obj.TailNumber,
                      ResourceID: resourceId
                    })
                  });
                })
                .then(response => {
                  if (response.ok) {
                    console.log('Second POST request succeeded');
                  } else {
                    console.error('Second POST request failed');
                  }
                })
                .catch(error => {
                console.error('Error:', error);
                });
            }
            else if (obj.Maintenance.toUpperCase() == 'PLANE') {
                fetch(base + 'plane-maintenance/', {
                    method: 'POST',
                    headers: {
                      'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                      PlaneSN: planeSN,
                      MDS: mds,
                      Narrative: narrative,
                      CrntTime: currentTime,
                      TimeRemain: timeRemaining,
                      DueTime: dueTime,
                      Freq: frequency,
                      Type: type,
                      JST: justification,
                      TFrame: timeFrame,
                      E_F: engineFlight,
                      title: title
                    })
                })
                .then(response => response.json())
                .then(data => {
                  // Extract the ID from the response
                  const id = data.PlaneMaintenanceID;
                  // Second POST request using the ID from the first response
                  return fetch(base + 'calendar/', {
                    method: 'POST',
                    headers: {
                      'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                      PartMaintenanceID: '0',
                      PlaneMaintenanceID: id,
                      GeoLoc: obj.GeoLoc,
                      FHours: obj.FHours,
                      EHours: obj.EHours,
                      title: obj.title,
                      MDS: obj.MDS,
                      JulianDate: obj.JulianDate,
                      end: end,
                      start: start,
                      TailNumber: obj.TailNumber,
                      ResourceID: resourceId
                    })
                  });
                })
                .then(response => {
                  if (response.ok) {
                    console.log('Second POST request succeeded');
                  } else {
                    console.error('Second POST request failed');
                  }
                })
                .catch(error => {
                  console.error('Error:', error);
                });
            }
        });
    });
}