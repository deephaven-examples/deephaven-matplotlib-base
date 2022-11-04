# syntax=docker/dockerfile:1.4

FROM ghcr.io/deephaven/web-plugin-packager:latest as build
RUN ./pack-plugins.sh @deephaven/js-plugin-matplotlib

FROM ghcr.io/deephaven/server:edge
RUN pip install deephaven-plugin-matplotlib
COPY --link --from=build js-plugins/ /opt/deephaven/config/js-plugins/
COPY --link deephaven.prop /opt/deephaven/config/deephaven.prop
