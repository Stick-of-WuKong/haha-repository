// Quickly create a tree of elements without having to use innerHTML
function createElement(elmName, props) {
  let elm = document.createElement(elmName)
  if (props) {
    for (let key in props) {
      if (props.hasOwnProperty(key) && !elm.hasOwnProperty(key)) {
        let value = props[key]
        if (key.indexOf('-') > -1) {
          elm.setAttribute(key, value)
        } else {
          elm[key] = value
        }
      }
    }
  }

  for (let i = 2, size = arguments.length; i < size; i++) {
    if (typeof arguments[i] == 'string' || typeof arguments[i] == 'number') {
      elm.innerText = arguments[i]
    } else {
      elm.appendChild(arguments[i])
    }
  }
  return elm
}
// Create alias
const CE = createElement


function renderHostnames(host) {
  let $hostnames = CE('ul')

  host.hostnames.forEach(hostname => {
    $hostnames.appendChild(
      CE('li', {},
        CE('a', {
          'href': 'https://' + hostname,
          'target': '_blank',
        }, CE('b', {}, hostname)))
      )
  })

  return $hostnames
}


function renderTable(host) {
  $items = document.getElementById('items')

  let rows = []
  rows.push(['IP Address', host.ip])

  if (host.hostnames && host.hostnames.length) {
    rows.push(['Hostname(s)', ''])
  }

  host.country_name && rows.push(['Country', host.country_name])
  host.city && rows.push(['City', host.city])
  host.os && rows.push(['Operating System', host.os])
  host.org && rows.push(['Organization', host.org])
  host.tags && host.tags.length > 0 && rows.push(['Tags', host.tags.join(', ')])
  host.vulns && host.vulns.length > 0 && rows.push(['Vulnerabilities', host.vulns.join(', ')])

  rows.forEach(row => {
    let child
    if (row[0] == 'Hostname(s)') {
      child = CE('tr', {},
        CE('td', {}, 'Hostname(s)'),
        CE('td', {}, renderHostnames(host))
      )
    } else {
      child = CE('tr', {},
        CE('td', {}, row[0]),
        CE('td', {}, CE('b', {}, row[1]))
      )
    }

    $items.appendChild(child)
  })
}


function renderPorts(host) {
  if (!host.ports || !host.ports.length) {
    return
  }

  const $ports = document.createElement('ul')

  // Convert the array to integers
  host.ports.map(port => parseInt(port))
  host.ports.sort((a, b) => a - b)

  const http_ports = [80, 8080, 81]
  const https_ports = [443, 8443]

  host.ports.forEach(port => {
    let child

    if (http_ports.indexOf(port) != -1) {
      // HTTP port
      child = CE('a', {
        'href': 'http://' + host.ip + ':' + port,
        'target': '_blank',
      }, port)
    } else if (https_ports.indexOf(port) != -1) {
      // HTTPS port
      child = CE('a', {
        'href': 'https://' + host.ip + ':' + port,
        'target': '_blank',
      }, port)
    } else {
      child = CE('span', {}, port)
    }

    $ports.appendChild(CE('li', {}, child))
  })

  document.getElementById('ports').appendChild($ports)
}


function renderVulns(host) {
  if (host.vulns && host.vulns.indexOf('CVE-2014-0160') != -1) {
    const $vulns = document.getElementById('vulns')
    $vulns.style.display = 'block'
  }
}

function renderPopup(data) {
  let host = data['host']
  let hostname = data['hostname']

  document.getElementById('domain').textContent = hostname;

  // Hostnames, location, operating system...
  renderTable(host)

  // Ports
  renderPorts(host)

  // Vulns
  renderVulns(host)

  // Update the links to the IP information and domain data
  document.getElementById('btnIpDetails').href = 'https://www.shodan.io/host/' + host.ip
  document.getElementById('btnDomainDetails').href = 'https://www.shodan.io/domain/' + hostname

  document.body.classList.remove('hidden')
}


// Get host from background page
chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
  let currentTab = tabs[0]
  if (currentTab) {
    chrome.runtime.sendMessage({
      'cmd': 'getHost',
      'url': currentTab.url,
    }, renderPopup)
  }
});
