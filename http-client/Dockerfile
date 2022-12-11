FROM php:7.4-apache
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
WORKDIR /var/www/html
COPY http-client/src /var/www/html/
RUN mkdir images && chmod 777 -R /var/www