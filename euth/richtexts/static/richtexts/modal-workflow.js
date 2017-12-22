// take from wagtail

(function ($) {
  /* A framework for modal popups that are loaded via AJAX, allowing navigation to other
   subpages to happen within the lightbox, and returning a response to the calling page,
   possibly after several navigation steps
   */
  function ModalWorkflow (opts) {
    /* options passed in 'opts':
     'url' (required): initial
     'responses' (optional): dict of callbacks to be called when the modal content
     calls modal.respond(callbackName, params)
     */

    var self = {}
    var responseCallbacks = opts.responses || {}

    /* remove any previous modals before continuing (closing doesn't remove them from the dom) */
    $('body > .modal').remove()

    // set default contents of container
    var container = $('<div class="modal fade" tabindex="-1" role="dialog" aria-hidden="true">\n    <div class="modal-dialog">\n        <div class="modal-content">\n            <button type="button" class="button close icon text-replace icon-cross" data-dismiss="modal" aria-hidden="true">&times;</button>\n            <div class="modal-body"></div>\n        </div><!-- /.modal-content -->\n    </div><!-- /.modal-dialog -->\n</div>')

    // add container to body and hide it, so content can be added to it before display
    $('body').append(container)
    container.modal('hide')

    self.body = container.find('.modal-body')

    self.loadUrl = function (url, urlParams) {
      $.get(url, urlParams, self.loadBody, 'html')
    }

    self.postForm = function (url, formData) {
      $.post(url, formData, self.loadResponse)
    }

    self.ajaxifyForm = function (formSelector) {
      $(formSelector).each(function () {
        var action = this.action
        $(this).submit(function () {
          self.postForm(action, $(this).serialize())
          return false
        })
      })
    }

    self.loadResponse = function (response, status, xhr, dataType) {
      // TODO: handle network errors here
      const contentType = xhr.getResponseHeader('content-type')

      if (contentType === 'text/html') {
        self.loadBody(response)
      } else if (contentType === 'application/json') {
        for (var key in response) {
          if (response.hasOwnProperty(key)) {
            self.respond(key, response[key])
            self.close()
          }
        }
      }
    }

    self.loadBody = function (response, status) {
      // TODO: handle network errors here

      self.body.html(response)
      self.ajaxifyForm('.modal form')
      container.modal('show')
    }

    self.respond = function (responseType) {
      if (responseType in responseCallbacks) {
        var args = Array.prototype.slice.call(arguments, 1)
        responseCallbacks[responseType].apply(self, args)
      }
    }

    self.close = function () {
      container.modal('hide')
    }

    self.loadUrl(opts.url, opts.urlParams)

    return self
  }

  window.ModalWorkflow = ModalWorkflow
})(window.jQuery)
