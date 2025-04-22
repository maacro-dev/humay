FROM node:18-alpine AS development

RUN npm install -g pnpm

WORKDIR /app

COPY apps/web/package.json apps/web/pnpm-lock.yaml ./

RUN pnpm install --frozen-lockfile

COPY apps/web .

EXPOSE 5173

CMD ["pnpm", "run", "dev"]
