// Wrap everything in a function
(function(i) {
    
    // date is a bit word packet in dos format
    // year 0 = 1980
    // 15      8  7       0
    // YYYY YYYM  MMMD DDDD
    //example: 19129 means may 25th 2016

    var year = ((i & 65024) >> 9) + 1980;
    var month = ((i & 480) >> 5);
    var day = (i & 31);

    var result = day + "." + month + "." + year;
    
    return result;
})(input)
// input variable contains data passed by openhab