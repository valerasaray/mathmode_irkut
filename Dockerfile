FROM node:18.12.0-alpine

WORKDIR /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ADD . .

RUN npm install
RUN npm i vite

ENTRYPOINT ["/entrypoint.sh"]   

CMD ["npm", "start"]
