// get markdown table of content


function markdown_toc(raw) {
    
    var md = require("markdown-it")({
        html: false,
        xhtmlOut: true,
        typographer: true
    }).use(require("markdown-it-anchor"), { permalink: true, permalinkBefore: true, permalinkSymbol: '§' })
        .use(require("markdown-it-toc-done-right"));
  
    var toc = md.render(raw);
    console.log(toc)
    return toc;
}

export default markdown_toc;