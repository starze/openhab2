//helper script for extracting channellist out of paperui and include it into basic-ui sitemap items (drop-down in basic-ui doesn't fill up from kodi automatically).
//usage: start openhab paper-ui and use chrome developper tools f12 to find drop-downs. use vs-code editor to get a list of channels each in one line.

const file = "./radiosenderliste";

let outString="";

var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream(file)
});
  
lineReader.on('line', function (line) {
  if (line !== "") {
      console.log(line);
      outString+=`"${line}"="${line}",`
  }
});

lineReader.input.on("end", () => {
  console.log(outString);
  require('fs').writeFileSync("out.txt", outString);
});
