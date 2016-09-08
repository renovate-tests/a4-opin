var $ = require('jquery')
var cookie = require('js-cookie')

$(function () {
  $.ajaxSetup({
    headers: { 'X-CSRFToken': cookie.get('csrftoken') }
  })
})

var baseURL = '/api/'

var api = (function () {
  var urls = {
    comment: baseURL + 'comments/',
    rate: baseURL + 'rates/',
    report: baseURL + 'reports/'
  }

  function _sendRequest (endpoint, id, options, data) {
    var $body = $('body')
    var url = urls[endpoint]
    if (typeof id === 'object') {
      // there's no id, switch parameters
      data = options
      options = id
    } else if (typeof id === 'number') {
      url = url + id + '/'
    }
    var defaultParams = {
      url: url,
      dataType: 'json',
      data: data,
      error: function (xhr, status, err) {
        console.error(url, status, err.toString())
      },
      complete: function () {
        $body.removeClass('loading')
      }
    }
    var params = $.extend(defaultParams, options)

    $body.addClass('loading')
    return $.ajax(params)
  }

  return {
    comments: {
      get: function (data) {
        return _sendRequest('comment', {
          cache: false,
          type: 'GET'
        }, data)
      },

      add: function (data) {
        return _sendRequest('comment', {
          type: 'POST'
        }, data)
      },

      change: function (data, id) {
        return _sendRequest('comment', id, {
          type: 'PATCH'
        }, data)
      },

      delete: function (id) {
        return _sendRequest('comment', id, {
          type: 'DELETE'
        })
      }
    },
    rate: {
      add: function (data) {
        return _sendRequest('rate', {
          type: 'POST'
        }, data)
      },
      change: function (data, id) {
        return _sendRequest('rate', id, {
          type: 'PATCH'
        }, data)
      }
    },
    report: {
      submit: function (data) {
        return _sendRequest('report', {
          type: 'POST'
        }, data)
      }
    }
  }
}())
module.exports = api