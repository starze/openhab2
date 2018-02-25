// Wrap everything in a function
(function(i) {
    // shape negative values
    i -= (i > 0x8000) ? 0xFFFF : 0x00;

    // do the division
    return parseFloat(i) / 100;
})(input)
// input variable contains data passed by openhab
