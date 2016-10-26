function showTime() {
    var today = new Date();
    var releaseDate = new Date("November 16, 2016 12:00:00");
    var diff = (releaseDate - today);
    var dayInMilliseconds = 24 * 60 * 60 * 1000;
    var hourInMilliseconds = 60 * 60 * 1000;
    var minuteInMilliseconds = 60 * 1000;
    var secondInMilliseconds = 1000;
    var day = Math.floor(diff / dayInMilliseconds);
    var hour = Math.floor( (diff - day * dayInMilliseconds) / hourInMilliseconds);
    var minute = Math.floor( (diff - day * dayInMilliseconds - hour * hourInMilliseconds) / minuteInMilliseconds);
    var second = Math.floor( (diff - day * dayInMilliseconds - hour * hourInMilliseconds - minute * minuteInMilliseconds) / secondInMilliseconds);
        
    hour = formatTime(hour);
    minute = formatTime(minute);
    second = formatTime(second);
        
    document.getElementById('clock-large').innerHTML = 
        day + " : " + hour + " : " + minute + " : " + second;
}

function formatTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}
setInterval(showTime, 500);