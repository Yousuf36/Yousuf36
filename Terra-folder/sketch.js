
let particles = [];

const G = 0.1;
const SCALE = 0.0001;

function setup() {
    createCanvas(windowWidth, windowHeight);

    for (let i = 0; i < 10; i++) {
        let x = random(0, width);
        let y = random(0, height);
        let mass = random(2e8, 1e9);

        particles.push(new particles(x, y, mass));
    }
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
}

function draw() {
    background(51);

    for (const particleA of particles) {
        for (const particleB of particles) {
            if (particleA !== particleB) {
                particleA.physics(particleB);
            }
        }
    }

    for (const particle of particles) {
        particle.update();
        particle.draw();
    }
}

