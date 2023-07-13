let starttime;
let dropdown;
let baseUrl = 'http://127.0.0.1:8000/';

document.addEventListener('DOMContentLoaded', function () {
  if (document.getElementById('calendar')) {
    var calendarEl = document.getElementById('calendar');

    // Retrieve the selected GeoLoc from the URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const selectedGeoLoc = urlParams.get('geoloc');

    var calendar = new FullCalendar.Calendar(calendarEl, {
      schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
      timeZone: 'local',
      resourceAreaColumns: [
        {
          field: 'title',
          headerContent: 'Tail Number',
          render: function (resource) {
            return resource.title;
          }
        },
      ],
      resources: function (fetchInfo, successCallback, failureCallback) {
        callResources(fetchInfo, successCallback, failureCallback, selectedGeoLoc);
      },
      events: function (fetchInfo, successCallback, failureCallback) {
        callCalendar(fetchInfo, successCallback, failureCallback, selectedGeoLoc);
        updateData(fetchInfo, successCallback, failureCallback, selectedGeoLoc);
      },
      themeSystem: 'bootstrap5',
      initialView: 'dayGridMonth',
      editable: true,
      eventResourceEditable: true,
      droppable: true,
      multiMonthMaxColumns: 1,
      headerToolbar: {
        left: 'prev,next addEventButton today',
        center: 'title',
        right: 'multiMonthYear,dayGridMonth,dayGridWeek,dayGridDay,resourceTimelineMonth',
      },
      customButtons: {
        addEventButton: {
          text: 'add event...',
          click: function () {
            cancelout.onclick = function () {
              modal.style.display = 'none';
              // Clear the input fields
              var inputFields = document.querySelectorAll('#createModal input[type="text"]');
              inputFields.forEach(function (input) {
                input.value = '';
              });
            };
            // Make a GET request to the API endpoint
            fetch(baseUrl + ' ')
              .then(response => response.json())
              .then(data => {
                const dropdown = document.getElementById('eventDropdown');

                // Iterate over the data and create an option element for each item
                data.forEach(item => {
                  const option = document.createElement('option');
                  option.value = item.value; // Set the value attribute
                  option.textContent = item.text; // Set the text content
                  dropdown.appendChild(option); // Append the option to the dropdown
                });
              })
              .catch(error => {
                console.error('Error:', error);
              });

            // Show the modal
            var modal = document.getElementById('createModal');
            modal.style.display = 'block';

            // grabs tailnumber data
            var dropdown = document.getElementById("eventDropdown");
            var otherInputLabel = document.getElementById("otherInputLabel");
            console.log(dropdown.value);


            var save = document.getElementById('buttonSaveC');
            save.onclick = function () {
              // Retrieve input values
              var title = document.getElementById('titleInput').value;
              var start = document.getElementById('startInput').value;
              var end = document.getElementById('endInput').value;
              var julianDate = document.getElementById('julianInput').value;
              var engineHours = document.getElementById('engineHoursInput').value;
              var flightHours = document.getElementById('flightHoursInput').value;
              var planeSN = document.getElementById('planeSNInput').value;
              var mds = document.getElementById('mdsInput').value;
              var narrative = document.getElementById('narrativeInput').value;
              var currentTime = document.getElementById('currentTimeInput').value;
              var timeRemaining = document.getElementById('timeRemainingInput').value;
              var dueTime = document.getElementById('dueTimeInput').value;
              var dueDate = document.getElementById('dueDateInput').value;
              var frequency = document.getElementById('frequencyInput').value;
              var type = document.getElementById('typeInput').value;
              var justification = document.getElementById('justificationInput').value;
              var timeFrame = document.getElementById('timeFrameInput').value;
              var engineFlight = document.getElementById('engineFlightInput').value;
              var partPlaneSN = document.getElementById('partPlaneSNInput').value;
              var partMDS = document.getElementById('partMDSInput').value;
              var equipmentID = document.getElementById('equipmentIDInput').value;
              var partSerialNumber = document.getElementById('partSerialNumberInput').value;
              var partNumber = document.getElementById('partNumberInput').value;
              var partNarrative = document.getElementById('partNarrativeInput').value;
              var wucLcn = document.getElementById('wucLcnInput').value;
              var catNumber = document.getElementById('catNumberInput').value;
              var partCurrentTime = document.getElementById('partCurrentTimeInput').value;
              var partTimeRemaining = document.getElementById('partTimeRemainingInput').value;
              var partDueTime = document.getElementById('partDueTimeInput').value;
              var partDueDate = document.getElementById('partDueDateInput').value;
              var partFrequency = document.getElementById('partFrequencyInput').value;
              var partType = document.getElementById('partTypeInput').value;
              var partJustification = document.getElementById('partJustificationInput').value;
              var partTimeFrame = document.getElementById('partTimeFrameInput').value;
              var partEngineFlight = document.getElementById('partEngineFlightInput').value;

              fetch(baseUrl + 'resource/')
                .then(response => {
                  if (response.ok) {
                    return response.json(); // Parse the response as JSON
                  } else {
                    throw new Error('Request failed');
                  }
                })
                .then(data => {
                  // Process the data from the response
                  console.log(data);
                })
                .catch(error => {
                  console.error('Error:', error);
                });

              if (wucLcn === undefined) {
                // First POST request
                fetch(baseUrl + 'part-maintenance/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({
                    PlaneSN: partPlaneSN,
                    MDS: partMDS,
                    EQP_ID: equipmentID,
                    PartSN: partSerialNumber,
                    PartNum: partNumber,
                    Narrative: partNarrative,
                    WUC_LCN: wucLcn,
                    CatNum: catNumber,
                    CrntTime: partCurrentTime,
                    TimeRemain: partTimeRemaining,
                    DueTime: partDueTime,
                    DueDate: partDueDate,
                    Freq: partFrequency,
                    Type: partType,
                    JST: partJustification,
                    TFrame: partTimeFrame,
                    E_F: partEngineFlight,
                    title: title
                  })
                })
                  .then(response => response.json())
                  .then(data => {
                    // Extract the ID from the response
                    const id = data.PartMaintenanceID;
                    console.log(id);
                    // Second POST request using the ID from the first response
                    return fetch(baseUrl + 'calendar/', {
                      method: 'POST',
                      headers: {
                        'Content-Type': 'application/json'
                      },
                      body: JSON.stringify({
                        PartMaintenanceID: id,
                        PlaneMaintenanceID: '0',
                        GeoLoc: encodeURIComponent(selectedGeoLoc),
                        FHours: flightHours,
                        EHours: engineHours,
                        title: title,
                        MDS: partMDS,
                        JulianDate: julianDate,
                        end: end,
                        start: start
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
              else {
                // First POST request
                fetch(baseUrl + 'plane-maintenance/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({ name: 'John', age: 25 })
                })
                  .then(response => response.json())
                  .then(data => {
                    // Extract the ID from the response
                    const id = data.id;

                    // Second POST request using the ID from the first response
                    return fetch(baseUrl + 'calendar/', {
                      method: 'POST',
                      headers: {
                        'Content-Type': 'application/json'
                      },
                      body: JSON.stringify({ id: id, someData: 'example' })
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
            }
          }
        }
      },
      eventResizeStart: function (info) {
        starttime = info.event.start.toISOString().substring(0, 10);
      },
      eventResize: function (info) {
        Swal.fire({
          title: info.event.title + ' end is now ' + info.event.end.toISOString().substring(0, 10),
          icon: 'info',
          showCancelButton: true,
          confirmButtonText: 'Yes',
          cancelButtonText: 'No',
          customClass: {
            title: 'swal-title' // Custom class for the title
          },
        }).then((result) => {
          if (result.isConfirmed) {
            resizeEvent(info);
            Swal.fire('Success', 'Event resized.', 'success');
          } else {
            info.revert();
          }
        });

      },
      eventDragStart: function (info) {
        starttime = info.event.start.toISOString().substring(0, 10);
      },
      eventDrop: function (info) {
        Swal.fire({
          title: info.event.title + ' was dropped on ' + info.event.start.toISOString().substring(0, 10),
          icon: 'info',
          showCancelButton: true,
          confirmButtonText: 'Yes',
          cancelButtonText: 'No',
          customClass: {
            title: 'swal-title' // Custom class for the title
          },
        }).then((result) => {
          if (result.isConfirmed) {
            dropEvent(info);
            Swal.fire('Success', 'Event moved.', 'success');
          } else {
            info.revert();
          }
        });
      },
      eventClick: function (info) {
        var event = info.event;
        var closeButton = document.getElementsByClassName('close')[0];

        if (event.extendedProps.PartMaintenanceID == 0) {
          document.getElementById('eventTitle').innerHTML = event.title;
          document.getElementById('eventMaintenance').innerHTML =
            'Start: ' + event.start.toDateString() + '<br>' +
            'End: ' + event.end.toDateString() + '<br>' +
            'Plane Serial Number: ' + event.extendedProps.maintenance.PlaneSN + '<br>' +
            'MDS: ' + event.extendedProps.maintenance.MDS + '<br>' +
            'Narrative: ' + event.extendedProps.maintenance.Narrative + '<br>' +
            'Time Remaining: ' + event.extendedProps.maintenance.TimeRemain + '<br>' +
            'Frequency: ' + event.extendedProps.maintenance.Freq + '<br>' +
            'Type: ' + event.extendedProps.maintenance.Type + '<br>' +
            'Justification: ' + event.extendedProps.maintenance.JST + '<br>' +
            'Time Frame: ' + event.extendedProps.maintenance.TFrame;
        } else {
          document.getElementById('eventTitle').innerHTML = event.title;
          document.getElementById('eventMaintenance').innerHTML =
            'Start: ' + event.start.toDateString() + '<br>' +
            'End: ' + event.end.toDateString() + '<br>' +
            'Plane Serial Number: ' + event.extendedProps.maintenance.PlaneSN + '<br>' +
            'MDS: ' + event.extendedProps.maintenance.MDS + '<br>' +
            'Narrative: ' + event.extendedProps.maintenance.Narrative + '<br>' +
            'Time Remaining: ' + event.extendedProps.maintenance.TimeRemain + '<br>' +
            'Frequency: ' + event.extendedProps.maintenance.Freq + '<br>' +
            'Type: ' + event.extendedProps.maintenance.Type + '<br>' +
            'Justification: ' + event.extendedProps.maintenance.JST + '<br>' +
            'Time Frame: ' + event.extendedProps.maintenance.TFrame + '<br>' +
            'Equipment ID: ' + event.extendedProps.maintenance.EQP_ID + '<br>' +
            'Part Serial Number: ' + event.extendedProps.maintenance.PartSN + '<br>' +
            'Part Number: ' + event.extendedProps.maintenance.PartNum + '<br>' +
            'Work Unit Code/ Logistics Control Number: ' + event.extendedProps.maintenance.WUC_LCN;
        }

        // Show the modal
        var modal = document.getElementById('eventModal');
        modal.style.display = 'block';

        // Handle edit button click
        var editButton = document.getElementById('editButton');

        editButton.onclick = function () {
          // Hide existing content
          document.getElementById('eventTitle').style.display = 'none';
          document.getElementById('eventStart').style.display = 'none';
          document.getElementById('eventEnd').style.display = 'none';
          document.getElementById('eventMaintenance').style.display = 'none';
          closeButton.style.display = 'none';
          editButton.style.display = 'none';

          // Show edit form
          var editForm = document.getElementById('editForm');
          editForm.style.display = 'block';

          // Populate form fields with existing values
          document.getElementById('eventTitleInput').value = event.title;
          document.getElementById('eventStartInput').value = event.start.toISOString().substring(0, 10);
          document.getElementById('eventEndInput').value = event.end.toISOString().substring(0, 10);
          if (event.extendedProps.PartMaintenanceID == 0) {
            document.getElementById('eventMaintenanceInput').innerHTML = '<p>Narrative: <input type="text" id="Narrative" placeholder="Narrative" value="' + event.extendedProps.maintenance.Narrative + '"></p>' +
              '<p>Time Remaining: <input type="text" id="TimeRemain" placeholder="Time Remaining" value="' + event.extendedProps.maintenance.TimeRemain + '"></p>' +
              '<p>Frequency: <input type="text" id="Freq" placeholder="Frequency" value="' + event.extendedProps.maintenance.Freq + '"></p>' +
              '<p>Type: <input type="text" id="Type" placeholder="Type" value="' + event.extendedProps.maintenance.Type + '"></p>' +
              '<p>Time Frame: <input type="text" id="TFrame" placeholder="Time Frame" value="' + event.extendedProps.maintenance.TFrame + '"></p>';
          }
          else {
            document.getElementById('eventMaintenanceInput').innerHTML = '<p>Narrative: <input type="text" id="Narrative" placeholder="Narrative" value="' + event.extendedProps.maintenance.Narrative + '"></p>' +
              '<p>Time Remaining: <input type="text" id="TimeRemain" placeholder="Time Remaining" value="' + event.extendedProps.maintenance.TimeRemain + '"></p>' +
              '<p>Frequency: <input type="text" id="Freq" placeholder="Frequency" value="' + event.extendedProps.maintenance.Freq + '"></p>' +
              '<p>Type: <input type="text" id="Type" placeholder="Type" value="' + event.extendedProps.maintenance.Type + '"></p>' +
              '<p>Time Frame: <input type="text" id="TFrame" placeholder="Time Frame" value="' + event.extendedProps.maintenance.TFrame + '"></p>' +
              '<p>Equipment ID: <input type="text" id="EQP" placeholder="Equipment ID" value="' + event.extendedProps.maintenance.EQP_ID + '"></p>' +
              '<p>Part Serial Number: <input type="text" id="PartSN" placeholder="Part Serial Number" value="' + event.extendedProps.maintenance.PartSN + '"></p>' +
              '<p>Part Number: <input type="text" id="PartNum" placeholder="Part Number" value="' + event.extendedProps.maintenance.PartNum + '"></p>' +
              '<p>Justification: <input type="text" id="JST" placeholder="Justification" value="' + event.extendedProps.maintenance.JST + '"></p>' +
              '<p>Work Unit Code/Logistics Control Number: <input type="text" id="WUC" placeholder="Work Unit Code/Logistics Control Number" value="' + event.extendedProps.maintenance.WUC_LCN + '"></p>';

          }

          var saveButton = document.getElementById('saveButton');
          saveButton.onclick = function () {

            //updated variables
            var updatedTitle = document.getElementById('eventTitleInput').value;
            var updatedStart = document.getElementById('eventStartInput').value;
            var updatedEnd = document.getElementById('eventEndInput').value;
            var updatedNarrative = document.getElementById('Narrative').value;
            var updatedTR = document.getElementById('TimeRemain').value;
            var updatedFreq = document.getElementById('Freq').value;
            var updatedType = document.getElementById('Type').value;
            var updatedTFrame = document.getElementById('TFrame').value;


            //search variables
            let planeSN = event.extendedProps.maintenance.PlaneSN;
            let mds = event.extendedProps.maintenance.MDS;
            let jst = event.extendedProps.maintenance.JST;
            let eqp = event.extendedProps.maintenance.EQP_ID;
            let partsn = event.extendedProps.maintenance.PartSN;
            let partnum = event.extendedProps.maintenance.PartNum;
            if (updatedTitle != event.extendedProps.title || updatedStart != event.extendedProps.start || updatedEnd != event.extendedProps.end) {
              console.log("true");
            }
            else {
              console.log("false");
            }

            if (event.extendedProps.PartMaintenanceID == 0) {

              // Use Swal to confirm before submitting
              Swal.fire({
                title: "Updating Data!",
                text: "Are you sure you want to submit these changes?",
                icon: "question",
                showCancelButton: true,
                confirmButtonText: "Yes",
                cancelButtonText: "Cancel"
              }).then((result) => {
                if (result.isConfirmed) {
                  fetch(baseUrl + 'plane-maintenance/' + planeSN + '/' + mds + '/' + jst + '/', {
                    method: 'PATCH',
                    headers: {
                      'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                      Narrative: updatedNarrative,
                      TimeRemain: updatedTR,
                      Freq: updatedFreq,
                      Type: updatedType,
                      TFrame: updatedTFrame
                    })
                  })
                    .then(response => {
                      if (response.ok) {
                        //updates the calendar with the updated data from the server
                        calendar.refetchEvents();
                        // removes the editfrom data from being displayed
                        editForm.style.display = 'none';

                        //udapdate it to the current calendar view
                        event.extendedProps.maintenance.Narrative = updatedNarrative;
                        event.extendedProps.maintenance.TimeRemain = updatedTR;
                        event.extendedProps.maintenance.Freq = updatedFreq;
                        event.extendedProps.maintenance.Type = updatedType;
                        event.extendedProps.maintenance.TFrame = updatedTFrame;

                        //set the new text displyed to the current data.
                        document.getElementById('eventMaintenance').innerHTML =
                          'Start: ' + event.start.toDateString() + '<br>' +
                          'End: ' + event.end.toDateString() + '<br>' +
                          'Plane Serial Number: ' + event.extendedProps.maintenance.PlaneSN + '<br>' +
                          'MDS: ' + event.extendedProps.maintenance.MDS + '<br>' +
                          'Narrative: ' + updatedNarrative + '<br>' +
                          'Time Remaining: ' + updatedTR + '<br>' +
                          'Frequency: ' + updatedFreq + '<br>' +
                          'Type: ' + updatedType + '<br>' +
                          'Justification: ' + event.extendedProps.maintenance.JST + '<br>' +
                          'Time Frame: ' + updatedTFrame;

                        // Show the original content
                        document.getElementById('eventTitle').style.display = 'block';
                        document.getElementById('eventMaintenance').style.display = 'block';
                        closeButton.style.display = 'block';
                        editButton.style.display = 'block';
                      } else {
                        throw new Error('API call failed');
                      }
                    })
                    .catch(error => {
                      Swal.fire({
                        title: "Error",
                        text: "Failed to submit location: " + error.message,
                        icon: "error",
                        confirmButtonText: "OK"
                      });
                    });
                }
              });

            } else {
              // other updated variables
              var updatedEQP = document.getElementById('EQP').value;
              var updatedPartSN = document.getElementById('PartSN').value;
              var updatedPartNum = document.getElementById('PartNum').value;
              var updatedJST = document.getElementById('JST').value;
              var updatedWUC = document.getElementById('WUC').value;

              //PlaneSN, MDS, EQP_ID, PartSN and PartNum
              // Use Swal to confirm before submitting
              Swal.fire({
                title: "Updating Data!",
                text: "Are you sure you want to submit these changes?",
                icon: "question",
                showCancelButton: true,
                confirmButtonText: "Yes",
                cancelButtonText: "Cancel"
              }).then((result) => {
                if (result.isConfirmed) {
                  fetch(baseUrl + 'part-maintenance/' + planeSN + '/' + mds + '/' + eqp + '/' + partsn + '/' + partnum + '/', {
                    method: 'PATCH',
                    headers: {
                      'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                      Narrative: updatedNarrative,
                      TimeRemain: updatedTR,
                      Freq: updatedFreq,
                      Type: updatedType,
                      TFrame: updatedTFrame,
                      EQP_ID: updatedEQP,
                      PartSN: updatedPartSN,
                      PartNum: updatedPartNum,
                      JST: updatedJST,
                      WUC_LCN: updatedWUC
                    })
                  })
                    .then(response => {
                      if (response.ok) {
                        //updates the calendar with the updated data from the server
                        calendar.refetchEvents();
                        // removes the editfrom data from being displayed
                        editForm.style.display = 'none';

                        //update it to the current calendar view
                        event.extendedProps.maintenance.Narrative = updatedNarrative;
                        event.extendedProps.maintenance.TimeRemain = updatedTR;
                        event.extendedProps.maintenance.Freq = updatedFreq;
                        event.extendedProps.maintenance.Type = updatedType;
                        event.extendedProps.maintenance.TFrame = updatedTFrame;
                        event.extendedProps.maintenance.EQP_ID = updatedEQP;
                        event.extendedProps.maintenance.PartSN = updatedPartSN;
                        event.extendedProps.maintenance.PartNum = updatedPartNum;
                        event.extendedProps.maintenance.JST = updatedJST;
                        event.extendedProps.maintenance.WUC_LCN = updatedWUC;


                        //set the new text displyed to the current data.
                        document.getElementById('eventMaintenance').innerHTML =
                          'Start: ' + event.start.toDateString() + '<br>' +
                          'End: ' + event.end.toDateString() + '<br>' +
                          'Plane Serial Number: ' + event.extendedProps.maintenance.PlaneSN + '<br>' +
                          'MDS: ' + event.extendedProps.maintenance.MDS + '<br>' +
                          'Narrative: ' + updatedNarrative + '<br>' +
                          'Time Remaining: ' + updatedTR + '<br>' +
                          'Frequency: ' + updatedFreq + '<br>' +
                          'Type: ' + updatedType + '<br>' +
                          'Justification: ' + updatedJST + '<br>' +
                          'Time Frame: ' + updatedTFrame + '<br>' +
                          'Equipment ID: ' + updatedEQP + '<br>' +
                          'Part Serial Number: ' + updatedPartSN + '<br>' +
                          'Part Number: ' + updatedPartNum + '<br>' +
                          'Work Unit Code/ Logistics Control Number: ' + updatedWUC;

                        // Show the original content
                        document.getElementById('eventTitle').style.display = 'block';
                        document.getElementById('eventMaintenance').style.display = 'block';
                        closeButton.style.display = 'block';
                        editButton.style.display = 'block';
                      } else {
                        throw new Error('API call failed');
                      }
                    })
                    .catch(error => {
                      Swal.fire({
                        title: "Error",
                        text: "Failed to submit location: " + error.message,
                        icon: "error",
                        confirmButtonText: "OK"
                      });
                    });
                }
              });
            }
          }
          // Handle cancel button click
          var cancelButton = document.getElementById('cancelButton');
          cancelButton.onclick = function () {
            // Hide the edit form
            var editForm = document.getElementById('editForm');
            editForm.style.display = 'none';

            // Show the original content
            document.getElementById('eventTitle').style.display = 'block';
            document.getElementById('eventMaintenance').style.display = 'block';
            closeButton.style.display = 'block';
            editButton.style.display = 'block';
          };
        }
        closeButton.onclick = function () {
          modal.style.display = 'none';
        };

      },
      eventMouseEnter: function (info) {
        if (info.event) {
          var tooltipContent = '<div><strong>' + info.event.extendedProps.planeData.TailNumber + '</strong></div>';
          tooltipContent += '<div>Title: ' + info.event.title + '</div>';
          tooltipContent += '<div>Narrative: ' + info.event.extendedProps.maintenance.Narrative + '</div>';
          tooltipContent += '<div>Type: ' + info.event.extendedProps.maintenance.Type + '</div>';
          if (info.event.extendedProps.PlaneMaintenanceID == 0) {
            tooltipContent += '<div>CatNum: ' + info.event.extendedProps.maintenance.CatNum + '</div>';
          }
          else {
            tooltipContent += '<div>JST: ' + info.event.extendedProps.maintenance.JST + '</div>';
          }

          var tooltipInstance = new bootstrap.Tooltip(info.el, {
            title: tooltipContent,
            html: true,
            placement: 'auto',
            trigger: 'hover',
            container: 'body'
          });

          tooltipInstance.show();
        }
      },
      eventMouseLeave: function (info) {
        var tooltipInstance = bootstrap.Tooltip.getInstance(info.el);
        if (tooltipInstance) {
          tooltipInstance.dispose();
          tooltipInstance.hide();
        }

      },
    });

    calendar.render();
  }
});

function callCalendar(fetchInfo, successCallback, failureCallback, selectedGeoLoc) {
  // Make an API call to retrieve the events
  // Replace 'YOUR_API_ENDPOINT' with the actual API endpoint URL
  fetch(baseUrl + 'calendar/geoloc/' + encodeURIComponent(selectedGeoLoc) + '/')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      //console.log(data);
      // Process the API response and transform it into FullCalendar event format
      var events = data.map(function (apiEvent) {
        return {
          title: apiEvent.title,
          start: apiEvent.start,
          end: apiEvent.end,
          // Include additional data beyond basic event properties
          // You can store any custom data as additional properties
          // For example:
          // Aircraft: apiEvent.Aircraft,
          MDS: apiEvent.MDS,
          TailNumber: apiEvent.TailNumber,
          JulianDate: apiEvent.JulianDate,
          EHours: apiEvent.EHours,
          FHours: apiEvent.FHours,
          maintenance: apiEvent.maintenance,
          PartMaintenanceID: apiEvent.PartMaintenanceID,
          PlaneMaintenanceID: apiEvent.PlaneMaintenanceID,
          GeoLoc: apiEvent.GeoLoc,
          CalendarID: apiEvent.CalendarID,
          planeData: apiEvent.plane_data,
          resourceId: apiEvent.ResourceID,

        }
      });

      //console.log(events);
      // Call the successCallback with the retrieved events
      successCallback(events);
    })
    .catch(function (error) {
      // Call the failureCallback in case of error
      failureCallback(error);
    });
}

function updateData(fetchInfo, successCallback, failureCallback, selectedGeoLoc) {
  fetch(baseUrl + 'calendar/geoloc/' + encodeURIComponent(selectedGeoLoc) + '/')
    .then(response => response.json())
    .then(data => {
      // Get today's date
      var today = new Date();
      console.log(data);
      // Filter the objects with end date prior to today's date and completed equal to false
      var filteredObjects = data.filter(obj => new Date(obj.end_date) < today && obj.completed === false);

      // Update the time for each filtered object
      filteredObjects.forEach(obj => {
        // Calculate the new times
        var newDueTime = obj.DueTime + obj.Freq;
        var newTimeRemain = obj.Freq;

        // Make a PATCH request to update the object
        if (obj.PlaneMaintenanceID > 0) {
          fetch(baseUrl + 'calendar/planemaintenance/' + obj.PlaneMaintenanceID + '/', { // Replace with your actual API endpoint URL and object ID field
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              DueTime: newDueTime,
              TimeRemain: newTimeRemain,
              Completed: true
            })
          })
            .then(response => {
              if (response.ok) {
                console.log('Object with ID ' + obj.id + ' updated successfully.');
              } else {
                console.error('Failed to update object with ID ' + obj.id + '.');
              }
            })
            .catch(error => {
              console.error('An error occurred while updating object with ID ' + obj.id + ':', error);
            });
        }
        else if (obj.PartMaintenanceID > 0) {
          fetch(baseUrl + 'calendar/partmaintenance/' + obj.PartMaintenanceID + '/', { // Replace with your actual API endpoint URL and object ID field
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              DueTime: newDueTime,
              TimeRemain: newTimeRemain,
              Completed: true
            })
          })
            .then(response => {
              if (response.ok) {
                console.log('Object with ID ' + obj.id + ' updated successfully.');
              } else {
                console.error('Failed to update object with ID ' + obj.id + '.');
              }
            })
            .catch(error => {
              console.error('An error occurred while updating object with ID ' + obj.id + ':', error);
            });
        }
      });
    })
    .catch(error => {
      console.error('An error occurred while fetching the objects:', error);
    });
}

