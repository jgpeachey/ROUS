function updateData(fetchInfo, successCallback, failureCallback, selectedGeoLoc)
{
    fetch(baseUrl + 'calendar/geoloc/' + encodeURIComponent(selectedGeoLoc) + '/')
    .then(response => response.json())
    .then(data => {
      // Get today's date
      var today = new Date();

      // Filter the objects with end date prior to today's date and completed equal to false
      var filteredObjects = data.filter(obj => new Date(obj.end_date) < today && obj.completed === false);

      // Update the time for each filtered object
      filteredObjects.forEach(obj => {
        // Calculate the new times
        var newDueTime = obj.DueTime + obj.Freq;
        var newTimeRemain = obj.Freq;

        // Make a PATCH request to update the object
        if (obj.PlaneMaintenanceID > 0)
        {
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
                  console.log('Object with ID '+obj.id+' updated successfully.');
                } else {
                  console.error('Failed to update object with ID '+obj.id+'.');
                }
              })
              .catch(error => {
                console.error('An error occurred while updating object with ID '+obj.id+':', error);
              });
        }
        else if (obj.PartMaintenanceID > 0)
        {
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
                  console.log('Object with ID '+obj.id+' updated successfully.');
                } else {
                  console.error('Failed to update object with ID '+obj.id+'.');
                }
              })
              .catch(error => {
                console.error('An error occurred while updating object with ID '+obj.id+':', error);
              });
        }
      });
    })
    .catch(error => {
      console.error('An error occurred while fetching the objects:', error);
    });
}

// make function to delete calendar events after a year