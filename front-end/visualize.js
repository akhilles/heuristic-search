cellSize = 7

function process(event) {
    file = event.target.files[0];
    //console.log(file);
    reader = new FileReader();
    reader.readAsText(file);
    reader.onload = function (e) {
        contents = e.target.result;
        rows = contents.split("\r\n");
        
        start = rows[0].split(',').map(Number)
        end = rows[1].split(',').map(Number)
        centers = []
        terrain = []
        
        for (i = 2; i < 10; i++){
            centers.push(rows[i].split(',').map(Number))
        }

        for (i = 10; i < rows.length; i++){
            terrain.push(rows[i].split(''))
        }

        console.log(start)
        console.log(end)
        console.log(centers)
        console.log(terrain)

        displayGrid(start, end, centers, terrain)
    }
}

function displayCell(x, y, color) {
    draw.beginPath()
    draw.rect(cellSize*x, cellSize*y, cellSize, cellSize)
    draw.fillStyle = color
    draw.fill()
    draw.stroke()
}

function displayGrid(start, end, centers, terrain) {
    terrain.forEach(function(row, y) {
        row.forEach(function(type, x) {
            color = '#686868'
            switch(type) {
                case '1': color = 'white'; break;
                case '2': color = '#d6d6d6'; break;
                case 'a': color = '#4f92ff'; break;
                case 'b': color = '#1d3660'; break;
            }
            displayCell(x,y,color)
        })
    })

    displayCell(start[1], start[0], 'green')
    displayCell(end[1], end[0], 'red')
}

window.onload = function() {
    draw = document.getElementById("grid").getContext("2d")
    draw.lineWidth = 0.1
    document.getElementById("gridSelect").addEventListener('change', process, false)
}