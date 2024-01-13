const editor = document.getElementById("editor")
const numberLine = document.getElementById("numberLine")

function changeLines() {
    const lines = editor.value.split("\n")
    const numberHTML = lines.map((_, i) => `<div>${i+1}</div>`).join("")
    numberLine.innerHTML = numberHTML
}

editor.addEventListener("keydown", function(e){
    if (e.key == 'Tab') {
        e.preventDefault()
        var start = this.selectionStart
        var end = this.selectionEnd

        if (isTab == 0) {
            this.value = this.value.substring(0, start) + "    " + this.value.substring(end)
            this.selectionStart =
            this.selectionEnd = start + 4
        } else {
            this.value = this.value.substring(0, start) + "\t" + this.value.substring(end)
            this.selectionStart =
            this.selectionEnd = start + 1
        }

    }
})

const changeSpacingButton = document.getElementById("changeSpacingButton")
let isTab = 0
changeSpacingButton.addEventListener("click", function(){
    if (isTab == 0) {
        isTab = 1
        changeSpacingButton.innerHTML = "4 spaces"
    } else {
        isTab = 0
        changeSpacingButton.innerHTML = "Tabs"
    }
})