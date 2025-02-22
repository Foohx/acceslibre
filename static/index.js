import '@gouvfr/dsfr/dist/dsfr/dsfr.module.min.js'

import 'leaflet'
import 'leaflet.markercluster'
import 'leaflet.locatecontrol'
import 'leaflet-center-cross'
import Chart from 'chart.js/auto'
window.Chart = Chart

import { Crisp } from 'crisp-sdk-web'
Crisp.configure('600aff6d-b1eb-414c-a186-233177221bbf')

// Bootstrap
import * as bootstrap from 'bootstrap'

// Sentry
import * as Sentry from '@sentry/browser'
import { Integrations } from '@sentry/tracing'
window.Sentry = Sentry
window.SentryIntegrations = Integrations

// app modules
import dom from './js/dom'
import geo from './js/geo'
import ui from './js/ui'
import cloneFilter from './js/ui/CloneFilter'
import Autocomplete from './js/ui/AutocompleteActivity'

// Initializations
dom.ready(() => {
  dom.mountOne('#app-map', geo.AppMap)
  dom.mountOne('#localisation-map', ui.LocalisationMap)
  dom.mountOne('#map-height-toggle-link', ui.MapExpander)
  dom.mountOne('.a4a-conditional-form', ui.ConditionalForm)
  dom.mountAll('.search-where-field', ui.SearchWhere)
  dom.mountAll('.asteriskField', ui.AsteriskField)
  dom.mountAll('.a4a-geo-link', ui.GeoLink)
  dom.mountAll('.get-geoloc-btn', ui.GetGeolocBtn)
  dom.mountAll('.half-progress', ui.ProgressBar)
  dom.mountAll('.a4a-label-tag', ui.LabelTag)
  dom.mountAll('.a4a-clone-filter', cloneFilter.cloneFilter)
  dom.mountOne('#clone-filter-submit', cloneFilter.cloneFilterSubmit)
  dom.mountOne('#no_activity', ui.NewActivity)
})

// expose general namespaced lib for usage within pages
window.a4a = {
  dom,
  geo,
}

window.onload = function () {
  var src = document.getElementById('id_email'),
    dst = document.getElementById('id_username')

  if (src && dst) {
    src.addEventListener('input', function () {
      dst.value = src.value.split('@')[0]
    })
  }

  ui.listenToLabelEvents()
}
