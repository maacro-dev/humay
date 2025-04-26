FROM node:23-alpine AS development

RUN npm install -g pnpm
RUN corepack enable

WORKDIR /app

COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./

COPY apps/web ./apps/web

COPY packages ./packages

RUN pnpm install --frozen-lockfile

WORKDIR /app/apps/web

EXPOSE 5173

CMD ["pnpm", "run", "dev"]
