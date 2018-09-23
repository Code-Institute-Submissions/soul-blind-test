setTimeout(function () {
    document.getElementById('submitGuess').click();
}, 30000);

let x = setInterval(function () {
    let currentSecs = $('#seconds').text();
    let newSecs = Number(currentSecs) > -1 ? Number(currentSecs) - 1: 0;
    $('#seconds').text(newSecs.toString());

}, 1000);

if (Number($('#seconds').text()) === 0) {
    clearInterval(x);
}
