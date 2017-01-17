// Avoid `console` errors in browsers that lack a console.
(function() {
    var method;
    var noop = function () {};
    var methods = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn'
    ];
    var length = methods.length;
    var console = (window.console = window.console || {});

    while (length--) {
        method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
            console[method] = noop;
        }
    }
}());

// Place any jQuery/helper plugins in here.

window.onload = function() {
    var tables = document.querySelectorAll('table');
    for(var i = 0 ; i < tables.length ; i++) {
        if(!tables[i].classList.contains('pure-table')) {
            tables[i].classList.add('pure-table');
        }
    }

    var press = document.querySelector('.press-content');
    if(press !== null) {
        var imgs = press.querySelectorAll('img');
        for(var i = 0 ; i < imgs.length ; i++) {
            imgs[i].classList.add('pure-img');
        }
    }

};
