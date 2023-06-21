document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    fetch('http://127.0.0.1:8000/calendar/')
        .then(function (response) {
            console.log(response.json());
            return response;
        })
        .then(function (events) {
            var calendar = new FullCalendar.Calendar(calendarEl, {
                timeZone: 'local',
                events: events,
                themeSystem: 'bootstrap5',
                initialView: 'dayGridMonth',
                editable: true,
                eventResourceEditable: true,
                droppable: true,
                headerToolbar: {
                    left: 'prev,next, addEventButton',
                    center: 'title',
                    right: 'dayGridMonth,dayGridWeek,resourceTimelineWeek',
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

            });
            calendar.render();
        });
});