function callResources(fetchInfo, successCallback, failureCallback, selectedGeoLoc) {
  // Fetch the tail numbers from the Plane data model
  fetch(baseUrl + 'calendar/geoloc/' + encodeURIComponent(selectedGeoLoc) + '/')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      //console.log(data);
      // Process the API response and transform it into FullCalendar event format
      var resources = data.map(function (apiEvent) {
        return {
          id: apiEvent.ResourceID,
          title: apiEvent.TailNumber,
        }
      });
      //console.log(resources);
      // Call the successCallback with the retrieved events
      successCallback(resources);
    })
    .catch(function (error) {
      // Call the failureCallback in case of error
      failureCallback(error);
    });
}



function dropEvent(info) {
  // Retrieve the updated event details
  var eventId = info.event.extendedProps.CalendarID;
  var newStart = info.event.start.toISOString().substring(0, 10);
  var newEnd = info.event.end.toISOString().substring(0, 10);

  fetch(baseUrl + 'calendar/' + eventId + '/', {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      start: newStart,
      end: newEnd
    })
  })
    .then(function (response) {
      // Check if the update was successful
      if (response.ok) {
        console.log('Event updated in the database.');
      } else {
        console.error('Failed to update event in the database.');
      }
    })
    .catch(function (error) {
      console.error('Error updating event:', error);
    });

}

