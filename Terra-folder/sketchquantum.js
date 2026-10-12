let electronDx = 180;
function setup() {
    createCanvas(600, 400);

}

function draw() {
    background(15, 20, 35);

    stroke(0, 220, 255);
    strokeWeight(4);



    //energy level 1 (n = 1)
    line(100, 300, 500, 300);
    //energy level 2 (n = 2)
    line(100, 200, 500, 200);
    //energy level 3(n = 3)
    line(100, 100, 500, 100);

    fill(235, 240, 250);
    noStroke();
    textSize(18);
    textAlign(LEFT);

    text("n= 1", 110, 295);
    text("n= 2", 110, 195);
    text("n= 3", 110, 95);

    fill(255, 190, 50);
    noStroke();
    circle(electronDx, 200, 16);

    electronDx = electronDx + 1;

    if (electronDx > 450) {
        electronDx = 150;

    }
}
