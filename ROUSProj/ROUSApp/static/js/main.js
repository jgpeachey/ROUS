let starttime;
let baseUrl = 'http://127.0.0.1:8000/';


document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        timeZone: 'local',
        events: function (fetchInfo, successCallback, failureCallback) {
            callCalendar(fetchInfo, successCallback, failureCallback);

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
            right: 'multiMonthYear,dayGridMonth,dayGridWeek,dayGridDay',
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
            alert(info.event.title + " end is now " + info.event.end.toISOString().substring(0, 10));

            if (!confirm("is this okay?")) {
                info.revert();
            }
            else {
                resizeEvent(info);
            }

        },
        eventDragStart: function (info) {
            starttime = info.event.start.toISOString().substring(0, 10);
        },
        eventDrop: function (info) {

            alert(info.event.title + " was dropped on " + info.event.start.toISOString().substring(0, 10));

            if (!confirm("Are you sure about this change?")) {
                info.revert();
            }
            else {
                dropEvent(info);
            }

        },
        eventClick: function (info) {
            alert('Event: ' + info.event.title);
        },
        eventMouseEnter: function (info) {
            if (info.event) {
                var tooltipContent = '<div><strong>' + info.event.extendedProps.aircraft.TailNumber + '</strong></div>';
                tooltipContent += '<div>Plane Serial Number: ' + info.event.extendedProps.aircraft.PlaneSN + '</div>';
                tooltipContent += '<div>MDS: ' + info.event.extendedProps.aircraft.MDS + '</div>';
                tooltipContent += '<div>Geo Location: ' + info.event.extendedProps.aircraft.GeoLoc + '</div>';
                tooltipContent += '<div>Equipment ID: ' + info.event.extendedProps.aircraft.EQP_ID + '</div>';
                tooltipContent += '<div>Work Unit Code/Logistics Control Number: ' + info.event.extendedProps.aircraft.WUC_LCN + '</div>';

                var tooltipInstance = new bootstrap.Tooltip(info.el, {
                    title: tooltipContent,
                    html: true,
                    placement: 'top',
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
            }

        },

    });

    calendar.render();
});


function callCalendar(fetchInfo, successCallback, failureCallback) {
    // Make an API call to retrieve the events
    // Replace 'YOUR_API_ENDPOINT' with the actual API endpoint URL
    fetch(baseUrl + 'calendar/')
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // Process the API response and transform it into FullCalendar event format
            var events = data.map(function (apiEvent) {
                return {
                    title: apiEvent.title,
                    start: apiEvent.start,
                    end: apiEvent.end,
                    // Include additional data beyond basic event properties
                    // You can store any custom data as additional properties
                    // For example:
                    Aircraft: apiEvent.Aircraft,
                    JulianDate: apiEvent.JulianDate,
                    EHours: apiEvent.EHours,
                    FHours: apiEvent.FHours,
                    aircraft: apiEvent.aircraft,

                    // ... and so on
                };
            });

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
    var eventId = info.event.extendedProps.Aircraft;
    var newStart = info.event.start.toISOString().substring(0, 10);
    var newEnd = info.event.end.toISOString().substring(0, 10);

    fetch(baseUrl + 'calendar/' + eventId + '/' + starttime + '/', {
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
    var eventId = info.event.extendedProps.Aircraft;
    var newStart = info.event.start.toISOString().substring(0, 10);
    var newEnd = info.event.end.toISOString().substring(0, 10);


    fetch(baseUrl + 'calendar/' + eventId + '/' + starttime + '/', {
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
