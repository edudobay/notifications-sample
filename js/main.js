const $ = require('jquery');
const toastr = require('toastr');
require('!style!css!toastr/package/toastr.css');

function main() {
    const p = $('<p>hello world</p>');
    const counter = { times: 0 };
    p.appendTo('#content')
        .on('click', () =>
            toastr.info(`This paragraph has been clicked ${++counter.times} times`));
}

$(main);
