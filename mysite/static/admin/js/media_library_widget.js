const image_url_field = document.getElementById('id_image')

image_url_field.insertAdjacentHTML(
    'afterend',
    '<span><button id="open-btn">Choose File</button></span>'
)

window.ml = cloudinary.createMediaLibrary(
    {
        cloud_name: 'dkc5rsxrn',
        api_key: '837991189459538',
        // username: '{{ cloudinary_user }}',
        // timestamp: '{{ timestamp }}',
        // signature: '{{ signature }}', // signature has cross site cookie issues
        multiple: false,
        z_index: 100,
        remove_header: true,
        // button_class: 'btn btn-primary',
        button_caption: 'Choose File'
    },
    {
        insertHandler: function (data) {
            data.assets.forEach((asset) => {
                // console.log('Inserted asset:', JSON.stringify(asset, null, 2))

                function getFileUrl() {
                    if (asset.derived) {
                        return asset.derived[0].secure_url
                    } else {
                        return asset.secure_url
                    }
                }

                image_url_field.value = getFileUrl()
                window.ml.hide()
            })
        }
    },
    // document.getElementById('open-btn')
    '#open-btn'
)
