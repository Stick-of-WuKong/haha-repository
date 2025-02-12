const CACHE_HOST = {}


function getHostname(url) {
  let elem = document.createElement('a')
  elem.href = url
  return elem.hostname
}


// Save host info to cache, and only store what is needed
function saveCache(hostname, host) {
  const keys = ['ip', 'hostnames', 'ports', 'tags', 'vulns']

  let smallerHost = {}
  keys.forEach(key => {
    if (host.hasOwnProperty(key) && host[key]) {
      // Ignore empty array
      if (Array.isArray(host[key]) && !host[key].length) {
        return
      }

      smallerHost[key] = host[key]
    }
  })

  CACHE_HOST[hostname] = smallerHost

  return smallerHost
}


function deleteCache(hostname) {
  delete CACHE_HOST[hostname]
}


function dnsLookup(hostname, callback) {
  let xhr = new XMLHttpRequest()
  xhr.open('GET', 'https://geonet.shodan.io/api/dns/' + hostname, true)
  xhr.responseType = 'json'
  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4) {
      let data = xhr.response

      if (data['answers']) {
        callback(data['answers'][0]['value'])
      } else {
        deleteCache(hostname)
      }
    }
  }
  xhr.onerror = () => {
    // Delete "fetching" status
    deleteCache(hostname)
  }
  xhr.send()
}


function hostLookup(hostname, ip, callback) {
  let xhr = new XMLHttpRequest()
  xhr.open('GET', 'https://internetdb.shodan.io/' + ip, true)
  xhr.responseType = 'json'
  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4) {
      let host = xhr.response
      if (!host.error) {
        callback(host)
      } else {
        deleteCache(hostname)
      }
    }
  }
  xhr.onerror = () => {
    // Delete "fetching" status
    deleteCache(hostname)
  }
  xhr.send()
}


function updateHost(host, tabId) {
  chrome.browserAction.enable(tabId)

  chrome.browserAction.setBadgeText({
    'text': host.ports.length.toString(),
  })
}


function updateBrowserAction(tabId, url) {
  // If the URL doesn't start with http or https then we won't go any further
  if (url.indexOf('http') !== 0) {
    return
  }

  let hostname = getHostname(url)

  // Disable the browser action button until we know that the current
  // hostname has some data.
  chrome.browserAction.disable(tabId)
  chrome.browserAction.setBadgeText({
    'text': '',
  })

  // If we're switching tabs or the URL is already in the cache, try to look up the host information
  // from the cache.
  let cached = CACHE_HOST[hostname]
  if (cached) {
    // Prevent calling same host multiple times
    if (cached == 'fetching') {
      return
    }

    // We've previously looked up the Shodan host information for this hostname, so use it
    updateHost(CACHE_HOST[hostname], tabId)
    return
  }

  CACHE_HOST[hostname] = 'fetching'

  // Resolve the hostname to its IP address, which then gets passed to the actual Shodan host lookup
  dnsLookup(hostname, ip => {
    hostLookup(hostname, ip, host => {
      // Make sure we got a response back for the right IP
      if (host.ip === ip) {
        // Update the hostname cache so we know when the browseraction needs to get updated
        host = saveCache(hostname, host)

        // Only update browserAction if current tab's hostname is the same as result
        chrome.tabs.query({ active: true }, tabs => {
          tabs.forEach(tab => {
            let tabHostname = getHostname(tab.url)
            if (hostname === tabHostname) {
              updateHost(host, tabId)
            }
          })
        })
      } else {
        // Delete "fetching" status
        deleteCache(hostname)
      }
    })
  })
}


function contextMenuHandler(info, tab) {
	let query = ''

  // The user has selected some text
  if (info.selectionText) {
    query = info.selectionText
  } else {
    let checkUrl = info.linkUrl || info.pageUrl || info.frameUrl || null
    if (checkUrl) {
      let hostname = getHostname(checkUrl)

      // Strip any prepending 'www.' if present
      if (hostname.indexOf('www.') === 0) {
        hostname = hostname.substr(4)
      }

      query = 'hostname:' + hostname
    }
  }

  if (query) {
    let shodanUrl = 'https://www.shodan.io/search?query=' + encodeURIComponent(query)
    chrome.tabs.create({
      'url': shodanUrl,
    })
  }
}


/*
 * Listen for changes in the URL in any of the tabs.
 */
chrome.tabs.onUpdated.addListener(function (id, info, tab) {
  if (tab.status === 'loading') {
    updateBrowserAction(id, tab.url)
  }
})

chrome.tabs.onActivated.addListener(function (activeInfo) {
  if (activeInfo.tabId) {
    chrome.tabs.get(activeInfo.tabId, function (tab) {
      updateBrowserAction(tab.id, tab.url)
    })
  }
})

// Set the button to disabled until we get some actual data
chrome.browserAction.disable()

chrome.browserAction.setBadgeBackgroundColor({
  'color': '#000',
})

// Add the ability to search Shodan using the right-click/ context menu
chrome.contextMenus.create({
  'title': 'Search Shodan for link',
  'contexts': ['link'],
  'onclick': contextMenuHandler,
})

chrome.contextMenus.create({
  'title': 'Search Shodan for current website',
  'contexts': ['page'],
  'onclick': contextMenuHandler,
})

chrome.contextMenus.create({
  'title': 'Search Shodan for "%s"',
  'contexts': ['selection'],
  'onclick': contextMenuHandler,
})

// Communitcate between popup and background page
chrome.runtime.onMessage.addListener((data, sender, sendResponse) => {
  if (data.cmd === 'getHost') {
    let hostname = getHostname(data.url)
    let cachedHost = CACHE_HOST[hostname]

    if (cachedHost) {
      sendResponse({
        'hostname': hostname,
        'host': cachedHost,
      })
    }
  }
})
