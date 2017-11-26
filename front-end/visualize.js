CELL_SIZE = 7

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

        for (i = 10; i < 130; i++){
            terrain.push(rows[i].split(''))
        }

        console.log(start)
        console.log(end)

        displayGrid(start, end, centers, terrain)

        if (rows.length <= 130) return

        f = []
        g = []
        h = []

        for (i = 130; i < 250; i++){
            f.push(rows[i].split(','))
        }
        for (i = 250; i < 370; i++){
            g.push(rows[i].split(','))
        }
        for (i = 370; i < 490; i++){
            h.push(rows[i].split(','))
        }

        path = rows[490].split(',').map(Number)
        displayPath(start, path)
    }
}

function displayCell(x, y, color) {
    draw.beginPath()
    draw.rect(CELL_SIZE*x, CELL_SIZE*y, CELL_SIZE, CELL_SIZE)
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

function displayPath(start, path) {
    x = start[1]
    y = start[0]
    console.log(path)
    path.forEach(function(val) {
        switch(val) {
            case 0: y--; break;
            case 1: x++; y--; break;
            case 2: x++; break;
            case 3: x++; y++; break;
            case 4: y++; break;
            case 5: x--; y++; break;
            case 6: x--; break;
            case 7: x--; y--; break;
        }
        console.log(x,y)
        displayCell(x,y,'red')
    })
}

window.onload = function() {
    draw = document.getElementById("grid").getContext("2d")
    draw.lineWidth = 0.1
    document.getElementById("gridSelect").addEventListener('change', process, false)
}