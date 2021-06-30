odoo.define('google_marker_dynamic_color.MapView', function (require) {
    'use strict';

    var GoogleMapView = require('web_google_maps.GoogleMapView');

    GoogleMapView.include({
        set_property_geometry: function (params) {
            this._super(params);
            this.rendererParams.fieldMarkerColor = this.arch.attrs.color;
        },
    });
});
