let saldo = 50
let seedCount = 0;

const second = 1000

const game = document.getElementById("game")
const money = document.getElementById("money")
const earth = document.getElementById("earth")
const water = document.getElementById("water")
const bird = document.getElementById("bird")
const sunflower = document.getElementById("sunflower")
const counterDisplay = document.getElementById("counter-sunflower");

const stages = ["sunflower_level_one.png", "sunflower_level_two.png", "sunflower_level_three.png", "sunflower_level_four.png", "sunflower_level_five.png","sunflower_level_six.png"];

class Plant {
    static idCounter = 0;
    static allPlants = [];

    constructor(x,y) {
        let element = document.createElement("img");
        element.src = "assets/sunflower_level_one.png";
        element.classList.add("plant");
        element.style.left = `${x}px`;
        element.style.top = `${y}px`;
        
        this.id = Plant.idCounter++
        this.stage = 0
        this.element = element
        
        element.setAttribute("id",this.id)
        Plant.allPlants.push(this);
        earth.appendChild(element)

        this.element.addEventListener("click",(e)=>{
            if(this.stage == 5){
                e.stopPropagation();
                showAlert("+ R$ 40,00")
                saldo += 37
                money.innerText = `R$ ${saldo.toFixed(2).replace(".", ",")}`;
                earth.removeChild(this.element)
            }
        })
    }

    grow() {
        if (this.stage < stages.length-1) {
            this.stage++;
  
            this.element.src = "assets/" + stages[this.stage];
            showAlert("+1✨");
        } else {
            showAlert("A planta está madura!");
        }
    }
}


function showAlert(message, duration = 3000) {
    const alertBox = document.getElementById("custom-alert");
    alertBox.textContent = message;
    alertBox.style.display = "block";

    setTimeout(() => {
        alertBox.style.display = "none";
    }, duration);
}

document.addEventListener("DOMContentLoaded",()=>{
    water.addEventListener("click", ()=>{
        if (saldo >= 5) {
            saldo -= 5;
            money.innerText = `R$ ${saldo.toFixed(2).replace(".", ",")}`;
            const rain = document.querySelectorAll(".rain");
            rain.forEach(drop => {
                drop.style.display = "initial";
            });
            rain.display = "initial"
            setTimeout(()=>{
                rain.forEach(drop => {
                    drop.style.display = "none";
                });
                Plant.allPlants.forEach(plant => plant.grow());
            },second * 3)
        }else{
            showAlert("Saldo insuficiente!")
        }
    });

    earth.addEventListener("click", function(event) {
        if(seedCount > 0) {
            seedCount--;
            counterDisplay.innerText = seedCount;
            let rect = this.getBoundingClientRect();
            let x = event.clientX - rect.left - 40;
            let y = event.clientY - rect.top - 220;
            
            if(y < -192){return}
            y > -50 ? y = -50:y
            y < -170 ? y = -170:y
            new Plant(x=x,y=y)
        }else{
            showAlert("Você não possui nenhuma semente!")
        }
    
    });
    
    if (money) {
        money.innerText = `R$ ${saldo.toFixed(2).replace(".", ",")}`;
    } else {
        console.error("Elemento com ID 'money' não encontrado!");
    }
})

bird.addEventListener("click", ()=>{
    console.log("Passáro baleado!")

    let computedStyle = window.getComputedStyle(bird);
    let topValue = computedStyle.getPropertyValue("top");
    let leftValue = computedStyle.getPropertyValue("left");

    bird.style.left = leftValue;
    bird.style.top = topValue;

    bird.classList.remove("animate");
    bird.classList.add("fall");

    setTimeout(() => {
        bird.classList.remove("fall"); 
    }, second*2);
});


function startBirdAnimation() {
    const randomTime = Math.random() * (second*30) + second*10;

    setTimeout(() => {
        bird.classList.add("animate");
        
        setTimeout(() => {
            bird.classList.remove("animate");
            startBirdAnimation();
        }, second*20);
    }, randomTime);

}

document.addEventListener("DOMContentLoaded", startBirdAnimation);


sunflower.addEventListener("click", () => {
    if (saldo >= 12) {
        saldo -= 12;
        money.innerText = `R$ ${saldo.toFixed(2).replace(".", ",")}`;
        seedCount++; 
        counterDisplay.innerText = seedCount;
    }else{
        showAlert("Saldo insuficiente!")
    }
});
