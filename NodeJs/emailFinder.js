const request = require('request');
const cheerio = require('cheerio');

const url = 'http://sample.com'; //
request(url, (error, response, html) => {
  if (!error && response.statusCode === 200) {
    const $ = cheerio.load(html);
    const emailSet = new Set();
    const emailRegex = /\S+@\S+\.\S+/;
    $('body').find('*').each((i, element) => {
      const text = $(element).text();
      const matches = text.match(emailRegex);
      if (matches) {
        emailSet.add(matches[0]);
      }
    });
    console.log(Array.from(emailSet)); 
  }
});

// ################################################
// |                                              |
// | for more contact me : abhi-raam.github.io/   |
// |                                              |
// ################################################