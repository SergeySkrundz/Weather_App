async function display_weather() {
    let place = document.getElementById('location').value;

    let res = await eel.get_place(place)();
    document.getElementById('place').innerHTML = res;

    let res1 = await eel.get_day()();
    document.getElementById('day').innerHTML = res1;
    
    let res2 = await eel.get_date()();
    document.getElementById('date').innerHTML = res2;

    let res3 = await eel.get_temp(place)();
    document.getElementById('temp').innerHTML = res3;

    let res4 = await eel.get_status(place)();
    document.getElementById('status').innerHTML = res4;

    let res5 = await eel.get_clouds(place)();
    document.getElementById('clouds').innerHTML = res5;

    let res6 = await eel.get_wind(place)();
    document.getElementById('wind').innerHTML = res6;

    let res7 = await eel.get_humidity(place)();
    document.getElementById('humidity').innerHTML = res7;

    let res8 = await eel.get_barometric(place)();
    document.getElementById('barometric').innerHTML = res8;

    let res9 = await eel.get_rain(place)();
    document.getElementById('rain').innerHTML = res9;

    let res10 = await eel.get_distance(place)();
    document.getElementById('distance').innerHTML = res10;
}


jQuery('#show').on('click', function() {
    display_weather();
});

$(document).keypress(function(e) {
    if(e.which == 13) {
        display_weather();
    }
});