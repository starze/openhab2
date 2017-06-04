// Wrap everything in a function
(function(i) {
    
    // alarm time is a bit word packet in dos time format
    // Seconds are in scale 2 (0..29 = 0..58 seconds)
    // 15      8  7       0
    // HHHH HMMM  MMMS SSSS
    //example: 10857 means 

    var hour = ((i & 63488) >> 11);
    var minute = ((i & 2016) >> 5);
    var second = (i & 31) * 2;

    var result = hour + ":" + minute + ":" + second;
    
    return result;
})(input)
// input variable contains data passed by openhab