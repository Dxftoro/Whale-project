FROM nginx:latest

WORKDIR /front/
RUN mkdir /front/css/
RUN mkdir /front/js/
RUN mkdir /front/other/

#COPY ./cfg/nginx.conf /etc/nginx/
COPY ./cfg/host.conf /etc/nginx/conf.d/default.conf

COPY ./index.html /front/
COPY ./extern.html /front/
COPY ./galery.html /front/
COPY ./services.html /front/
COPY ./second_page.html /front/
COPY ./services.html /front/

COPY ./css /front/css
COPY ./js /front/js
COPY ./other /front/other

EXPOSE 80

#CMD ["nginx", "-g", "daemon off;"]
#CMD ["ls", "/front"]
#CMD ["cat", "/etc/nginx/nginx.conf"]
#RUN service nginx restart
