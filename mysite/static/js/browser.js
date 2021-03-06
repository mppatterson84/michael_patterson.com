window.ml = cloudinary.openMediaLibrary(
    {
        cloud_name: 'dkc5rsxrn',
        api_key: '837991189459538',
        // username: '{{ cloudinary_user }}',
        // timestamp: '{{ timestamp }}',
        // signature: '{{ signature }}', // signature has cross site cookie issues
        multiple: false,
        z_index: 1,
        inline_container: '.ml-widget',
        remove_header: true
    },
    {
        insertHandler: function (data) {
            data.assets.forEach((asset) => {
                console.log('Inserted asset:', JSON.stringify(asset, null, 2));

                function getUrlParam(paramName) {
                    var reParam = new RegExp(
                        '(?:[?&]|&)' + paramName + '=([^&]+)',
                        'i'
                    );
                    var match = window.location.search.match(reParam);

                    return match && match.length > 1 ? match[1] : null;
                }

                function getFileUrl() {
                    if (asset.derived) {
                        return asset.derived[0].secure_url;
                    } else {
                        return asset.secure_url;
                    }
                }

                function copyURL() {
                    let selBox = document.createElement('textarea');
                    selBox.style.position = 'fixed';
                    selBox.style.left = '0';
                    selBox.style.top = '0';
                    selBox.style.opacity = '0';
                    selBox.value = fileUrl;
                    document.body.appendChild(selBox);
                    selBox.focus();
                    selBox.select();
                    document.execCommand('copy');
                    document.body.removeChild(selBox);
                }

                function ckeditorWindow() {
                    var field = 'CKEditor';
                    var url = window.location.href;
                    if (url.indexOf('?' + field + '=') != -1) return true;
                    else if (url.indexOf('&' + field + '=') != -1) return true;
                    return false;
                }

                var funcNum = getUrlParam('CKEditorFuncNum');
                var fileUrl = getFileUrl();
                console.log(fileUrl);
                if (ckeditorWindow()) {
                    window.opener.CKEDITOR.tools.callFunction(funcNum, fileUrl);
                    window.close();
                } else {
                    copyURL();
                    alert(`URL copied to clipboard.\n'${fileUrl}'`);
                }
            });
        }
    }
);
