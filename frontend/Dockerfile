FROM node:lts-alpine

EXPOSE 8080

RUN yarn global add http-server

WORKDIR /

COPY package*.json ./

RUN yarn install

ADD . /

RUN yarn run build

CMD [ "http-server", "dist" ]