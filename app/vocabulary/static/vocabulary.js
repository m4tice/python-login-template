document.addEventListener('DOMContentLoaded', function() {
    fetchData();
});

function fetchData() {
    fetch('/vocabulary/data')
        .then(response => response.json())
        .then(data => {
            console.log(data.pairs);
        });
};

function createTable(data){
    console.log(data);
    // const table = document.createElement('table');
    // const headerRow = document.createElement('tr');
    // const germanHeader = document.createElement('th');
    // germanHeader.textContent = 'German';
    // const englishHeader = document.createElement('th');
    // englishHeader.textContent = 'English';
    
    // headerRow.appendChild(germanHeader);
    // headerRow.appendChild(englishHeader);
    // table.appendChild(headerRow);

    // data.forEach(pair => {
    //     const row = document.createElement('tr');
    //     const germanCell = document.createElement('td');
    //     germanCell.textContent = pair[0];
    //     const englishCell = document.createElement('td');
    //     englishCell.textContent = pair[1];

    //     row.appendChild(germanCell);
    //     row.appendChild(englishCell);
    //     table.appendChild(row);
    // });

    // document.body.appendChild(table);
};