function resizeEvent(info) {
  // Retrieve the updated event details
  var eventId = info.event.extendedProps.CalendarID;
  var newStart = info.event.start.toISOString().substring(0, 10);
  var newEnd = info.event.end.toISOString().substring(0, 10);


  fetch(baseUrl + 'calendar/' + eventId + '/', {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      start: newStart,
      end: newEnd
    })
  })
    .then(function (response) {
      // Check if the update was successful
      if (response.ok) {
        console.log('Event updated in the database.');
      } else {
        console.error('Failed to update event in the database.');
      }
    })
    .catch(function (error) {
      console.error('Error updating event:', error);
    });
}




document.addEventListener('DOMContentLoaded', function () {
  if (document.getElementById('dropdownContainer')) {
    const container = document.getElementById('dropdownContainer');
    const submitBtn = document.getElementById('submit-btn');

    async function fetchOptions() {
      try {
        const response = await fetch(baseUrl + 'loc/');
        const data = await response.json();

        dropdown = document.getElementById('select');

        data.forEach(item => {
          const option = document.createElement('option');
          option.value = item.id;
          option.text = item.GeoLoc;
          option.setAttribute('data-geoloc', item.GeoLoc); // Store the GeoLoc value as an attribute
          dropdown.appendChild(option);
        });

        container.appendChild(dropdown);
      } catch (error) {
        console.error('Error fetching options:', error);
      }
    }

    fetchOptions();

    submitBtn.addEventListener('click', function () {
      const selectedOption = dropdown.options[dropdown.selectedIndex]; // Get the selected option element
      const selectedGeoLoc = selectedOption.getAttribute('data-geoloc'); // Retrieve the GeoLoc value

      saveSelectedGeoLoc(selectedGeoLoc);
      // Redirect to the calendar page based on the selected GeoLoc
      window.location.href = `calendar.html?geoloc=${encodeURIComponent(selectedGeoLoc)}`;
    });
  }
});

