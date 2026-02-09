FROM node:20-slim AS front-base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

COPY front /app
WORKDIR /app

FROM front-base AS front-build
# added 2 lines here to fix build error with pnpm
RUN printf "allowBuilds:\n  esbuild: true\n" > /app/pnpm-workspace.yaml
# changed to --no-frozen-lockfile
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --no-frozen-lockfile
# used 1.70.0 sass
RUN pnpm add -D sass@^1.70.0
RUN pnpm run build

FROM nginx:1.21.0-alpine

COPY ./docker/front/proxy_params /etc/nginx/proxy_params
COPY ./docker/front/app.conf /etc/nginx/conf.d/default.conf
COPY --from=front-build /app/dist /front
