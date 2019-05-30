function startGame() {
    var welcome_heading = document.getElementById("welcome-heading")
    var start_area = document.getElementById("start-area")
    var level_description = document.getElementById("level-description")
    var next_button = document.getElementById("next-button")
    welcome_heading.style.display = "none"
    start_area.style.display = "none"
    level_description.style.display = "block"
    eel.startGame()(displayLevelDescription)
    next_button.style.display = "block"
}

eel.expose(next);
function next(){
    eel.getNextLevel()(displayLevelDescription)
}
function displayLevelDescription(description){
    var description_text = document.getElementById("description-text")
    description_text.innerHTML = description;
}

function encyclopedia(){
    eel.getEncyclopedia()(displayEncyclopedia)
}

function displayEncyclopedia(enc){
    var encyclopedia = document.getElementById("encyclopedia")
    var welcome_heading = document.getElementById("welcome-heading")
    var start_area = document.getElementById("start-area")
    welcome_heading.style.display = "none"
    start_area.style.display = "none"
    encyclopedia.style.display = "block"
    encyclopedia.innerHTML = enc
}


function startLevels(){
    eel.startLevels()
}