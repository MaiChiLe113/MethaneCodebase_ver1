# web/

React 18, TypeScript, Vite, MapLibre GL, TanStack Query, Tailwind. Talks to the API over HTTP only through src/api/client.ts, which is generated from the OpenAPI contract (scripts/gen_ts_client.sh). To create when Nam starts: package.json dependencies, tsconfig.json, vite.config.ts, index.html. Playwright tests in web/e2e mirror the usability acceptance tasks (locate a candidate, interpret evidence and uncertainty, record a review).
