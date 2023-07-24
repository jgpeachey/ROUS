//import { passgeoloc } from './main.js'

let base = 'http://127.0.0.1:8000/';

// waits until page has loaded to make changes
window.onload = () => {
    const selectedGeoLoc = urlParams.get('geoloc');
    loadTable(selectedGeoLoc);
}

async function loadTable(selectedGeoLoc) {
    // gets all planes from current GeoLoc
    const tailNums = await getTailNums(selectedGeoLoc);

    // create map for their respective maintenances
    var planeMap = new Map();
    var partMap = new Map();

    // gets all maintenances and adds them to their respective map with key = TailNumber and value = array of maintenance objects
    for (let plane of tailNums) {
        let planeM = await getPlaneMaintenances(plane.TailNumber);
        let partM = await getPartMaintenances(plane.TailNumber);
        planeMap.set(plane.TailNumber, planeM);
        partMap.set(plane.TailNumber, partM);
    }

    // adds all TailNumbers as Table Heads
    loadTableHead(tailNums);
    // adds all Maintenances for their respective TailNumber
    loadTableData(planeMap, partMap, tailNums);
}

// add Tail Numbers as table heads and Part/Plane as table sub heads for each plane
function loadTableHead(tailNums) {
    // get table headings from doc
    const tableHead = document.getElementById('TailNumbers');
    const tableSubHead = document.getElementById('Plane_Part');
    // creates strings to be inserted for the tableHead and tableSubHead innerHTML
    let headHtml = '';
    let subHeadHtml = '';

    // create headings for each plane and add to future innerHTML strings
    for (let plane of tailNums) {
        headHtml += '<th colspan="2">'+plane.TailNumber+'</th>';
        subHeadHtml += '<th>Plane</th><th>Part</th>';
    }

    // add in all headings
    tableHead.innerHTML = headHtml;
    tableSubHead.innerHTML = subHeadHtml;
}

// uses GET api call to get all planes from selected GeoLoc
 async function getTailNums (selectedGeoLoc) {
    return fetch(base + 'resource/geoloc/' + encodeURIComponent(selectedGeoLoc) + '/')
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => console.warn(error));
}

// add plane/part maintenance to the table data under their designated plane
async function loadTableData(planeMap, partMap, tailNums) {
    // get table body from doc
    const tableBody = document.getElementById('Maintenances');
    // creates string to be inserted for the tableBody innerHTML
    let bodyHtml = '';

    // find largest length of the value arrays
    let length = 0;
    for (let plane of tailNums) {
        if (length < planeMap.get(plane.TailNumber).length) {
            length = planeMap.get(plane.TailNumber).length;
        }
        else if (length < partMap.get(plane.TailNumber).length) {
            length = partMap.get(plane.TailNumber).length;
        }
    }
    console.log(planeMap);
    console.log(partMap);

    // create table of size length
    for (let i = 0; i < length; i++) {
        // create table row
        bodyHtml += '<tr>'
        for (let plane of tailNums) {
            // if able to access planeMaintenance, add planeMaintenance to table with id = PlaneMaintenanceID
            try {
                // get planeMaintenance for easy access
                var maint = planeMap.get(plane.TailNumber)[i];
                bodyHtml += '<td class="maintenance-item" data-type="plane" data-maintenance="'+maint.PlaneMaintenanceID+'">Current Time: '+maint.CrntTime+'<br>';
                bodyHtml += 'Time Remaining:'+maint.TimeRemain+'<br>';
                bodyHtml += 'Due Time:'+maint.DueTime+'<br>';
                bodyHtml += 'Frequency:'+maint.Freq+'<br>';
                bodyHtml += 'Type:'+maint.Type+'<br>';
                bodyHtml += 'Justification:'+maint.JST+'<br>';
                bodyHtml += 'Time Frame:'+maint.TFrame+'<br>';
                bodyHtml += 'Engine(E)/Flight(F):'+maint.E_F+'<br>';
                bodyHtml += '</td>'
            }
            // if no planeMaintenance to access add blank row
            catch {
                bodyHtml += '<td></td>'
            }
            // if able to access partMaintenance, add partMaintenance to table with id = PartMaintenanceID
            try {
                // get partMaintenance for easy access
                var maint = partMap.get(plane.TailNumber)[i];
                bodyHtml += '<td class="maintenance-item" data-type="plane" data-maintenance="'+maint.PlaneMaintenanceID+'">Current Time: '+maint.CrntTime+'<br>';
                bodyHtml += 'Equipment ID:'+maint.EQP_ID+'<br>';
                bodyHtml += 'Part Serial Number:'+maint.PartSN+'<br>';
                bodyHtml += 'Part Number:'+maint.PartNum+'<br>';
                bodyHtml += 'WUC/LCN:'+maint.WUC_LCN+'<br>';
                bodyHtml += 'Category Number:'+maint.CatNum+'<br>';
                bodyHtml += 'Time Remaining:'+maint.TimeRemain+'<br>';
                bodyHtml += 'Due Time:'+maint.DueTime+'<br>';
                bodyHtml += 'Frequency:'+maint.Freq+'<br>';
                bodyHtml += 'Type:'+maint.Type+'<br>';
                bodyHtml += 'Justification:'+maint.JST+'<br>';
                bodyHtml += 'Time Frame:'+maint.TFrame+'<br>';
                bodyHtml += 'Engine(E)/Flight(F):'+maint.E_F+'<br>';
                bodyHtml += '</td>'
            }
            // if no partMaintenance to access add blank row
            catch {
                bodyHtml += '<td></td>'
            }
        }
        // end table row
        bodyHtml += '</tr>'
    }

    tableBody.innerHTML = bodyHtml;
}

// uses GET api call to get all plane maintenances from selected plane
async function getPlaneMaintenances(TailNumber) {
    return fetch(base + 'plane-data/' + TailNumber + '/')
    .then(response => response.json())
    .then(pdata => {
        return fetch(base + 'plane-maintenance/' + pdata.PlaneSN + '/' + pdata.MDS + '/')
        .then(response => response.json())
        .then(data => {
            return data;
        })
        .catch(error => console.warn(error));
    })
    .catch(error => console.warn(error));
}

// uses GET api call to get all part maintenances from selected plane
async function getPartMaintenances(TailNumber) {
    return fetch(base + 'plane-data/' + TailNumber + '/')
    .then(response => response.json())
    .then(pdata => {
        return fetch(base + 'part-maintenance/' + pdata.PlaneSN + '/' + pdata.MDS + '/')
        .then(response => response.json())
        .then(data => {
            return data;
        })
        .catch(error => console.warn(error));
    })
    .catch(error => console.warn(error));
}

// pops up with calendar event creation when maintenance is clicked on
async function createEvent(maintenanceType, maintenanceID) {
    
}