function addlocation() {
  // Grab the location value from the input field
  var location = document.getElementById("location-input").value;

  // Use Swal to confirm before submitting
  Swal.fire({
    title: "Submit Location",
    text: "Are you sure you want to submit this " + location + "?",
    icon: "question",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "Cancel"
  }).then((result) => {
    if (result.isConfirmed) {
      // Perform the API call or any other desired action
      // Replace the 'API_CALL_URL' with the actual API endpoint
      // You can use AJAX, Fetch, or any other method to make the API call
      // Example using Fetch API
      fetch(baseUrl + 'loc/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ GeoLoc: location })
      })
        .then(response => {
          if (response.ok) {
            // Redirect to another page after successful API call
            window.location.href = "/";
          } else {
            throw new Error('API call failed');
          }
        })
        .catch(error => {
          Swal.fire({
            title: "Error",
            text: "Failed to submit location: " + error.message,
            icon: "error",
            confirmButtonText: "OK"
          });
        });
    }
  });
}
function saveSelectedGeoLoc(selectedGeoLoc) {
  sessionStorage.setItem('selectedGeoLoc', selectedGeoLoc);
}
// Retrieve selected GeoLoc from session storage
function getSelectedGeoLoc() {
  return sessionStorage.getItem('selectedGeoLoc');
}
function passgeoloc(filename) {
  const selectedGeoLoc = getSelectedGeoLoc();
  window.location.href = baseUrl + filename + '?geoloc=' + encodeURIComponent(selectedGeoLoc);
}

document.addEventListener('DOMContentLoaded', function () {
  // Attach event listeners for collapsible buttons
  var collapsibleButtons = document.getElementsByClassName('collapsible');
  for (var i = 0; i < collapsibleButtons.length; i++) {
    collapsibleButtons[i].addEventListener('click', function () {
      this.classList.toggle('active');
      var content = this.parentNode.nextElementSibling;
      if (content.style.display === 'block') {
        content.style.display = 'none';
      } else {
        content.style.display = 'block';
      }
    });
  }
});

function toggleOtherInputLabel() {
  var dropdown = document.getElementById("eventDropdown");
  var otherInputLabel = document.getElementById("otherInputLabel");

  if (dropdown.value === "other") {
    otherInputLabel.classList.remove("hidden");
  } else {
    otherInputLabel.classList.add("hidden");
  }
}