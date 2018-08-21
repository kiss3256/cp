var request = require('request');
var cheerio = require('cheerio');
var fs      = require('fs');


var rootPath = 'data/cqssc/'

var headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    // 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    // 'Referer': 'http://caipiao.163.com/award/cqssc/20180702.html',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'text/html; charset=UTF-8',
    // 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    // 'Cookie': '_ntes_nnid=2a49880019255af6f8fc713b80c05ed5,1531569973413; _ntes_nuid=2a49880019255af6f8fc713b80c05ed5; JSESSIONID=abc9uKXvZa5gA_gJI0ouw; JSESSIONID-WYBM=^%^2FLn75niDVXBkF7JqTlagpZUWCfW^%^2FXa7o0V9ug8sK8LWjPtxGyCt^%^2FM9Y1H0TMtbsla8F0dDbbP03m9^%^2FS4fStnOSVfoBIdAWsiZCllAmbWFShtHAPPFECxifKmWm0Nbz9XK0JdPIoFCbHMxbkhHi33kzaMqQ^%^2BKflrNUoPaCxSZ2MypeD^%^5Ch^%^3A1533645576306; _78x8309xiuyl_=31; ne_analysis_trace_id=1533552230584; s_n_f_l_n3=7ccad9d4a87d42161533552230595; vinfo_n_f_l_n3=7ccad9d4a87d4216.1.2.1533552230586.1533552230586.1533552262608; pgr_n_f_l_n3=7ccad9d4a87d421615335522515044149; nteslogger_exit_time=1533552262610'
};



function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
        var fileName = response.req.path.match(/\d+/)[0];

        var $ = cheerio.load(body);
        var data = [];
        $('.award-winNum').map(function() {
            var element = cheerio(this).prev();
            data.push(element.data());
        });
        setTimeout(function() {
            fs.writeFile(rootPath + fileName, JSON.stringify(data), function(err) {
                if (err) { throw err; }
            });
        }, 0);
        
    }
}


function format(a) {
    return (a < 10 ? '0' : '') + a
}

(function fetch() {

    var days = 8960;
    for (var i = 0; i < days; i++) {
        var date = new Date('2016-01-01');
        date.setDate(date.getDate() + i);
        theDay = '' + date.getFullYear() + format(date.getMonth() + 1) + format(date.getDate());

        var options = {
            url: 'http://caipiao.163.com/award/cqssc/'+theDay+'.html',
            headers: headers,
            gzip: true
        };

        request(options, callback);
    }

})()

