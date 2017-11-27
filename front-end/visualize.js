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
        displayGrid(start, end, centers, terrain)
        if (rows.length <= 130) return

        f = []
        g = []
        h = []
        for (i = 130; i < 250; i++){
            f.push(rows[i].split(','))
        }
        for (i = 251; i < 371; i++){
            g.push(rows[i].split(','))
        }
        for (i = 372; i < 492; i++){
            h.push(rows[i].split(','))
        }

        path = rows[493]
        path = path.substring(1,path.length-1).split('),(')
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
    draw.clearRect(0, 0, canvas.width, canvas.height);
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
    console.log(path)
    path.forEach(function(val, index) {
        if (index != 0){
            coords = val.split(', ')
            displayCell(coords[1],coords[0],'red')
        }
    })
}

function updateFGH(event) {
    x = event.pageX - canvas.offsetLeft
    y = event.pageY - canvas.offsetTop
    r = Math.floor(y / CELL_SIZE)
    c = Math.floor(x / CELL_SIZE)

    if (r >= 0 && r < 120 && c >= 0 && c < 160) {
        document.getElementById("f").innerHTML = f[r][c]
        document.getElementById("g").innerHTML = g[r][c]
        document.getElementById("h").innerHTML = h[r][c]
    }

    //console.log(r,c)
}

window.onload = function() {
    canvas = document.getElementById("grid")
    canvas.addEventListener('mousemove', updateFGH)
    draw = canvas.getContext("2d")
    draw.globalAlpha = 0.7
    draw.lineWidth = 0.1
    document.getElementById("gridSelect").addEventListener('change', process, false)
}