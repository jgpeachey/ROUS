let starttime;
let dropdown;
let baseUrl = 'http://127.0.0.1:8000/'; //'rousapp.com';

const container = document.getElementById('dropdownContainer');


document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('calendar')) {
        var calendarEl = document.getElementById('calendar');

        // Retrieve the selected GeoLoc from the URL parameter
        const urlParams = new URLSearchParams(window.location.search);
        const selectedGeoLoc = urlParams.get('geoloc');


        var calendar = new FullCalendar.Calendar(calendarEl, {
            schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
            timeZone: 'local',
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
                right: 'multiMonthYear,dayGridMonth,dayGridWeek,dayGridDay,resourceTimelineWeek',
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
                        title: 'swal-title'
                    }
                }).then((result) => {
                    if (result.isConfirmed) {
                        dropEvent(info);
                        Swal.fire('Success', 'Event dropped.', 'success');
                    } else {
                        info.revert();
                    }
                });

            },
            eventClick: function (info) {
                handleEventClick(info);
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
                    JulianDate: apiEvent.JulianDate,
                    EHours: apiEvent.EHours,
                    FHours: apiEvent.FHours,
                    maintenance: apiEvent.maintenance,
                    PartMaintenanceID: apiEvent.PartMaintenanceID,
                    PlaneMaintenanceID: apiEvent.PlaneMaintenanceID,
                    GeoLoc: apiEvent.GeoLoc,
                    CalendarID: apiEvent.CalendarID,
                    planeData: apiEvent.plane_data,

                };
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

function dropEvent(info) {
    // Retrieve the updated event details
    var eventId = info.event.extendedProps.CalendarID;
    var newStart = info.event.start.toISOString().substring(0, 10);
    var newEnd = info.event.end.toISOString().substring(0, 10);

    fetch(baseUrl + 'calendar/' + eventId, {
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


    fetch(baseUrl + 'calendar/' + eventId, {
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

function handleEventClick(info) {
    var event = info.event;

    // Populate event details in the modal
    document.getElementById('eventTitle').innerHTML = event.title;
    document.getElementById('eventStart').innerHTML = 'Start: ' + event.start;
    document.getElementById('eventEnd').innerHTML = 'End: ' + event.end;

    // Show the modal
    var modal = document.getElementById('eventModal');
    modal.style.display = 'block';

    // Handle edit button click
    var editButton = document.getElementById('editButton');
    editButton.addEventListener('click', function () {
        // Handle editing functionality
        var newTitle = prompt('Enter a new title', event.title);
        if (newTitle) {
            event.setProp('title', newTitle);
            // Update the displayed title in the modal
            document.getElementById('eventTitle').innerHTML = newTitle;
            // You can also update other properties and their display here if needed
        }
    });

    // Close the modal when the close button is clicked
    var closeBtn = document.getElementsByClassName('close')[0];
    closeBtn.addEventListener('click', function () {
        modal.style.display = 'none';
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
