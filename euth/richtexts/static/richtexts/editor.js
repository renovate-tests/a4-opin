(function ($) {
  let Quill = window.Quill
  let BlockEmbed = Quill.import('blots/block/embed')

  class A4ImageBlot extends BlockEmbed {
    static create (value) {
      let node = super.create()
      node.setAttribute('alt', value.alt)
      node.setAttribute('src', value.url)
      node.setAttribute('class', ['a4image-blot', value.style || ''].join(' '))
      return node
    }

    static value (node) {
      return {
        alt: node.getAttribute('alt'),
        url: node.getAttribute('src'),
        style: node.getAttribute('style')
      }
    }
  }
  A4ImageBlot.blotName = 'a4image'
  A4ImageBlot.tagName = 'img'

  Quill.register(A4ImageBlot)

  $(function () {
    var quill = new Quill('.richtext', {
      modules: {
        toolbar: [
          ['bold', 'italic'],
          ['link', 'blockquote'],
          ['a4image'],
          [{ list: 'ordered' }, { list: 'bullet' }]
        ]
      },
      theme: 'snow'
    })

    var toolbar = quill.getModule('toolbar')
    toolbar.addHandler(
      'a4image',
      function selectImage () {
        window.ModalWorkflow({
          url: '/richtexts/uploadimage',
          urlParams: {},
          responses: {
            imageChosen: function (imageData) {
              let range = quill.getSelection(true)
              quill.insertText(range.index, '\n', Quill.sources.USER)
              quill.insertEmbed(range.index + 1, 'a4image', imageData, Quill.sources.USER)
              quill.setSelection(range.index + 2, Quill.sources.SILENT)
            }
          }
        })
      }
    )

    // ensure that hidden input is updated on form submit
    var form = $('.richtext').closest('form')
    form.submit(function () {
      // FIXME: remove hardcoded hidden field
      var hiddenInput = document.querySelector('input[name=text]')
      hiddenInput.value = JSON.stringify(quill.getContents())
    })
  })
})(window.jQuery)
