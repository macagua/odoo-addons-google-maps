odoo.define('web_google_maps.view_registry', function (require) {
    'use strict';

    var GoogleMapView = require('web_google_maps.GoogleMapView');
    var view_registry = require('web.view_registry');

    view_registry.add('google_map', GoogleMapView);
});
