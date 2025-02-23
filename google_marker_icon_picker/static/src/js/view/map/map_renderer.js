odoo.define('google_marker_dynamic_color.MapRenderer', function (require) {
    'use strict';

    var GoogleMapRenderer = require('web_google_maps.GoogleMapRenderer').GoogleMapRenderer;

    GoogleMapRenderer.include({
        set_property_geometry: function (params) {
            this._super(params);
            this.fieldMarkerColor = params.fieldMarkerColor;
        },
        _createMarker: function (latLng, record, color) {
            color =
                (record.data[this.fieldMarkerColor] ? record.data[this.fieldMarkerColor] : color) ||
                'red';
            this._super(latLng, record, color);
        },
    });
});
