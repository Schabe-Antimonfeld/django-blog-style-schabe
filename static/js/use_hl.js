function removePrefix(str, prefix) {
    if (str.startsWith(prefix)) {
        return str.replace(new RegExp('^' + prefix), '');
    }
    return str;
}

$(document).ready(function () {
    hljs.highlightAll();
    hljs.initLineNumbersOnLoad();
    $('pre > code').each(function () {
        // 查找语言（以md中指定的为主，没有则设置为hljs识别结果）
        var language = "code", curLanguage = "code";
        var classes = $(this).attr('class').split(/\s+/);
        $.each(classes, function (index, className) {
            if (className.startsWith('lang-')) {
                language = removePrefix(className, 'lang-');
            }
            if (className.startsWith('language-')) {
                curLanguage = removePrefix(className, 'language-');
            }
        });

        if (language == "code") {
            language = curLanguage;
        }

        $(this).addClass('codeSnippet rounded bg-light');
        $(this).wrap('<div class="p-1 border rounded"></div>');
        $(this).before(
            `<div class="mb-1 d-flex align-items-center">
                <small class="ms-2 font-monospace text-muted text-uppercase">${language}</small>
                <div class="d-flex ms-auto">
                    <button type="button" class="btn btn-sm btn-outline-primary copyButton"><i class="bi bi-clipboard"></i></button>
                </div>
            </div>`
        );
    });
});

// 代码复制按钮
$(document).ready(function () {
    $('.copyButton').click(function () {
        var $button = $(this);  // 缓存按钮
        var codeElement = $button.parent().parent().next('.codeSnippet')[0];

        var codeLines = [];
        $(codeElement).find('.hljs-ln-code').each(function () {
            codeLines.push($(this).text());
        });

        var codeContent = codeLines.join('\n')
            .replace(/\u200b/g, '')
            .replace(/\n\n/g, '\n')
            .trim();

        navigator.clipboard.writeText(codeContent)
            .then(function () {
                const originalHtml = $button.html();
                $button.html('<i class="bi bi-check-lg check-animate"></i>')
                    .removeClass('btn-outline-primary')
                    .addClass('btn-success');

                setTimeout(() => {
                    $button.html(originalHtml)
                        .removeClass('btn-success')
                        .addClass('btn-outline-primary');
                }, 1500);
            })
            .catch(function (err) {
                console.error('复制失败:', err);
            });
    });
});
