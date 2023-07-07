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
      resources: function (fetchInfo, successCallback, failureCallback) {
        callResources(fetchInfo, successCallback, failureCallback);
      },
      events: function (fetchInfo, successCallback, failureCallback) {
        callCalendar(fetchInfo, successCallback, failureCallback, selectedGeoLoc);
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
            var dateStr = prompt('Enter a date in YYYY-MM-DD format');
            var date = new Date(dateStr + 'T00:00:00'); // will be in local time

            if (!isNaN(date.valueOf())) { // valid?
              calendar.addEvent({
                title: 'dynamic event',
                start: date,
                allDay: true
              });
              alert('Great. Now, update your database...');
            } else {
              alert('Invalid date.');
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
            var updatedTitle = document.getElementById('eventTitleInput').value;
            var updatedStart = document.getElementById('eventStartInput').value;
            var updatedEnd = document.getElementById('eventEndInput').value;

            if (event.extendedProps.PartMaintenanceID == 0) {
              var updatedNarrative = document.getElementById('Narrative').value;
              var updatedTR = document.getElementById('TimeRemain').value;
              var updatedFreq = document.getElementById('Freq').value;
              var updatedType = document.getElementById('Type').value;
              var updatedTFrame = document.getElementById('TFrame').value;
              let planeSN = event.extendedProps.maintenance.PlaneSN;
              let mds = event.extendedProps.maintenance.MDS;
              let jst = event.extendedProps.maintenance.JST;


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
                        event.extendedProps.maintenance.TimeRemain = updatedTimeRemain;
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
              //udated variables
              var updatedNarrative = document.getElementById('Narrative').value;
              var updatedTR = document.getElementById('TimeRemain').value;
              var updatedFreq = document.getElementById('Freq').value;
              var updatedType = document.getElementById('Type').value;
              var updatedTFrame = document.getElementById('TFrame').value;
              var updatedEQP = document.getElementById('EQP').value;
              var updatedPartSN = document.getElementById('PartSN').value;
              var updatedPartNum = document.getElementById('PartNum').value;
              var updatedJST = document.getElementById('JST').value;
              var updatedWUC = document.getElementById('WUC').value;

              // search variables
              let planeSN = event.extendedProps.maintenance.PlaneSN;
              let mds = event.extendedProps.maintenance.MDS;
              let eqp = event.extendedProps.maintenance.EQP_ID;
              let partsn = event.extendedProps.maintenance.PartSN;
              let partnum = event.extendedProps.maintenance.PartNum;

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

                        //udapdate it to the current calendar view
                        event.extendedProps.maintenance.Narrative = updatedNarrative;
                        event.extendedProps.maintenance.TimeRemain = updatedTimeRemain;
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
                          'Time Remaining: ' + updatedTimeRemain + '<br>' +
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
            editButton.style.display = 'block';
          };


        }

        var closeButton = document.getElementsByClassName('close')[0];
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
  fetch(baseUrl + 'calendar/geoloc/' + encodeURIComponent(selectedGeoLoc))
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
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

        }
      });

      console.log(events);
      // Call the successCallback with the retrieved events
      successCallback(events);
    })
    .catch(function (error) {
      // Call the failureCallback in case of error
      failureCallback(error);
    });
}

function callResources(fetchInfo, successCallback, failureCallback) {
  // Fetch the tail numbers from the Plane data model
  fetch(baseUrl + 'plane-data/')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
      // Process the API response and transform it into FullCalendar event format
      var resources = data.map(function (apiEvent) {
        return {
          title: apiEvent.TailNumber,
        }
      });
      console.log(resources);
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
